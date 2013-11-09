#!/usr/bin/env python
import numpy as np
from numpy import sqrt

# A dictionary of movie critics and their ratings of a small
# set of movies. Realistically, data would be in database
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}
# -----------------------------------
# Calculate Euclidean Distance for inter-person similarity
# Returns a distance-based similarity score for person 1 and person 2
# Value of 1 indicated perfect similarity
# Call to prefs refers to Python index of critics above
# From Python interpreter: 
# import my_recommendations
# reload(my_recommendations)
# my_recommendations.sim_distance(critics, 'name', 'name')

def sim_distance(prefs,person1,person2):
  # Get list of shared items
  si = {}
  for item in prefs[person1]:
    if item in prefs[person2]:
      si[item] = 1
  # if the have no ratings in common, return 0
  if len(si) == 0: 
    return 0
  # add up the sum of squares of all the differences
  sum_of_squares = sum([pow(prefs[person1][item] - 
prefs[person2][item],2) for item in si])
  return 1/(1 + sqrt(sum_of_squares))
# -------------------------------------------
# Returns the Pearson correlation coefficient for p1 and p2
# See above for Python interpreter commands

def sim_pearson(prefs,p1,p2):
  # Get list of mutually rated items
  si = {}
  for item in prefs[p1]:
    if item in prefs[p2]:
      si[item] = 1
  # Find the number of mutully rated items
  n = len(si)

  # if no ratings in common, return 0
  if n == 0:
    return 0 
  # Calculate Pearson correlation components
  # Add up all preferences
  sum1 = sum([prefs[p1][it] for it in si])
  sum2 = sum([prefs[p2][it] for it in si])

  # Sum the squares
  sum1Sq = sum([pow(prefs[p1][it],2) for it in si])
  sum2Sq = sum([pow(prefs[p2][it],2) for it in si])

  # Sum up the products
  pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

  # Calculate Pearson Score
  num = pSum - (sum1 * sum2/n)
  den = sqrt((sum1Sq - pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den == 0:
    return 0
  r = num/den

  return r
# ------------------------------
# Now that we have functions for ranking two people (above), create function
# that scores everyone against a given person and finds closest matches

# Returns best matches for person from the prefs dictionary
# Number of results and similarity function are optional params

def topMatches(prefs,person,n=5,similarity=sim_pearson):
  scores = [(similarity(prefs,person,other),other)
    for other in prefs if other!=person]

  # Sort the list so the highest scores appear at the top
  scores.sort( )
  scores.reverse( )
  return scores[0:n]
#---------------------------------
# Gets recommendations for a person by using a weighted
# average of every user's rankings

def getRecommendations(prefs,person,similarity=sim_pearson):
  totals = {}
  simSums = {}
  for other in prefs:
    # don't compare me to myself
    if other == person:
      continue
    sim = similarity(prefs,person,other)

    #ignore scores of zero or lower
    if sim <= 0:
      continue
    for item in prefs[other]:
      # only score movies that i have not seen
      if item not in prefs[person] or prefs[person][item] == 0:
        # Similarity * score
        totals.setdefault(item,0)
        totals[item]+= prefs[other][item] * sim
        # Sum of similarities
        simSums.setdefault(item,0)
	simSums[item] += sim
  # Create the normalized list
  rankings = [(total/simSums[item],item) for item, total in totals.items()]
  # Return the sorted list
  rankings.sort()
  rankings.reverse()
  return rankings

# -------------------------------------
# Now i know how to find similar people and recommend products
# for a given person...
# What if you want to see which products are similar to each other
# e.g., shopping site when it does not know a lot about you

# Transform the critics dictionary
def transformPrefs(prefs):
  result = {}
  for person in prefs:
    for item in prefs[person]:
      result.setdefault(item,{})
      # Flip item and person
      result[item][person] = prefs[person][item]
  return result
#-------------------------------------------------
# Item Based Collaborative Filtering
# Build the "item comparison dataset"
def calculateSimilarItems(prefs,n=10):
  # Create dictionary of items showing which other items
  # they are most similar to
  result = {}
  # Invert the preference matrix to be item-centric
  itemPrefs = transformPrefs(prefs)
  c = 0
  for item in itemPrefs:
    # Status updates for large datasets
    c += 1
    if c%100 == 0:
      print "%d / %d" % (c, len(itemPrefs))
    # find the most similar items to this one
    scores = topMatches(itemPrefs,item, n=n,similarity=sim_distance)
    result[item] = scores
  return result
#----------------------------------------------------
# Now implement Item-based recommendations by building a table
# as was done with getRecommendations() - based on user recommendations
def getRecommendedItems(prefs,itemMatch,user):
  userRatings=prefs[user]
  scores= {}
  totalSim = {}
  
  # Loop over items rated by this user
  for(item,rating) in userRatings.items():
    # Loop over items similar to this one
    # Note: item2 represents columns of unseen user movies
    for (similarity,item2) in itemMatch[item]:
      # Ignore if this user has already rated this item
      if item2 in userRatings: 
        continue
      # Weighted sum of rating times similarity
      scores.setdefault(item2,0)
      scores[item2]+= similarity * rating

      # Sum of all the similarities
      totalSim.setdefault(item2,0)
      totalSim[item2]+= similarity
  # Divide each total score by total weighting to get an average
  rankings = [(score/totalSim[item],item) for item,score in scores.items()]
  # Return the ranking form highest to lowest
  rankings.sort()
  rankings.reverse()
  return rankings

#-------------------------------------------------
# Now working with MovieLens data
def loadMovieLens(path='/home/skerr/DataSets/ml-100k'):
  # Get movie titles
  movies = {}
  for line in open(path+'/u.item'):
    (id,title) = line.split('|')[0:2]
    movies[id] = title

  # Load data
  prefs = {}
  for line in open(path+'/u.data'):
    (user,movieid,rating,ts) = line.split('\t')
    prefs.setdefault(user,{})
    prefs[user][movies[movieid]] = float(rating)
  return prefs

