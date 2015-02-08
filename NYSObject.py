import json

f1 = open("businessObjects.json")
f2 = open("NYSObject.json","w")

Lines = f1.readlines()
for line in Lines:
	json_data = json.loads(line)
	if json_data['state'] == 'NY':
		f2.write(line)

f1.close()
f2.close()