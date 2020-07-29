import os, json, boto3

def event_handler(event, context):

	name_to_kw = {'Diet': 'diet', 'Cooking level':'cooking_level', 'Time for lunch':'max_time_lunch', 'Time for dinner':'max_time_dinner', 'Spice tolerance':'spice_tolerance', 'Top cuisines':'top_cuisines', 'Disliked foods': 'disliked_foods'}
# def test(event):
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('iris_users')

	if 'user_id' in event.keys():
		user_id = event['user_id']
	elif 'body' in event.keys():
		user_id = json.loads(event['body'])['user_id']
	else:
		user_id = '17ef5c4b-3ac9-4548-a309-41e30a61c6e8'

	field = name_to_kw[event['preference']['title']]
	if event['preference']['type'] == 'single_select':
		new_info = event['preference']['items'][0]['title']
	else:
		new_info = [e['title'] for e in event['preference']['items']]

	try:
		table.update_item(
			Key = {
				'user_id': user_id
			},
			UpdateExpression="set preferences.#val=:v",
			ExpressionAttributeNames={
				'#val': field
			},
			ExpressionAttributeValues={
				':v': new_info
			})
	except Exception as e:
		print(e)

	return True