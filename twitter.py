import twitter
from twitter import *
import pprint
# see "Authentication" section below for tokens and keys

OAUTH_TOKEN = "585421028-zyBh2Opwk6SMiEAZRwb5CjHgB4utNfEKY5f8j6md"
OAUTH_SECRET = "1RXrBsgz88wqbX8En2urOnKKfP6DHATpH9dfIBNzBfU"
CONSUMER_KEY = "hwu3JBY0QHoLy05xpj1G6w"
CONSUMER_SECRET ="kJ27v6yuibGGzzkjI8lnDaOBEcdwHEb4c8YV5fs"

t = Twitter(
            auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                       CONSUMER_KEY, CONSUMER_SECRET)
           )

# Get your "home" timeline
results = t.search.tweets(q = "obama")
pprint.pprint(results[0])

#twitter_stream = TwitterStream(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
#                      CONSUMER_KEY, CONSUMER_SECRET))
#iterator = twitter_stream.statuses.sample()
#for tweet in iterator:
#        try:
#                if tweet['geo'] != None:
#                       pprint.pprint(tweet)
#                        print '================'
#                        pprint.pprint(tweet['text'])
#                        pprint.pprint(tweet['place'])
#                        print '================'
#        except:
#                pass;
