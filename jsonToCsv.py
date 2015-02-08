import json

#define a function
def convert(x):
	#convert a json string to a python dictionary
	ob=json.loads(x)
	#parse nested json item such as "categories" 
	for k,v in ob.items():
		if isinstance(v,list):
			ob[k]='-'.join(v)
		elif isinstance(v,dict):
			for kk,vv in v.items():
				ob['%s_%s' % (k,vv)]=vv
			del ob[k]
	return ob

#change f1 and f2 if you want to convert a specific json file to csv file
f1=open("IthacaObject.json")
f2=open("IthacaObject.csv","w")

Lines=f1.readlines()
for line in Lines:
	newline=convert(line)
	result=str(newline)
	f2.write(result+'\n')

f1.close()
f2.close()