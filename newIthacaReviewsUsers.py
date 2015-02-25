import json

f1 = open("IthacaReviewsUsers.json")
f2 = open("IthacaReviews.json")
f3 = open("IthacaReviewsUsers.json")
f4 = open("newIthacaReviewsUsers.json", "a")

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

Lines2 = f3.readlines()
for line2 in Lines2:
	json_data2 = json.loads(line2)
	if json_data2['user_id'] in ithaca_review_count:
		x = ithaca_review_count[json_data2['user_id']]
		json_data2['ithaca_review_count'] = x
		f4.write(str(json_data2)+'\n')


f1.close()
f2.close()
f3.close()
f4.close()