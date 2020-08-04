import os, json, boto3
from boto3.dynamodb.conditions import Key


users = {'iris20':'17ef5c4b-3ac9-4548-a309-41e30a61c6e8', #Kanyes's Token/ID
}
def event_handler(event, context):
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('iris_users')

	print(event)
	if 'access_code' in event.keys():
		token = event['access_code'].upper()
	elif 'body' in event.keys():
		token = json.loads(event['body'])['access_code'].upper()

	print(f"Token: {token}")
	try:
		response = table.query(IndexName='token-index', KeyConditionExpression=Key('token').eq(token))
		response = response["Items"][0]
	except Exception as e:
		return {"error":"Invalid token"}


	name = response['name'].split(' ')[0]
	preferences = response['preferences']
	diet = preferences['diet']
	cooking_level = preferences['cooking_level']
	favorite_ingredients = ', '.join([e for e in preferences['ingredients']])
	disliked_foods = ', '.join([e for e in preferences['disliked_foods']])
	max_time_dinner = preferences['max_time_dinner']
	max_time_lunch = preferences['max_time_lunch']
	top_cuisines = ', '.join([e for e in preferences['top_cuisines']])

	ret = {}
	ret['user_id'] = response['user_id']
	ret['text'] = [
		f"Hello, {name}",
		f"Iris is loading your preferences into the app",
		f"Diet: {diet}",
		f"{cooking_level} chef",
		f"{max_time_lunch} for lunch",
		f"{max_time_dinner} for dinner",
		f"Common ingredients are {favorite_ingredients}" if favorite_ingredients else f"No common ingredients yet",
		f"Favorite cuisines are {top_cuisines}" if top_cuisines else f"No favorite cuisines yet",
		f"Dislikes {disliked_foods}" if disliked_foods else f"No dislike foods yet",
	]

	return ret

