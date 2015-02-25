import json

f1 = open("IthacaReviews.json")
f2 = open("users.json")
f3 = open("IthacaReviewsUsers.json",'a')

# get all the user_id for Ithaca object
user_list = []
Lines = f1.readlines()
for line in Lines:
	json_data = json.loads(line)
	user_id = json_data['user_id']
	user_list.append(user_id)

# get all the reviews of Ithaca object	
Lines1 = f2.readlines()
for line1 in Lines1:
	json_data1 = json.loads(line1)
	if json_data1['user_id'] in user_list:
		f3.write(line1)

#print user_list

f1.close()
f2.close()
f3.close()