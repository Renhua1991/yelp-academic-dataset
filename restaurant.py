import json

f1 = open("reviews.json")
f2 = open("Moosewood Restaurant.json","w")

#is's convenient to use the business_id rather than business name. 
Lines = f1.readlines()
for line in Lines:
	json_data = json.loads(line)
	if json_data['business_id'] == "TA8Jj9Gsl6gvNrIP8hpvew":
		f2.write(line)

f1.close()
f2.close()