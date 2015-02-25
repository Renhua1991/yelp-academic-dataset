import json

# open json file we need 
f1 = open("IthacaReviews.json")
f2 = open("newIthacaReviewsUsers.json")
f3 = open("IthacaUsers_stars.json","w")

# create a new dictionary for user_id : total_Ithaca_stars.
total_Ithaca_stars = dict()

# read json file
Lines1 = f1.readlines()
for line1 in Lines1:
	# load data and get user_id, stars for every review
	json_data1 = json.loads(line1)
	user_id1 = json_data1['user_id']
	stars = json_data1['stars']

	# if the user_id is not in total_Ithaca_stars
	if( user_id1 not in total_Ithaca_stars ):
		total_Ithaca_stars[user_id1] = stars
	# if the user_id is still in total_Ithaca_stars
	else:
		total_Ithaca_stars[user_id1] += stars

# read json file 
Lines2 = f2.readlines()
for line2 in Lines2:
	# load data
	json_data2 = json.loads(line2)
	# delete the attribute of votes
	del json_data2['votes']
	# get the user_id
	user_id2 = json_data2['user_id']
	# get the local count
	local_count = json_data2['local_review_count']
	# compute average-stars and add it to json
	total_stars = total_Ithaca_stars[user_id2]
	json_data2['local_average_stars'] = total_stars/local_count
	# write it to the json file
	f3.write(json.dumps(json_data2) + '\n')

	#print json_data2

#print total_Ithaca_stars



f1.close()
f2.close()
f3.close()