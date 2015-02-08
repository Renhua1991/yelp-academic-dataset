import json

f1 = open("dataset.json")
f2 = open("users.json", "w")
f3 = open("reviews.json", "w")
f4 = open("businessObjects.json", "w")

Lines = f1.readlines()
for line in Lines:
	json_data = json.loads(line)
	if json_data['type'] == "user" :
		f2.write(line)
	elif json_data['type'] == "review" :
		f3.write(line)
	else :
		f4.write(line)

f1.close()
f2.close()
f3.close()
f4.close()
			