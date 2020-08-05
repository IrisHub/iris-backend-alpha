import os, json
import boto3
import boto3.dynamodb.types
from botocore.exceptions import ClientError

diets = ['No preference', 'Vegetarian', 'Vegan', 'Pescatarian']
cooking_level = ['Beginner', 'Intermediate', 'Advanced']
disliked_foods = ['Almonds', 'Apple', 'Avocado', 'Bacon', 'Banana', 'Beans', 'Beef', 'Bell Pepper', 'Blueberries', 'Bok Choy', 'Bread', 'Brie', 'Broccoli', 'Cabbage', 'Carrots', 'Cauliflower', 'Cheddar', 'Cheese', 'Cherry', 'Chia Seeds', 'Chicken Breasts', 'Chicken Legs', 'Chicken Stock', 'Chicken Thighs', 'Chicken Wings', 'Chickpea', 'Chocolate', 'Cod', 'Collard Greens', 'Corn', 'Couscous', 'Cucumber', 'Edamame', 'Egg Whites', 'Eggs', 'English Muffin', 'Fettuccine', 'Fish', 'Fish Sauce', 'Five Spice', 'Flour', 'Flour Tortillas', 'Fruit', 'Fresh Herbs', 'Fresh Mint', 'Garlic', 'Garlic Salt', 'Ginger', 'Goat Cheese', 'Granola', 'Greek Yogurt', 'Green Beans', 'Grapes', 'Ground Beef', 'Ground Turkey', 'Guacamole', 'Ham', 'Hoisin Sauce', 'Jasmine Rice', 'Kale', 'Lemon', 'Lettuce', 'Lime', 'Linguine', 'Mango', 'Meat', 'Milk', 'Mushroom', 'Oat Milk', 'Okra', 'Olive Oil', 'Olive', 'Onion', 'Oyster Sauce', 'Paneer', 'Parmesan', 'Pasta', 'Peach', 'Peanut Butter', 'Peas', 'Peppers', 'Pesto', 'Pork', 'Pork Belly', 'Pork Chop', 'Potato', 'Quinoa', 'Ramen', 'Rice', 'Rice Milk', 'Rice Noodles', 'Salmon', 'Sausage', 'Scallops', 'Sesame Oil', 'Sesame Seeds', 'Shallot', 'Soy Milk', 'Protein Powder', 'Soy Sauce', 'Spaghetti', 'Spinach', 'Squash', 'Sriracha', 'Strawberries', 'Sweet Potato', 'Teriyaki Sauce', 'Thai Basil', 'Tofu', 'Tomato', 'Tortilla', 'Tuna', 'Turkey', 'Vanilla', 'Vegan Cheese', 'Vegan Chocolate Chips', 'Vegetable Broth', 'Vegetarian Bacon', 'Walnuts', 'Whipping Cream', 'Yeast', 'Yogurt', 'Zucchini', 'Farro', 'Lentils', 'Cashews', 'Hazelnuts', 'Pistachios', 'Coconut Milk', 'Almond Milk', 'Cereal', 'Vegetables', 'Orzo', 'Yam', 'Eggplant', 'Noodles', 'Shellfish', 'Butter', 'Green Onion', 'Basil', 'Seafood', 'Shrimp', 'Crab', 'Lobster', 'Mussel', 'Scallops', 'Cilantro']
cuisines = ['American', 'Chinese', 'French', 'Indian', 'Italian', 'Mexican', 'Southwestern', 'Thai', 'Asian']
max_time_lunch = ["Under 30 minutes", "Under 45 minutes", "Under 1 hour"]
max_time_dinner = ["Under 30 minutes", "Under 45 minutes", "Under 1 hour"]
common_ingredients = ['Avocado', 'Bacon', 'Beans', 'Beef', 'Bell pepper', 'Bok choy', 'Bread', 'Broccoli', 'Cabbage', 'Carrots', 'Cauliflower', 'Cheddar', 'Cheese', 'Chicken breast', 'Chicken stock', 'Chicken thigh', 'Cod', 'Corn', 'Cucumber', 'Eggs', 'Fish', 'Fish sauce', 'Flour', 'Flour tortillas', 'Fruit', 'Goat cheese', 'Green beans', 'Ground beef', 'Ground turkey', 'Ham', 'Jasmine rice', 'Kale', 'Lettuce', 'Linguine', 'Meat', 'Milk', 'Mushrooms', 'Olive', 'Oyster sauce', 'Parmesan', 'Pasta', 'Peas', 'Peppers', 'Pesto', 'Pork', 'Potato', 'Quinoa', 'Rice', 'Rice noodles', 'Salmon', 'Sausage', 'Scallops', 'Soy sauce', 'Spaghetti', 'Spinach', 'Squash', 'Sweet potato', 'Tofu', 'Tomato', 'Tortilla', 'Turkey', 'Vegetable broth', 'Yogurt', 'Zucchini', 'Cashews', 'Coconut milk', 'Vegetables', 'Yam', 'Eggplant', 'Noodles', 'Green onion', 'Shrimp']

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
		'items': [{'name': e, 'selected': True if e.lower() == response['preferences']['M']['diet']['S'].lower() else False}for e in diets]
	}
	preferences[1] = {
		'title': 'Cooking level',
		'type': 'single_select',
		'items': [{'name': e, 'selected': True if e.lower() == response['preferences']['M']['cooking_level']['S'].lower() else False}for e in cooking_level]
	}
	preferences[2] = {
		'title': 'Time for lunch',
		'type': 'single_select',
		'items': [{'name': e, 'selected': True if e.lower() == response['preferences']['M']['max_time_lunch']['S'].lower() else False}for e in max_time_lunch]
	}
	preferences[3] = {
		'title': 'Time for dinner',
		'type': 'single_select',
		'items': [{'name': e, 'selected': True if e.lower() == response['preferences']['M']['max_time_dinner']['S'].lower() else False}for e in max_time_dinner]
	}
	preferences[4] = {
		'title': 'Common ingredients',
		'type': 'multi_select',
		'items': [{'name': e, 'selected': True if e.lower() in [e['S'].lower() for e in response['preferences']['M']['ingredients']['L']] else False}for e in common_ingredients]
	}
	preferences[5] = {
		'title': 'Top cuisines',
		'type': 'multi_select',
		'items': [{'name': e, 'selected': True if e.lower() in [e['S'].lower() for e in response['preferences']['M']['top_cuisines']['L']] else False}for e in cuisines]
	}
	preferences[6] = {
		'title': 'Disliked foods',
		'type': 'multi_select',
		'items': [{'name': e, 'selected': True if e.lower() in [e['S'].lower() for e in response['preferences']['M']['disliked_foods']['L']] else False}for e in disliked_foods]
	}

	print({'etching': etching, 'user_number': user_number, 'preferences':preferences})
	return json.loads(json.dumps({'etching': etching, 'user_number': user_number, 'preferences':preferences}))
