import csv
values = {} # create empty dictionary
for i in csv.reader(open("/home/skerr/AWK/DAuditNew10000_1-8_noquotes",'rb'),dialect='excel'):
	try:
		if i[2] == 'Fetch':
			dataid = i[4]
			perf = i[7]
			if dataid in values:
				values[dataid].append(perf)
			else:
				values[dataid] = [] 	
				values[dataid].append(perf)
	except:
			print 'ERRRRRRR'


print '+++++++++++++++++++++++++++++++++++++++++++++++'
for key in values.keys():
	values[key] = list(set(values[key]))
	print key,values[key]
