#!/usr/bin/env python

import sys
import re

# Input file: rats.csv
# Output file: rats_open

# Create pattern that allows to find just open rat complaints 

pattern = '(\d+\/\d+\/\d{4}),(\w{4}),(.*)'
regex = re.compile(pattern)

f = open('rats_open','at')

for line in sys.stdin:
  line = line.strip()
  match = regex.match(line)

  # if we did match, we want to skip to next line, but count the dup
  if match:
    dups += 1
  else:
    f.write(line)
    f.write('\n')
sys.stderr.write('Number of dups: %i' %dups)
sys.stderr.write('\n')

