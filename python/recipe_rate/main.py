import boto3

def event_handler(event, context):
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('iris_users')

	if 'user_id' in event.keys():
		user_id = event['user_id']
		recipe_id = event['recipe_id']
	elif 'body' in event.keys():
		user_id = json.loads(event['body'])['user_id']
		recipe_id = json.loads(event['body'])['recipe_id']

	field='disliked_recipes'
	try:
		table.update_item(
			Key = {
				'user_id': user_id
			},
			UpdateExpression="set disliked_recipes = list_append(disliked_recipes, :v)",
			ExpressionAttributeValues={
				':v': [recipe_id]
			})
	except Exception as e:
		print(e)