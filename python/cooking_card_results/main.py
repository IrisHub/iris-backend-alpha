import boto3
import json
import time
import math
import random
# import numpy as np
from datetime import datetime
from datetime import timedelta

def event_handler(event, context):

# def test():
	# now = time.time()
	# s3 = boto3.client('s3')
	# data = s3.get_object(Bucket='yummly-recipes', Key='all_yummly.json')
	# data = data['Body'].read().decode('utf-8')

	# data = json.loads(data)

	# print(len(data)) {"user_id":	"17ef5c4b-3ac9-4548-a309-41e30a61c6e8", "query": {"query_type": "ingredient", "query_body": "Chicken"}}
	# print(f"Time for execution: {time.time()- now}")
	diet_dict = {
		"vegan": 0,
		"vegetarian": 1,
		"pescatarian": 2,
		"no preference": 3,
		"none":3
	}

	difficulty_dict = {
		'beginner': 0,
		'intermediate': 1,
		'advanced': 2
	}

	data = json.load(open('all_yummly.json', 'r'))
	print(len(data))
	dynamodb = boto3.client('dynamodb')
	print(event)
	if 'user_id' in event.keys():
		user_id = event['user_id']
		query_type = event['query_type']
		query_string = event['query_string']
	elif 'body' in event.keys():
		user_id = json.loads(event['body'])['user_id']

	try:
		response = dynamodb.get_item(TableName='iris_users', Key={"user_id":{"S":str(user_id)}})
		response = response["Item"]
	except Exception as e:
		print(e)

	hour = (datetime.now()-timedelta(hours=7)).hour
	# hour = (hour-7) % 24
	time_for_lunch = response['preferences']['M']['max_time_lunch']['S'].lower()
	time_for_dinner = response['preferences']['M']['max_time_dinner']['S'].lower()
	time_for_breakfast = "under 30 minutes"

	if hour > 2 and hour < 11:
		meal = "Breakfast"
		cooking_time = time_for_breakfast
	if hour >= 11 and hour < 16:
		meal = "Lunch"
		cooking_time = time_for_lunch
	else:
		meal = "Dinner"
		cooking_time = time_for_dinner

	ret = {}
	ret['category'] = query_type
	ret['title'] = 'Your results for'
	ret['item'] = query_string.title()
	ret['subtitle'] = f"Created for {(datetime.now()-timedelta(hours=7)).strftime('%I:%M %p')}"

	data = [e for e in data if diet_dict[e['diet'].lower()] <= diet_dict[response['preferences']['M']['diet']['S'].lower()]]
	print(f"Data after diet filter: {len(data)}")
	common_ingredients = [e['S'].lower() for e in response['preferences']['M']['ingredients']['L']]
	bad_ingredients = [e['S'].lower() for e in response['preferences']['M']['disliked_foods']['L']]
	bad_recipes = [e['S'] for e in response['disliked_recipes']['L']]
	if 'seafood' in bad_ingredients:
		bad_ingredients.extend(['fish', 'shellfish'])
	if "shellfish" in bad_ingredients:
		bad_ingredients.extend(['lobster', 'shrimp', 'clam', 'mussel', 'crab'])
	if 'fish' in bad_ingredients:
		bad_ingredients.extend(['cod', 'tilapia', 'salmon'])
	top_cuisines = [e['S'].lower() for e in response['preferences']['M']['top_cuisines']['L']]
	difficulty = response['preferences']['M']['cooking_level']['S'].lower()

	new_data = []
	for e in data:
		flag = True
		if e['uuid'] in bad_recipes:
			flag = False
		for bad_ingredient in bad_ingredients:
			for ingredient in e['ingredientLines']:
				if bad_ingredient in ingredient.lower():
					flag = False
		if not flag:
			continue
		e['score'] = 1

		if query_type.lower() == 'ingredient':
			for a in e['ingredientLines']:
				if query_string.lower()[:-1] in a.lower():
					e['score'] = 50
		elif query_type.lower() == 'dish':
			if query_string.lower()[:-1] in e['name'].lower():
				e['score'] = 50
		elif query_type.lower() == 'cuisine':
			if query_string.lower() == e['cuisine'].lower():
				e['score'] = 50
		else:
			print("LSKJDFLSKADJFKJ")
		if "30" in cooking_time:
			if e['totalTimeInSeconds'] <= 30*60:
				e['score'] += 2
		elif "45" in cooking_time:
			if e['totalTimeInSeconds'] <= 45*60:
				e['score'] += 2
		
		if meal == 'Lunch' and 'lunch' in e['course'].lower():
			e['score'] += 2
		elif meal == 'Breakfast' and 'breakfast' in e['course'].lower():
			e['score'] += 2

		for ingredient in common_ingredients:
			for a in e['ingredientLines']:
				if ingredient.lower() in a.lower():
					e['score'] += 1
		if e['cuisine'].lower() in top_cuisines:
			e['score'] += 3
		if difficulty_dict[e['difficulty'].lower()] <= difficulty_dict[difficulty]:
			e['score'] += 5

		new_data.append(e)


	data = new_data
	data = sorted(data, reverse=True, key=lambda x: x['score'])
	# data.sort(key=lambda x: x['score'])

	print(len(data))

	recipes = data[:3]
	print([e['score'] for e in recipes])
	recipe_list = [{
		'title': e['name'],
		'id': e['uuid'],
		'rating': f"{random.randint(80,100)}% liked",
		'cook_time': f"{e['totalTimeInSeconds']//60} mins",
		'difficulty': e['difficulty'],
		'ingredients': e['ingredientLines'],
		'link': e['url'],
		'image_url': f"https://yummly-images.s3-us-west-1.amazonaws.com/img{e['image_id']}.jpg",
		# 'image_url': f"https://yummly-images.s3-us-west-1.amazonaws.com/img00001.jpg",
	} for e in recipes]

	ret['results'] = recipe_list

	# sample_data = {
	# 	'category': "ingredient",
	# 	'title': "Your results for",
	# 	'item': "Chicken",
	# 	'subtitle': "Created for 3:20pm",
	# 	'results':[
	# 		{
	# 			'title': "Chinese Chicken and Broccoli",
	# 			'id': "86ad1f34-5551-46d6-a96d-e0dd721933eb",
	# 			'rating': "91% liked",
	# 			'cook_time': "30 min",
	# 			'difficulty': "Intermediate",
	# 			'image_url': "https://yummly-images.s3-us-west-1.amazonaws.com/img10591.jpg",
	# 			'ingredients': [
	# 				"2 boneless, skinless chicken breasts, cut into bite-sized pieces",
	# 				"1 large head of broccoli, crowns only, cut into bite-sized pieces",
	# 				"1 tablespoon vegetable oil",
	# 				"2 tablespoons vegetable oil",
	# 				"1 tablespoon water",
	# 				"1/2 teaspoon baking soda",
	# 				"1 teaspoon sugar",
	# 				"2 teaspoons cornstarch",
	# 				"1 tablespoon reduced-sodium soy sauce",
	# 				"1/4 cup + 1 tablespoon reduced-sodium soy sauce",
	# 				"2 tablespoons brown sugar",
	# 				"4 cloves garlic, minced",
	# 				"2 tablespoons flour",
	# 				"1 tablespoon rice vinegar",
	# 				"1 tablespoon vegetable oil",
	# 				"2 tablespoons water"
	# 			],
	# 			'link': "http://www.simplywhisked.com/chinese-chicken-and-broccoli/"
	# 		},
	# 		{
	# 			'title': "Chinese Chicken and Broccoli",
	# 			'id': "86ad1f34-5551-46d6-a96d-e0dd721933eb",
	# 			'rating': "91% liked",
	# 			'cook_time': "30 min",
	# 			'difficulty': "Intermediate",
	# 			'image_url': "https://yummly-images.s3-us-west-1.amazonaws.com/img10591.jpg",
	# 			'ingredients': [
	# 				"2 boneless, skinless chicken breasts, cut into bite-sized pieces",
	# 				"1 large head of broccoli, crowns only, cut into bite-sized pieces",
	# 				"1 tablespoon vegetable oil",
	# 				"2 tablespoons vegetable oil",
	# 				"1 tablespoon water",
	# 				"1/2 teaspoon baking soda",
	# 				"1 teaspoon sugar",
	# 				"2 teaspoons cornstarch",
	# 				"1 tablespoon reduced-sodium soy sauce",
	# 				"1/4 cup + 1 tablespoon reduced-sodium soy sauce",
	# 				"2 tablespoons brown sugar",
	# 				"4 cloves garlic, minced",
	# 				"2 tablespoons flour",
	# 				"1 tablespoon rice vinegar",
	# 				"1 tablespoon vegetable oil",
	# 				"2 tablespoons water"
	# 			],
	# 			'link': "http://www.simplywhisked.com/chinese-chicken-and-broccoli/"
	# 		},
	# 		{
	# 			'title': "Chinese Chicken and Broccoli",
	# 			'id': "86ad1f34-5551-46d6-a96d-e0dd721933eb",
	# 			'rating': "91% liked",
	# 			'cook_time': "30 min",
	# 			'difficulty': "Intermediate",
	# 			'image_url': "https://yummly-images.s3-us-west-1.amazonaws.com/img10591.jpg",
	# 			'ingredients': [
	# 				"2 boneless, skinless chicken breasts, cut into bite-sized pieces",
	# 				"1 large head of broccoli, crowns only, cut into bite-sized pieces",
	# 				"1 tablespoon vegetable oil",
	# 				"2 tablespoons vegetable oil",
	# 				"1 tablespoon water",
	# 				"1/2 teaspoon baking soda",
	# 				"1 teaspoon sugar",
	# 				"2 teaspoons cornstarch",
	# 				"1 tablespoon reduced-sodium soy sauce",
	# 				"1/4 cup + 1 tablespoon reduced-sodium soy sauce",
	# 				"2 tablespoons brown sugar",
	# 				"4 cloves garlic, minced",
	# 				"2 tablespoons flour",
	# 				"1 tablespoon rice vinegar",
	# 				"1 tablespoon vegetable oil",
	# 				"2 tablespoons water"
	# 			],
	# 			'link': "http://www.simplywhisked.com/chinese-chicken-and-broccoli/"
	# 		},
	# 	]
	# }

	return json.loads(json.dumps(ret))