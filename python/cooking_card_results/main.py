import boto3
import json
import time


def event_handler(event, context):

# def test():
	# now = time.time()
	# s3 = boto3.client('s3')
	# data = s3.get_object(Bucket='yummly-recipes', Key='all_yummly.json')
	# data = data['Body'].read().decode('utf-8')

	# data = json.loads(data)

	# print(len(data)) {"user_id":	"17ef5c4b-3ac9-4548-a309-41e30a61c6e8", "query": {"query_type": "ingredient", "query_body": "Chicken"}}
	# print(f"Time for execution: {time.time()- now}")
	sample_data = {
		'category': "ingredient",
		'title': "Your results for",
		'item': "Chicken",
		'subtitle': "Created for 3:20pm",
		'results':[
			{
				'title': "Chinese Chicken and Broccoli",
				'id': "86ad1f34-5551-46d6-a96d-e0dd721933eb",
				'rating': "91% liked",
				'cook_time': "30 min",
				'difficulty': "Intermediate",
				'image_url': "https://yummly-images.s3-us-west-1.amazonaws.com/img10591.jpg",
				'ingredients': [
					"2 boneless, skinless chicken breasts, cut into bite-sized pieces",
					"1 large head of broccoli, crowns only, cut into bite-sized pieces",
					"1 tablespoon vegetable oil",
					"2 tablespoons vegetable oil",
					"1 tablespoon water",
					"1/2 teaspoon baking soda",
					"1 teaspoon sugar",
					"2 teaspoons cornstarch",
					"1 tablespoon reduced-sodium soy sauce",
					"1/4 cup + 1 tablespoon reduced-sodium soy sauce",
					"2 tablespoons brown sugar",
					"4 cloves garlic, minced",
					"2 tablespoons flour",
					"1 tablespoon rice vinegar",
					"1 tablespoon vegetable oil",
					"2 tablespoons water"
				],
				'link': "http://www.simplywhisked.com/chinese-chicken-and-broccoli/"
			},
			{
				'title': "Chinese Chicken and Broccoli",
				'id': "86ad1f34-5551-46d6-a96d-e0dd721933eb",
				'rating': "91% liked",
				'cook_time': "30 min",
				'difficulty': "Intermediate",
				'image_url': "https://yummly-images.s3-us-west-1.amazonaws.com/img10591.jpg",
				'ingredients': [
					"2 boneless, skinless chicken breasts, cut into bite-sized pieces",
					"1 large head of broccoli, crowns only, cut into bite-sized pieces",
					"1 tablespoon vegetable oil",
					"2 tablespoons vegetable oil",
					"1 tablespoon water",
					"1/2 teaspoon baking soda",
					"1 teaspoon sugar",
					"2 teaspoons cornstarch",
					"1 tablespoon reduced-sodium soy sauce",
					"1/4 cup + 1 tablespoon reduced-sodium soy sauce",
					"2 tablespoons brown sugar",
					"4 cloves garlic, minced",
					"2 tablespoons flour",
					"1 tablespoon rice vinegar",
					"1 tablespoon vegetable oil",
					"2 tablespoons water"
				],
				'link': "http://www.simplywhisked.com/chinese-chicken-and-broccoli/"
			},
			{
				'title': "Chinese Chicken and Broccoli",
				'id': "86ad1f34-5551-46d6-a96d-e0dd721933eb",
				'rating': "91% liked",
				'cook_time': "30 min",
				'difficulty': "Intermediate",
				'image_url': "https://yummly-images.s3-us-west-1.amazonaws.com/img10591.jpg",
				'ingredients': [
					"2 boneless, skinless chicken breasts, cut into bite-sized pieces",
					"1 large head of broccoli, crowns only, cut into bite-sized pieces",
					"1 tablespoon vegetable oil",
					"2 tablespoons vegetable oil",
					"1 tablespoon water",
					"1/2 teaspoon baking soda",
					"1 teaspoon sugar",
					"2 teaspoons cornstarch",
					"1 tablespoon reduced-sodium soy sauce",
					"1/4 cup + 1 tablespoon reduced-sodium soy sauce",
					"2 tablespoons brown sugar",
					"4 cloves garlic, minced",
					"2 tablespoons flour",
					"1 tablespoon rice vinegar",
					"1 tablespoon vegetable oil",
					"2 tablespoons water"
				],
				'link': "http://www.simplywhisked.com/chinese-chicken-and-broccoli/"
			},
		]
	}

	return json.loads(json.dumps(sample_data))