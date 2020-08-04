import json

dish_str = """Katsu
Sushi
Crepes
Pancakes
Udon
Bowls
Shakshuka
Ropa Vieja
Kefta
Pad thai
Lasagna
Fried Rice
Yakisoba
Burritos
Hummus
Toasts
kebabs
Croque Madame
Dumplings
Ravioli
Jambalaya
Tortellini
Teriyaki
Granola
Hamburgers
Tamales
Guacamole
Empanadas
tzatziki
Miso soup
Smoothies
Salads
couscous
Drunken noodles
Huevos Rancheros
Daal
pizza
Omelettes
Soba
Souvlaki
Tempura
Chicken Curry
Croque Monsieur
Fettuccine
Ratatouille
Waffles
Ramen
Sandwiches
Quesadillas
Eggs
Tikka Masala
Noodles
Risotto
Quiches
Soups
Cuban sandwich
Chow mein
Chorizo
tortillas
Cuban Pork
Wontons
Gyoza
Yakitori
Gyros
Grilled cheese
French Toast
Tacos"""


dish_cuisines = """Japanese
Japanese
French
American
Japanese
American
Middle Eastern
Cuban
moroccan
Thai
Italian
Asian
Japanese
Mexican
mediterranean
American
mediterranean
French
Chinese
Italian
Southern
Italian
Japanese
American
American
mexican
Mexican
Mexican
Greek
Chinese
American
American
mediterranean
Thai
southwestern
Indian
mediterranean
American
Japanese
Greek
Japanese
Indian
French
Italian
French
American
Japanese
American
Mexican
American
Indian
Chinese
Italian
French
American
Cuban
Chinese
southwestern
southwestern
Cuban
Chinese
Japanese
Japanese
Greek
American
American
Mexican"""

dish_images = """https://images.unsplash.com/photo-1569050467447-ce54b3bbc37d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2735&q=80
https://images.unsplash.com/photo-1579871494447-9811cf80d66c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1515467837915-15c4777ba46a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2853&q=80
https://images.unsplash.com/photo-1541288097308-7b8e3f58c4c6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1558985212-324add95595a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2624&q=80
https://images.unsplash.com/photo-1533244769204-d345e73a30c1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1890&q=80
https://images.unsplash.com/photo-1590412200988-a436970781fa?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=975&q=80
https://live.staticflickr.com/7338/9419809373_b929016e21_b.jpg
https://images.unsplash.com/photo-1520218508822-998633d997e6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80
https://images.unsplash.com/photo-1559314809-0d155014e29e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1581904243918-7aac00cefed2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=933&q=80
https://images.unsplash.com/photo-1584269600464-37b1b58a9fe7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2851&q=80
https://images.unsplash.com/photo-1512398975429-6ec18e1f3eb4?ixlib=rb-1.2.1&auto=format&fit=crop&w=934&q=80
https://images.unsplash.com/photo-1566740933430-b5e70b06d2d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80
https://images.unsplash.com/photo-1591299177061-2151e53fcaea?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1825&q=80
https://images.unsplash.com/photo-1525351484163-7529414344d8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1400&q=80
https://images.unsplash.com/photo-1559551082-3d2a032a03e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2852&q=80
https://images.unsplash.com/photo-1531664412848-9610afed156c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1563245372-f21724e3856d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2858&q=80
https://images.unsplash.com/photo-1587740908075-9e245070dfaa?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDAxNX0&auto=format&fit=crop&w=975&q=80
https://live.staticflickr.com/3013/2799144481_1f7cae30dc_b.jpg
https://images.unsplash.com/photo-1484325881845-65073528922e?ixlib=rb-1.2.1&auto=format&fit=crop&w=2100&q=80
https://images.unsplash.com/photo-1516684465974-78661ba8165d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80
https://images.unsplash.com/photo-1526893628193-76477eb4bc8f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2852&q=80
https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2803&q=80
https://images.unsplash.com/photo-1587569906338-f79d500d7122?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1867&q=80
https://images.unsplash.com/photo-1523634700860-90d0ef74f137?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2725&q=80
https://images.unsplash.com/photo-1548228586-171fb0887ac0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1870&q=80
https://images.unsplash.com/photo-1591120583691-49d2741e55da?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2776&q=80
https://images.unsplash.com/photo-1454334281609-87a89762912c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2732&q=80
https://images.unsplash.com/photo-1532301791573-4e6ce86a085f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1578687388049-079580e6eb2d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80
https://images.unsplash.com/photo-1519996409144-56c88c9aa612?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80
https://images.unsplash.com/photo-1537081956137-3931105e2d37?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2800&q=80
https://images.unsplash.com/photo-1585975754487-25489eabf36a?ixlib=rb-1.2.1&auto=format&fit=crop&w=934&q=80
https://images.unsplash.com/photo-1546833999-b9f581a1996d?ixlib=rb-1.2.1&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2814&q=80
https://images.unsplash.com/photo-1494597706938-de2cd7341979?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2760&q=80
https://images.unsplash.com/photo-1496114212242-bac8bd9de53d?ixlib=rb-1.2.1&auto=format&fit=crop&w=934&q=80
https://images.unsplash.com/photo-1573126161855-f9633aa8a9f0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1867&q=80
https://images.unsplash.com/photo-1593357871477-00fd350cc0f8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80
https://images.unsplash.com/photo-1588166524941-3bf61a9c41db?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=931&q=80
https://images.unsplash.com/photo-1574896265656-975846108510?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80
https://images.unsplash.com/photo-1551631759-96b8377f491c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1920&q=80
https://images.unsplash.com/photo-1572453800999-e8d2d1589b7c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1864&q=80
https://images.unsplash.com/photo-1591325418441-ff678baf78ef?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1867&q=80
https://images.unsplash.com/photo-1591325418441-ff678baf78ef?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1867&q=80
https://images.unsplash.com/photo-1540713434306-58505cf1b6fc?ixlib=rb-1.2.1&auto=format&fit=crop&w=2734&q=80
https://images.unsplash.com/photo-1573010288252-e958ff11effc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80
https://images.unsplash.com/photo-1582169505937-b9992bd01ed9?ixlib=rb-1.2.1&auto=format&fit=crop&w=1898&q=80
https://upload.wikimedia.org/wikipedia/commons/6/61/Homemade_chicken_tikka_masala.jpg
https://images.unsplash.com/photo-1551183053-bf91a1d81141?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2806&q=80
https://images.unsplash.com/photo-1461009683693-342af2f2d6ce?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2062&q=80
https://images.unsplash.com/photo-1490556278693-b666672547a1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80
https://images.unsplash.com/photo-1510431198580-7727c9fa1e3a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2734&q=80
https://images.unsplash.com/photo-1590076862697-0324a3938545?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1464500422302-6188776dcbf3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2842&q=80
https://images.unsplash.com/photo-1529241160658-a8a2a0d86620?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMjF9&auto=format&fit=crop&w=2100&q=80
https://images.unsplash.com/photo-1545505005-0a09f804dcf6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80
https://live.staticflickr.com/5055/5421409201_ef774e95e4_b.jpg
https://images.unsplash.com/photo-1559948271-7d5c98d2e951?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80
https://images.unsplash.com/photo-1588182728399-e8f2df121744?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1867&q=80
https://images.unsplash.com/photo-1563118946-9d60eae4a82d?ixlib=rb-1.2.1&auto=format&fit=crop&w=2100&q=80
https://images.unsplash.com/photo-1542706133547-2b957ec7ee5e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80
https://images.unsplash.com/photo-1528736235302-52922df5c122?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2844&q=80
https://images.unsplash.com/photo-1484723091739-30a097e8f929?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=987&q=80
https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80"""


dish_diets = """None
None
Vegetarian
Vegetarian
Vegetarian
Vegan
Vegetarian
None
None
Vegan
Vegan
Vegetarian
Vegan
Vegan
Vegan
Vegan
None
None
None
Vegetarian
None
Vegetarian
None
Vegan
None
None
Vegan
None
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Vegetarian
Vegan
Vegetarian
Vegetarian
Vegan
None
None
None
None
Vegetarian
Vegan
Vegan
None
Vegan
Vegetarian
Vegetarian
Vegan
Vegan
Vegan
Vegetarian
Vegan
None
Vegan
None
Vegan
None
Vegan
None
None
None
Vegetarian
Vegetarian
Vegan"""

dishes = dish_str.split('\n')
dish_cuisines = dish_cuisines.split('\n')
dish_images= dish_images.split('\n')
dish_diets = dish_diets.split('\n')


dishes = [{"name":e[0].title(), "cuisine":e[1].title(), "img":e[2], "diet":e[3].title()} for e in list(zip(dishes, dish_cuisines, dish_images, dish_diets))]

# print(json.dumps(dishes, indent=4))

cuisine_str = """American
Southern
Chinese
Cuban
French
German
Greek
Indian
Italian
Japanese
Mediterranean
Mexican
Moroccan
Portuguese
Southwestern
Spanish
Thai
European
Asian"""
cuisines = cuisine_str.split('\n')
cuisine_imgs = """https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2767&q=80
https://images.unsplash.com/photo-1522237825450-a0c44eecddb4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2848&q=80
https://images.unsplash.com/photo-1563245372-f21724e3856d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2858&q=80
https://live.staticflickr.com/2708/4351990762_a1d63b1b16_b.jpg
https://images.unsplash.com/photo-1571157577110-493b325fdd3d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2734&q=80
https://images.unsplash.com/photo-1568486504489-9e70d75313b8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80
https://images.unsplash.com/photo-1529006557810-274b9b2fc783?ixlib=rb-1.2.1&auto=format&fit=crop&w=2855&q=80
https://images.unsplash.com/photo-1565557623262-b51c2513a641?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2724&q=80
https://images.unsplash.com/photo-1555072956-7758afb20e8f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2734&q=80
https://images.unsplash.com/photo-1519077204685-ed90d0cc05b7?ixlib=rb-1.2.1&auto=format&fit=crop&w=2689&q=80
https://images.unsplash.com/photo-1565560665129-4831aa15206c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=975&q=80
https://images.unsplash.com/photo-1582234372722-50d7ccc30ebd?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2800&q=80
https://images.unsplash.com/photo-1517314597476-e1788060b6cb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=933&q=80
https://images.unsplash.com/photo-1591107576521-87091dc07797?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1586561945641-98a839abd3f7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80
https://images.unsplash.com/photo-1571167366136-b57e07761625?ixlib=rb-1.2.1&auto=format&fit=crop&w=2775&q=80
https://images.unsplash.com/photo-1562565651-7d4948f339eb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2689&q=80
https://images.unsplash.com/photo-1561668048-fe9c092832e0?ixlib=rb-1.2.1&auto=format&fit=crop&w=2102&q=80
https://images.unsplash.com/photo-1496116218417-1a781b1c416c?ixlib=rb-1.2.1&auto=format&fit=crop&w=2100&q=80"""
cuisine_imgs = cuisine_imgs.split('\n')

cuisines = [{"name":e[0].title(), "img":e[1], } for e in list(zip(cuisines, cuisine_imgs))]



ingredients = """almonds
apple
avocado
bacon
banana
beans
beef
bell pepper
blueberries
bok choy
bread
brie
broccoli
cabbage
carrots
cauliflower
cheddar
cheese
cherry
chia seeds
chicken breasts
chicken legs
chicken stock
chicken thighs
chicken wings
chickpea
chocolate
cod
collard greens
corn
couscous
cucumber
edamame
egg whites
eggs
english muffin
fettuccine
fish
fish sauce
five spice
flour
flour tortillas
fruit
fresh herbs
fresh mint
garlic
garlic salt
ginger
goat cheese
granola
greek yogurt
green beans
grapes
ground beef
ground turkey
guacamole
ham
hoisin sauce
jasmine rice
kale
lemon
lettuce
lime
linguine
mango
meat
milk
mushroom
Oat milk
okra
olive oil
olive
onion
oyster sauce
paneer
parmesan
pasta
peach
peanut butter
peas
peppers
pesto
pork
pork belly
pork chop
potato
quinoa
ramen
rice
rice milk
rice noodles
salmon
sausage
scallops
sesame oil
sesame seeds
shallot
soy milk
protein powder
soy sauce
spaghetti
spinach
squash
sriracha
strawberries
sweet potato
teriyaki sauce
thai basil
tofu
tomato
tortilla
tuna
turkey
vanilla
vegan cheese
vegan chocolate chips
vegetable broth
vegetarian bacon
walnuts
whipping cream
yeast
yogurt
zucchini
farro
lentils
cashews
hazelnuts
pistachios
coconut milk
almond milk
cereal
vegetables
orzo
yam
eggplant
noodles
shellfish
butter
green onion
basil
seafood
shrimp
crab
lobster
mussel
scallops
cilantro"""

ingredient_imgs= """https://images.unsplash.com/photo-1508061253366-f7da158b6d46?ixlib=rb-1.2.1&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1551445523-324a0fdab051?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2732&q=80
https://images.unsplash.com/photo-1557925922-dac32ff4429f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2671&q=80
https://images.unsplash.com/photo-1592086326871-f7cf2f1801ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2800&q=80
https://images.unsplash.com/photo-1580979443662-13a976bd7632?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2777&q=80
https://images.unsplash.com/photo-1556269923-e4ef51d69638?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2771&q=80
https://images.unsplash.com/photo-1587656221664-37e89ddebbf6?ixlib=rb-1.2.1&auto=format&fit=crop&w=975&q=80
https://images.unsplash.com/photo-1425934398893-310a009a77f9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1951&q=80
https://images.unsplash.com/photo-1585162535710-bb6a1bb0f1de?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1549931319-a545dcf3bc73?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1571046313732-cf3a7406c84c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80
https://images.unsplash.com/photo-1518164147695-36c13dd568f5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2800&q=80
https://images.unsplash.com/photo-1578208895671-29d47f61294e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2767&q=80
https://images.unsplash.com/photo-1590848791238-fb3596a2ba56?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1568584952634-e9bb8a163e28?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2852&q=80
https://unsplash.com/photos/n-QvF3vyf5M
https://images.unsplash.com/photo-1558221693-89a565d7ecd8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=975&q=80
https://images.unsplash.com/photo-1439127989242-c3749a012eac?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1490474504059-bf2db5ab2348?ixlib=rb-1.2.1&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1516684669134-de6f7c473a2a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2734&q=80
https://images.unsplash.com/photo-1517984055083-fd6e1e788e54?ixlib=rb-1.2.1&auto=format&fit=crop&w=2734&q=80
https://images.unsplash.com/photo-1554136512-5d996b22f5fa?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2800&q=80
https://images.unsplash.com/photo-1532550907401-a500c9a57435?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80
https://images.unsplash.com/photo-1566918214014-a3b3e0132267?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2800&q=80
https://images.unsplash.com/photo-1509401867-6a8e89483fdb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2000&q=80
https://images.unsplash.com/photo-1575377427642-087cf684f29d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2734&q=80
https://images.unsplash.com/photo-1579631542761-d7c4e913f8d4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2851&q=80
https://images.unsplash.com/photo-1559852925-6a5a7125525b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2000&q=80
https://images.unsplash.com/photo-1578652903016-b78571b87410?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2734&q=80
https://images.unsplash.com/photo-1582576163090-09d3b6f8a969?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2851&q=80
https://images.unsplash.com/photo-1589621316382-008455b857cd?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1575262599410-837a72005862?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2798&q=80
https://images.unsplash.com/photo-1562918005-50afb98e5d32?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2734&q=80
https://images.unsplash.com/photo-1509479100390-f83a8349e79c?ixlib=rb-1.2.1&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1565975925216-8bde89da915d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1971&q=80
https://images.unsplash.com/photo-1560177006-c5b5c3cfa75b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2767&q=80
https://images.unsplash.com/photo-1535461064904-2866de140568?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2734&q=80
https://images.unsplash.com/photo-1510808052173-32bd048cc8f3?ixlib=rb-1.2.1&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1591465001609-ded6360ecaab?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1565607052745-35f8c6ba59b1?ixlib=rb-1.2.1&auto=format&fit=crop&w=2721&q=80
https://images.unsplash.com/photo-1583898791652-5e8b960710bd?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1586999528871-ded77bc9656c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1001&q=80
https://images.unsplash.com/photo-1514733670139-4d87a1941d55?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2114&q=80
https://images.unsplash.com/photo-1582556135623-653b87486f21?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2795&q=80
https://images.unsplash.com/photo-1587049332298-1c42e83937a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2800&q=80
https://images.unsplash.com/photo-1518110925495-5fe2fda0442c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1589707790848-9097c28e8569?ixlib=rb-1.2.1&auto=format&fit=crop&w=2849&q=80
https://images.unsplash.com/photo-1559141234-794de31e3036?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2767&q=80
https://images.unsplash.com/photo-1578687595055-d15759a04151?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1562114808-b4b33cf60f4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2852&q=80
https://images.unsplash.com/photo-1558024083-31acc7b7b64a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2691&q=80
https://images.unsplash.com/photo-1580451359753-6f163ed6c244?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2775&q=80
https://images.unsplash.com/photo-1579366948929-444eb79881eb?ixlib=rb-1.2.1&auto=format&fit=crop&w=2800&q=80
https://images.pexels.com/photos/2757176/pexels-photo-2757176.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260
https://images.unsplash.com/photo-1593668220627-93c071ab0dfc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2853&q=80
https://images.unsplash.com/photo-1524438418049-ab2acb7aa48f?ixlib=rb-1.2.1&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1476224203421-9ac39bcb3327?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1522193582792-c66cf1cddd16?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1568569350062-ebfa3cb195df?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1515356956468-873dd257f911?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2395&q=80
https://images.unsplash.com/photo-1561024342-ddb9779e55fb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1984&q=80
https://images.unsplash.com/photo-1481931098730-318b6f776db0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2737&q=80
https://images.unsplash.com/photo-1582655299221-2b6bff351df0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2680&q=80
https://images.unsplash.com/photo-1555939594-58d7cb561ad1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2734&q=80
https://images.unsplash.com/photo-1517448931760-9bf4414148c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2734&q=80
https://images.unsplash.com/photo-1504545102780-26774c1bb073?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2765&q=80
https://images.unsplash.com/photo-1574343193689-93e01f51291e?ixlib=rb-1.2.1&auto=format&fit=crop&w=2731&q=80
https://images.unsplash.com/photo-1425543103986-22abb7d7e8d2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80
https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2848&q=80
https://images.unsplash.com/photo-1591122523233-22037c1dec9f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2734&q=80
https://images.unsplash.com/photo-1587049633312-d628ae50a8ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2800&q=80
https://images.unsplash.com/photo-1571936979636-c6c5e345fb73?ixlib=rb-1.2.1&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1589647363585-f4a7d3877b10?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2852&q=80
https://images.unsplash.com/photo-1587394214315-85d8f8d6bf5c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1546549032-9571cd6b27df?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2734&q=80
https://images.unsplash.com/photo-1532704868953-d85f24176d73?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80
https://images.unsplash.com/photo-1504388192519-fb4be897c4d0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2734&q=80
https://images.unsplash.com/photo-1503444786070-ab39340977f2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80
https://images.unsplash.com/photo-1577098093907-93abb87b29be?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2448&q=80
https://images.unsplash.com/photo-1473093295043-cdd812d0e601?ixlib=rb-1.2.1&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1560883389-3bd36d16d021?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80
https://images.unsplash.com/photo-1571067224158-622a54542fed?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2775&q=80
https://images.unsplash.com/photo-1432139555190-58524dae6a55?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2855&q=80
https://images.unsplash.com/photo-1508313880080-c4bef0730395?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2272&q=80
https://images.unsplash.com/photo-1586201375799-47cd24c3f595?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1569718212165-3a8278d5f624?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1400&q=80
https://images.unsplash.com/photo-1516684732162-798a0062be99?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2592&q=80
https://images.unsplash.com/photo-1594813593170-547b5eaf5bc9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2491&q=80
https://images.unsplash.com/photo-1569058242276-0bc3e078cf86?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1559058789-672da06263d8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2847&q=80
https://images.unsplash.com/photo-1585325701165-351af916e581?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2788&q=80
https://images.unsplash.com/photo-1580302498882-b5aa77f09b75?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1585009198949-c3ac58de8ef6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2775&q=80
https://images.unsplash.com/photo-1585009198949-c3ac58de8ef6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2775&q=80
https://images.unsplash.com/photo-1578907814239-d2654ba61616?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1555465083-a845797ef750?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80
https://images.unsplash.com/photo-1579722821273-0f6c7d44362f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2734&q=80
https://images.unsplash.com/photo-1582581720432-de83a98176ab?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1551892374-ecf8754cf8b0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2800&q=80
https://images.unsplash.com/photo-1574316071802-0d684efa7bf5?ixlib=rb-1.2.1&auto=format&fit=crop&w=2775&q=80
https://images.unsplash.com/photo-1591578954582-dc4a81447c6c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2767&q=80
https://images.unsplash.com/photo-1519420638722-a2a5749c32be?ixlib=rb-1.2.1&auto=format&fit=crop&w=2775&q=80
https://images.unsplash.com/photo-1518635017498-87f514b751ba?ixlib=rb-1.2.1&auto=format&fit=crop&w=2852&q=80
https://images.unsplash.com/photo-1576458634550-157c96efa950?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2734&q=80
https://images.unsplash.com/photo-1588166524938-1ee110d7dcef?ixlib=rb-1.2.1&auto=format&fit=crop&w=2734&q=80
https://images.unsplash.com/photo-1530632789071-8543f47edb34?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1588166524941-3bf61a9c41db?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2731&q=80
https://images.unsplash.com/photo-1546094096-0df4bcaaa337?ixlib=rb-1.2.1&auto=format&fit=crop&w=2852&q=80
https://images.unsplash.com/photo-1583898791652-5e8b960710bd?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1501595091296-3aa970afb3ff?ixlib=rb-1.2.1&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1501200291289-c5a76c232e5f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2781&q=80
https://images.unsplash.com/photo-1516829748982-fec83d87bff7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2853&q=80
https://images.unsplash.com/photo-1573810655264-8d1e50f1592d?ixlib=rb-1.2.1&auto=format&fit=crop&w=2690&q=80
https://images.unsplash.com/photo-1587678777691-3d0df519c046?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1512003867696-6d5ce6835040?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1528607929212-2636ec44253e?ixlib=rb-1.2.1&auto=format&fit=crop&w=2767&q=80
https://images.unsplash.com/photo-1542617664-d890823e695e?ixlib=rb-1.2.1&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1583507623011-5cc6ff99e11c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2384&q=80
https://images.unsplash.com/photo-1591374781716-ee4dd5616150?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80
https://images.unsplash.com/photo-1571212515416-fef01fc43637?ixlib=rb-1.2.1&auto=format&fit=crop&w=930&q=80
https://images.unsplash.com/photo-1580294672673-4fbda48428be?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80
https://live.staticflickr.com/7563/15798620250_2ddd4ca440_b.jpg
https://images.unsplash.com/photo-1542627501-cadbb5b43ad7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2441&q=80
https://images.unsplash.com/photo-1509912760195-4f6cfd8cce2c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80
https://images.unsplash.com/photo-1543208541-0961a29a8c3d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80
https://images.unsplash.com/photo-1502825751399-28baa9b81efe?ixlib=rb-1.2.1&auto=format&fit=crop&w=2250&q=80
https://images.unsplash.com/photo-1588413335367-e49d32c5b50b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2434&q=80
https://images.unsplash.com/photo-1525070389266-b9afb0eed846?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80
https://images.unsplash.com/photo-1506368197720-c242fdaa44dc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80
https://images.unsplash.com/photo-1557844352-761f2565b576?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80
https://live.staticflickr.com/2804/4182848803_211151c587_b.jpg
https://images.unsplash.com/photo-1584699006710-3ad3b82fce7f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80
https://images.unsplash.com/photo-1528825950832-560a4a11473a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2200&q=80
https://images.unsplash.com/photo-1552611052-33e04de081de?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1300&q=80
https://images.unsplash.com/photo-1534080564583-6be75777b70a?ixlib=rb-1.2.1&auto=format&fit=crop&w=2250&q=80
https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80
https://images.unsplash.com/photo-1533802150735-4893270fc771?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80
https://images.unsplash.com/photo-1527964105263-1ac6265a569f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80
https://images.unsplash.com/photo-1539586345401-51d5bfba7ac0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80
https://images.unsplash.com/photo-1568254500745-c879851c30fe?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80
https://images.unsplash.com/photo-1511543865714-5a5a5ce51a94?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2500&q=80
https://images.unsplash.com/photo-1590759668628-05b0fc34bb70?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80
https://images.unsplash.com/photo-1516687773447-14c58c40816e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2252&q=80
https://images.unsplash.com/photo-1575506142613-499224781394?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1758&q=80
https://images.unsplash.com/photo-1535189487909-a262ad10c165?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1978&q=80"""

ingredient_diets = """Vegan
Vegan
Vegan
None
Vegan
Vegan
None
Vegan
Vegan
Vegan
Vegan
Vegetarian
Vegan
Vegan
Vegan
Vegan
Vegetarian
Vegetarian
Vegan
Vegan
None
None
None
None
None
Vegan
Vegetarian
Pescatarian
Vegan
Vegan
Vegan
Vegan
Vegan
Vegetarian
Vegetarian
Vegetarian
Vegan
Pescatarian
Pescatarian
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Vegetarian
Vegan
Vegetarian
Vegan
Vegan
None
None
Vegan
None
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
None
Vegetairan
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Pescatarian
Vegetarian
Vegetarian
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
None
None
None
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Pescatarian
None
Pescatarian
Vegan
Vegan
Vegan
Vegan
Vegetarian
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Vegetarian
Vegan
Vegan
Vegan
Vegan
Pescatarian
None
Vegan
Vegan
Vegan
Vegan
Vegetarian
Vegan
Vegetarian
Vegan
Vegetarian
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Vegan
Pescatarian
Vegetarian
Vegan
Vegan
Pescatarian
Pescatarian
Pescatarian
Pescatarian
Pescatarian
Pescatarian
Vegan"""

ingredient_cuisines = """None
None
Mexican,Southwestern
None
None
None
None
None
None
Asian,Chinese,Japanese,Thai
None
French
Asian,Chinese,Japanese,Thai
None
None
Indian
American
None
None
None
None
None
None
None
None
Indian
None
None
American
Mexican,Southwestern
Moroccan,Mediterranean
None
None
None
None
None
Italian
None
Asian,Chinese,Japanese,Thai
Chinese
None
Mexican,Southwestern
None
None
None
None
None
Indian,Asian,Chinese,Japanese,Thai
None
None
None
None
None
None
None
Mexican,Southwestern
None
Asian,Chinese,Japanese,Thai
Indian,Asian,Chinese,Japanese,Thai
None
None
None
None
Italian
None
None
None
None
None
None
None
Mediterranean
None
Asian,Chinese,Japanese,Thai
Indian
Italian
Italian
None
None
None
None
Italian
None
None
None
None
None
Asian,Japanese
None
None
Asian,Chinese,Japanese,Thai
None
None
None
Asian,Chinese,Japanese,Thai
Indian,Asian,Chinese,Japanese,Thai
None
None
None
Asian,Chinese,Japanese,Thai
Italian
None
None
Indian,Asian,Chinese,Japanese,Thai
None
None
Asian,Chinese,Japanese,Thai
Asian,Chinese,Japanese,Thai
Asian,Chinese,Japanese,Thai
None
Mexican,Southwestern
None
None
None
None
None
None
None
None
None
None
None
None
Italian
Indian
None
None
None
Thai
None
None
None
Italian
None
None
Asian,Chinese,Japanese,Thai
None
None
None
Italian,Thai
None
None
None
None
None
None
None"""

ingredients = ingredients.split('\n')
ingredient_imgs = ingredient_imgs.split('\n')
ingredient_cuisines = ingredient_cuisines.split('\n')
ingredient_cuisines = [e.split(',') for e in ingredient_cuisines]
ingredient_diets = ingredient_diets.split('\n')

ingredients = [{"name":e[0].title(), "img":e[1], "cuisines":[a.title() for a in e[2]], "diet": e[3].title()} for e in list(zip(ingredients, ingredient_imgs, ingredient_cuisines, ingredient_diets))]

data = {'ingredients':ingredients, 'dishes':dishes, 'cuisines':cuisines}

with open('info.json', 'r+') as f:
	f.seek(0)
	f.write(json.dumps(json.loads(json.dumps(data)), indent=4))
	f.truncate()