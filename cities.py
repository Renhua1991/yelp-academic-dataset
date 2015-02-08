import json

f1 = open("businessObjects.json")
f2 = open("city.json","w")

city_list = []
Lines = f1.readlines()
for line in Lines:
	json_data = json.loads(line)
	city = json_data['city']
	if city not in city_list:
		city_list.append(city)
		f2.write(city + '\n')

f1.close()
f2.close()