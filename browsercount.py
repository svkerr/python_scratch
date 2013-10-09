#!/usr/bin/env python

# The next two lines import the 're' (regular 
# expression) and 'sys' (system) modules.  The
#'sys' module is needed to read from standard
# input and to write to the standard error stream.
import re
import sys

# The regular expression pattern we'll use to parse
# individual fields from the Apache log file.  Here's
# the order in which those fields appear, along with 
# a brief description and an example.  Note that the 
# user agent (browser) field is very long and the 
# example value shown here has been truncated so that
# it will fit into the table.
#
# Index Field        Example value
# ----- ------------ ----------------------------------------------------
#    1 	IP address   192.168.13.2
#    2	Ident        -  (seldom populated on modern servers)
#    3	User         -  (never used in this log)
#    4	Date/Time    [22/Sep/1997:15:01:46 -0800]
#    5	Request      "GET /rate?movie=250&rating=4 HTTP/1.1"
#    6	Status code  200
#    7	Bytes sent   7
#    8	Referer      "http://clouderamovies.com/"
#    9	User agent   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) ..."
#   10	Cookie       "USER=29"
#
# NOTE: the pattern itself contains double quotes, so we use single quotes
# to define the string so we don't have to escape embedded double quotes.
pattern = '(\d+\.\d+\.\d+\.\d+) (.*) (.*) \[(.*)\] "(.*)" (\d+) (.*) "(.*)" "(.*)" "(.*)"'

regex = re.compile(pattern)

# We're going to count the operating systems used to 
# access our site, based on the contents of the user 
# agent field.  We need to initialize the variables
# we'll use to keep track of each type.
mac = 0
windows = 0

# read each line from the standard input stream
for line in sys.stdin:
  line = line.strip()
  match = regex.match(line)

  # if we did match, extract the 9th (user agent) field
  if match:
    field = match.group(9)

    # check for substrings indicating the operating system
    if "Mac OS X" in field:
      mac = mac + 1
    elif "Windows" in field:
      windows = windows + 1
  # if we didn't match, print a warning to standard error
  else:
    sys.stderr.write("ERROR: Could not parse line '%s'" % line)

# add values to get the total number of requests
total = mac + windows

# print out the total number of requests
print "There were %i total requests" % total

# print out the number of requests by type
print "  Mac requests:     %i" % mac
print "  Windows requests: %i" % windows
