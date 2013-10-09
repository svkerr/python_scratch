import json
import csv

f = open('ufo_awesome.json')
data = json.load(f)

f.close()

f=csv.writer(open('test.csv','wb+'))

f.writerow([item['pk'],item['model']] + item['fields'].values())
