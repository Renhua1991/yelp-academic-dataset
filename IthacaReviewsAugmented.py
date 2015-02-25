import json

# open json file we need 
f1 = open("IthacaUsers_stars.json")
f2 = open("IthacaReviews.json")
f3 = open("IthacaReviewsAugmented.json","w")

# create a new dictionary for user_id : all_user_information.
dictionary = dict()

# read json file
Lines1 = f1.readlines()
for line1 in Lines1:
	# load data 
	json_data1 = json.loads(line1)
	user_id1 = json_data1['user_id']
	# load the whole line int dictionary
	dictionary[user_id1] = json_data1

	# print isinstance(json_data1, dict)
	# print isinstance(line1, list)
	# print isinstance(line1, dict)

#print dictionary

# read json file
Lines2 = f2.readlines()
for line2 in Lines2:
	# load data
	json_data2 = json.loads(line2)
	# delete votes
	del json_data2['votes']
	# get user_id
	user_id2 = json_data2['user_id']
	
	#print dictionary[user_id2]

	#get all the attribute we need
	name = dictionary[user_id2]['name']
	url = dictionary[user_id2]['url']
	review_count = dictionary[user_id2]['review_count']
	local_review_count = dictionary[user_id2]['local_review_count']
	average_stars = dictionary[user_id2]['average_stars']
	local_review_stars = dictionary[user_id2]['local_average_stars']


	# append user information to reviews
	json_data2['name'] = name
	json_data2['url'] = url
	json_data2['review_count'] = review_count
	json_data2['local_review_count'] = local_review_count
	json_data2['average_stars'] = average_stars
	json_data2['local_review_stars'] = local_review_stars

	f3.write(json.dumps(json_data2) + '\n')

print "done"

f1.close()
f2.close()
f3.close()