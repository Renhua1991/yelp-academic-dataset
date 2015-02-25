import json

f1 = open("businessObjects.json")
f2 = open("reviews.json")
f3 = open("IthacaReviews.json",'a')

# get all the business_id of Ithaca object
business_location = []
Lines = f1.readlines()
for line in Lines:
	json_data = json.loads(line)
	business_id = json_data['business_id']
	location = json_data['city']
	if location == "Ithaca":
		business_location.append(business_id)

# get all the reviews of Ithaca object	
Lines1 = f2.readlines()
for line1 in Lines1:
	json_data1 = json.loads(line1)
	if json_data1['business_id'] in business_location:
		f3.write(line1)


f1.close()
f2.close()
f3.close()