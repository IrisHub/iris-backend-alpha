import os, json
import boto3
import boto3.dynamodb.types
from botocore.exceptions import ClientError

diets = ['No preference', 'Vegetarian', 'Vegan', 'Pescatarian']
cooking_level = ['Beginner', 'Intermediate', 'Advanced']
disliked_foods = ['Almonds', 'Apple', 'Asfoetida', 'Avocado', 'Bacon', 'Banana', 'Basmati Rice', 'Bay Leaves', 'Beans', 'Beef', 'Bell Pepper', 'Blueberries', 'Bok Choy', 'Bread', 'Brie', 'Broccoli', 'Cabbage', 'Cardamom', 'Carrots', 'Cauliflower', 'Cheddar', 'Cheese', 'Cherry', 'Chia Seeds', 'Chicken Breasts', 'Chicken Legs', 'Chicken Stock', 'Chicken Thighs', 'Chicken Wings', 'Chickpea', 'Chocolate', 'Cilantro', 'Cod', 'Collard Greens', 'Cookies', 'Corn', 'Couscous', 'Cream Cheese', 'Cucumber', 'Edamame', 'Egg Whites', 'Eggs', 'English Muffin', 'Fennel', 'Fenugreek Leaf', 'Fettuccine', 'Fish', 'Fish Sauce', 'Five Spice', 'Flour', 'Flour Tortillas', 'Fresh Fruit', 'Fresh Herbs', 'Fresh Mint', 'Frozen Spinach', 'Garlic', 'Garlic Powder', 'Garlic Salt', 'Ginger', 'Goat Cheese', 'Granola', 'Greek Yogurt', 'Green Beans', 'Grapes', 'Ground Beef', 'Ground Pork', 'Ground Turkey', 'Guacamole', 'Ham', 'Hoisin Sauce', 'Jasmine Rice', 'Kale', 'Kosher Salt', 'Lemon', 'Lettuce', 'Lime', 'Linguine', 'Mango', 'Marinara Sauce', 'Meat', 'Milk', 'Mushroom', 'Oat Milk', 'Okra', 'Olive Oil', 'Olives', 'Onions', 'Oregano', 'Oyster Sauce', 'Paneer', 'Parmesan', 'Pasta', 'Pasta Sauce', 'Peach', 'Peanut Butter', 'Peas', 'Peppers', 'Pesto', 'Pork', 'Pork Belly', 'Pork Chops', 'Potatoes', 'Quinoa', 'Ramen Noodles', 'Rice', 'Rice Milk', 'Rice Noodles', 'Rosemary', 'Salmon', 'Sausage', 'Sea Scallops', 'Sesame Oil', 'Sesame Seeds', 'Shallot', 'Soy Milk', 'Soy Protein Powder', 'Soy Sauce', 'Spaghetti', 'Spinach', 'Squash', 'Sriracha Sauce', 'Strawberries', 'Sweet Potato', 'Taco Shells', 'Teriyaki Sauce', 'Thai Basil', 'Tofu', 'Tomatoes', 'Tortilla', 'Tumeric', 'Tuna', 'Turkey', 'Vanilla', 'Vegan Cheese', 'Vegan Chocolate Chips', 'Vegetable Broth', 'Vegetarian Bacon', 'Walnuts', 'Whipping Cream', 'Yeast', 'Yogurt']
cuisines = ['American', 'Southern', 'Chinese', 'Cuban', 'French', 'German', 'Greek', 'Hungarian', 'Indian', 'Italian', 'Japanese', 'Mediterrean', 'Mexican', 'Moroccan', 'Portuguese', 'Southwestern', 'Spanish', 'Thai', 'European', 'Asian']
max_time_lunch = ["Under 30 minutes", "Under 45 minutes", "Under 1 hour"]
max_time_dinner = ["Under 30 minutes", "Under 45 minutes", "Under 1 hour"]
spice_tolerance = ["Low", "Medium", "High"]


def event_handler(event, context):
	print("Event:")
	print(json.dumps(event))
	if 'user_id' in event.keys():
		user_id = event['user_id']
	elif 'body' in event.keys():
		user_id = json.loads(event['body'])['user_id']
	else:
		user_id = '17ef5c4b-3ac9-4548-a309-41e30a61c6e8'

	print(user_id)

	dynamodb = boto3.client('dynamodb')

	# dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
	# table = dynamodb.Table('iris_users')

	try:
		response = dynamodb.get_item(TableName='iris_users', Key={"user_id":{"S":str(user_id)}})
		print("Response:")
		print(json.dumps(response))
		response = response["Item"]
	except ClientError as e:
		print(e.response['Error']['Message'])
	

	etching = "Created for you"
	user_number = f"User #{response['user_number']['N']}"
	preferences = [None] * 7
	preferences[0] = {
		'title': 'Diet',
		'type': 'single_select',
		'items': [{'name': e, 'selected': True if e == response['preferences']['M']['diet']['S'] else False}for e in diets]
	}
	preferences[1] = {
		'title': 'Cooking Level',
		'type': 'single_select',
		'items': [{'name': e, 'selected': True if e == response['preferences']['M']['cooking_level']['S'] else False}for e in cooking_level]
	}
	preferences[2] = {
		'title': 'Time for lunch',
		'type': 'single_select',
		'items': [{'name': e, 'selected': True if e == response['preferences']['M']['max_time_lunch']['S'] else False}for e in max_time_lunch]
	}
	preferences[3] = {
		'title': 'Time for dinner',
		'type': 'single_select',
		'items': [{'name': e, 'selected': True if e == response['preferences']['M']['max_time_dinner']['S'] else False}for e in max_time_dinner]
	}
	preferences[4] = {
		'title': 'Spice tolerance',
		'type': 'single_select',
		'items': [{'name': e, 'selected': True if e == response['preferences']['M']['spice_tolerance']['S'] else False}for e in spice_tolerance]
	}
	preferences[5] = {
		'title': 'Top cuisines',
		'type': 'multi_select',
		'items': [{'name': e, 'selected': True if e in [e['S'] for e in response['preferences']['M']['top_cuisines']['L']] else False}for e in cuisines]
	}
	preferences[6] = {
		'title': 'Disliked foods',
		'type': 'multi_select',
		'items': [{'name': e, 'selected': True if e in [e['S'] for e in response['preferences']['M']['disliked_foods']['L']] else False}for e in disliked_foods]
	}

	print({'etching': etching, 'user_number': user_number, 'preferences':preferences})
	return json.loads(json.dumps({'etching': etching, 'user_number': user_number, 'preferences':preferences}))
