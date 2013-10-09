## Reads in birth name files in csv format
## 2011 is the last available year right now
## NOTE(s):
## 1. This script relies on pandas
## 2. Stores pandas dataframe in file called names
## 3. To recover dataframe: names = pd.DataFrame.load('names')

import pandas as pd

years = range(1880,2012)
pieces = []
columns = ['names','sex','births']

for year in years:
	path = '../Names/yob%d.txt' % year
	frame = pd.read_csv(path, names = columns)

	frame['year'] = year
	pieces.append(frame)

## concantenate everything into a single file system
names = pd.concat(pieces, ignore_index=True)
names.save('names')

