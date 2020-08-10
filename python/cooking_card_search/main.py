import json, os, time, random
from datetime import datetime
import boto3
import numpy as np

def event_handler(event, context):

	diet_dict = {
		"vegan": 0,
		"vegetarian": 1,
		"pescatarian": 2,
		"no preference": 3,
		"none":3
	}

	dynamodb = boto3.client('dynamodb')

	if 'user_id' in event.keys():
		user_id = event['user_id']
	elif 'body' in event.keys():
		user_id = json.loads(event['body'])['user_id']

	options = json.loads(open('info.json', 'r').read())

	try:
		response = dynamodb.get_item(TableName='iris_users', Key={"user_id":{"S":str(user_id)}})
		response = response["Item"]
	except Exception as e:
		print(e)

	hour = datetime.now().hour
	hour = (hour-7) % 24
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
	ret['title'] = f"{meal} {cooking_time}"
	ret['subtitle'] = "For you"
	ret['data'] = {}
	ingredients = options['ingredients']
	ingredients = [a for a in ingredients if a['name'].lower() not in [e['S'].lower() for e in response['preferences']['M']['disliked_foods']['L']]]
	ingredients = [a for a in ingredients if diet_dict[a['diet'].lower()] <= diet_dict[response['preferences']['M']['diet']['S'].lower()]]
	for e in ingredients:
		e['weight'] = 1
		if e['name'].lower() in [e['S'].lower() for e in response['preferences']['M']['ingredients']['L']]:
			e['weight'] += 10
		for cuisine in e['cuisines']:
			if cuisine.lower() in [e['S'].lower() for e in response['preferences']['M']['top_cuisines']['L']]:
				e['weight'] += 10

	ingredient_weights = [e['weight'] for e in ingredients]
	ingredient_weights = [e/sum(ingredient_weights) for e in ingredient_weights]
	ret_ingredients = [{'name':e['name'], 'image':e['img'], 'discover':False, 'ideas':False, 'category':'Ingredient'} for e in ingredients]

	discover = np.random.choice(ret_ingredients, size=6, p=ingredient_weights).tolist()
	for e in discover:
		e['discover'] = True
	ideas = random.sample(discover, 3)
	for e in ideas:
		e['ideas'] = True


	dishes = options['dishes']
	dishes = [a for a in dishes if diet_dict[a['diet'].lower()] <= diet_dict[response['preferences']['M']['diet']['S'].lower()]]
	for e in dishes:
		e['weight'] = 1
		if e['cuisine'].lower() in [e['S'].lower() for e in response['preferences']['M']['top_cuisines']['L']]: 
			e['weight'] += 10

	dish_weights = [e['weight'] for e in dishes]
	dish_weights = [e/sum(dish_weights) for e in dish_weights]
	ret_dishes = [{'name':e['name'], 'image':e['img'], 'discover':False, 'ideas':False, 'category':'Dish'} for e in dishes]
	discover = np.random.choice(ret_dishes, size=6, p=dish_weights).tolist()
	for e in discover:
		e['discover'] = True
	ideas = random.sample(discover, 3)
	for e in ideas:
		e['ideas'] = True

	cuisines = options['cuisines']
	ret_cuisines = [{'name':e['name'], 'image':e['img'], 'discover':False, 'ideas':False, 'category':'Cuisine'} for e in cuisines]
	discover = random.sample(ret_cuisines, 6)
	for e in discover:
		e['discover'] = True
	ideas = random.sample(discover, 3)
	for e in ideas:
		e['ideas'] = True
	
	ret['data']['timestamp'] = int(time.time())
	ret['data']['items'] = ret_ingredients + ret_dishes + ret_cuisines
	return ret

