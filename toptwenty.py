import json

f1 = open("IthacaObject.json")
f2 = open("reviews.json")
f3 = open("toptwentyIthaca.json", "w")
f4 = open("IthacaObject.json")

#create a new dictionary
d = dict()

#get a dictionary with d{'id of restaurant1':0, ....}
Lines = f1.readlines()
for line in Lines:
		json_data = json.loads(line)
		objects_id = json_data['business_id']
		d[objects_id] = 0

# get the number of views of every restaurant in Ithaca
Lines1 = f2.readlines()
for line1 in Lines1:
		json_data1 = json.loads(line1)
		data_id = json_data1['business_id']
		if data_id in d :
			d[data_id] += 1

dictlist = []
for key, value in d.iteritems():
	temp = [value, key]
	dictlist.append(temp)

#sort according to the numbers of reviews and get the top ten restaurants in Ithaca
dictlist.sort(reverse=True)
newlist = dictlist[:20:]

alist = []
for a in newlist:
	alist.append(a[1])

#get the name of the top ten restraurants in Itahca 
newLines = f4.readlines()
for newline in newLines:
	json_data2 = json.loads(newline)
	if json_data2['business_id'] in alist:
		f3.write(json_data2['name'] + "\n")


f1.close()
f2.close()
f3.close()
f4.close()
