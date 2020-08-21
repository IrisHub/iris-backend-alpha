# import json, os
# from scipy import stats

# with open('all_yummly.json', 'r+') as f:
# 	data = json.load(f)

# 	keep = []
# 	for e in data:
# 		if len(e['ingredientLines']) <= 12:
# 			keep.append(e)


# 	times = [e['totalTimeInSeconds'] for e in keep]
# 	steps = [len(e['ingredientLines']) for e in keep]

# 	def difficulty_function(e):
# 		time_percentile = stats.percentileofscore(times, e['totalTimeInSeconds'])
# 		steps_percentile = stats.percentileofscore(steps, len(e['ingredientLines']))
# 		difficulty = 0.5*time_percentile + 0.5*steps_percentile
# 		if difficulty < 37:
# 			return "Beginner"
# 		elif difficulty < 63:
# 			return "Intermediate"
# 		else:
# 			return "Advanced"
# 	for e in keep:
# 		e['difficulty'] = difficulty_function(e)

# 	f.seek(0)
# 	f.write(json.dumps(keep, indent=4))
# 	f.truncate()