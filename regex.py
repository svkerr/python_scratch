#!/usr/bin/env python

# import the re (regular expression) module, which
# is required to use regular expressions in Python
import re

data = "Smith,John  212-555-1234/smith@example.com"

# There are four fields, and therefore, four 
# capture groups (the values in parentheses)
#
# Quick regex primer: 
#
# .  matches any character
# \d matches a digit [0-9]
# \w matches "word" characters (letters or digits)
# * matches zero or more of the preceding character
# + matches one or more of the preceding character
# {N} matches exactly N occurrences of the preceding character
# 
# first name: one or more word characters 
#   followed by a comma
# last name: one or more word characters
#   followed by any number of whitespace characters
# phone number: 3 digits, dash, 3 digits, dash, 4 digits
#   followed by a forward slash
# email address: any content after the slash
pattern = "(\w+),(\w+)\s+(\d{3}-\d{3}-\d{4})/(.*)"

# We must compile this string into a regular 
# expression object before we can use it.
regex = re.compile(pattern)

# If leading and trailing whitespace isn't needed, it's 
# a good idea strip it off using the string's strip()
# method.  This will make the strings more consistent
# and easier to parse.
data = data.strip()

# try to match our pattern on the string
match = regex.match(data)

# if we did match, extract the individual fields
if match:
  fname = match.group(1)
  lname = match.group(2)
  phone = match.group(3)
  email = match.group(4)

# If we didn't match, print an error message
else:
  print "ERROR: Could not parse string!"

# Finally, print out the values of the parsed fields
print "First Name: %s" % fname 
print "Last Name:  %s" % lname 
print "Phone:      %s" % phone
print "E-Mail:     %s" % email
