import json
import collections

f1=open("businessObjects.json")
f2=open("reviews.json")
f3=open("user_location3.json","w")

# create a dictionary that stores businessObject and its location 
a=dict()
Lines1=f1.readlines()
for line1 in Lines1:
	json_line1=json.loads(line1)
	businessid1=json_line1['business_id']
	#print businessid
	businesscity1=json_line1['city']
	#print businesscity
# if business is not in the dictionary, we put it into the dict; else, let it go.
	if(businessid1 not in a):
		#a.update({'businessid':businesscity})
		a[businessid1]=businesscity1
# we get all (business,city) in a now.
#print a

# create a new dictionary. {user_id1:{city1:count1,city2:count2,...},user_id2:{...},...}
b=dict()
# set the count of cities to 0 at the beginning.
#count=1
Lines2=f2.readlines()
for line2 in Lines2:
	json_line2=json.loads(line2)
	userid=json_line2['user_id']
	businessid2=json_line2['business_id']
	city=a[businessid2]
	#print city
	#if user is not in dictionary.
	if(userid not in b):
		b[userid]={}
		b[userid][city]=1
		#print b[userid]

	#if user is still in dictionary.
	else:
		if(city not in b[userid]):
			b[userid][city]=1
			#print "yes"
		else:
			b[userid][city]+=1
			#print "no"

	#f3.write(b[userid])
#print b

#c is dict that used to store userid and its location
c=dict()
#x=1
for k in b.keys():
	vals=b[k].values()
	maxvals=max(vals)
	c[k]=[]
	for k2 in b[k].keys():
		if b[k][k2]==maxvals:
			#c[k]={}
			c[k].append(k2)
			#result=(str)({k:c[k]})
			#f3.write(result+'\n')
			#print ({k:c[k]})
			#print x
			#x+=1


for d in c.keys():
	#str_result=(str)({d:c[d]})
	json_result=json.dumps({d:c[d]})
	f3.write(json_result+'\n')

#with open('user_location2.json','w') as outfile:
#	json.dump(c, outfile, indent=2)
	

#print c

f1.close()
f2.close()
f3.close()
