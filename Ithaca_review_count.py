import json

f1 = open("IthacaReviewsUsers.json")
f2 = open("IthacaReviews.json")
f3 = open("ithaca_review_count.json", "a")

ithaca_user_list = []
Lines = f1.readlines()
for line in Lines:
	json_data = json.loads(line)
	user_id = json_data['user_id']
	ithaca_user_list.append(user_id)

ithaca_review_count = dict()
Lines1 = f2.readlines()
for line1 in Lines1:
	#i = 1
	json_data1 = json.loads(line1)
	userid = json_data1['user_id']
	if userid in ithaca_user_list:
		if userid not in ithaca_review_count:
			ithaca_review_count[userid] = 1
		else:
			ithaca_review_count[userid] += 1

#print ithaca_review_count

for key in ithaca_review_count:
	json_result=json.dumps({key:ithaca_review_count[key]})
	f3.write(json_result+'\n')



f1.close()
f2.close()
f3.close()
