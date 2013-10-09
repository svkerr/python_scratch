#!/usr/bin/env python

import sys
import re

# Input file: rats.csv
# Output file: rats_non_dups
# This is first step in processing rats.csv file
#
# following this processing, we then execute from shell:
#   cat rats_non_dups | rev | cut -d',' --complement -f1,2 | rev > filename 
# following this shell command, we then remove the comma between the quotes:
#   cat rats_non_dups_nolatlon | sed -e 's/"\(.*\),\(.*\)"/\1\2/g' > rats_comma_removed
#
# Create pattern that accounts for two cases:
#   Completed - Dup
#   Open - Dup
pattern = '(\d+\/\d+\/\d{4}),(\w{4,} - Dup),(.*)'
regex = re.compile(pattern)

dups = 0 

f = open('rats_non_dups','at')

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

