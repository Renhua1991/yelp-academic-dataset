import json

f1 = open("businessObjects.json")
f2 = open("IthacaObject.json","w")

Lines = f1.readlines()
for line in Lines:
	json_data = json.loads(line)
	if json_data['city'] == 'Ithaca':
		f2.write(line)

f1.close()
f2.close()
