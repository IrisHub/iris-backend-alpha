import json, os, time, random

def event_handler(event, context):
	options = json.load(open('info.json', 'r+'))
	ret = {}
	ret['title'] = "Lunch under 30min"
	ret['subtitle'] = "For you"
	ret['data'] = {}
	ingredients = options['ingredients']
	ret_ingredients = [{'name':e['name'], 'image':e['img'], 'discover':False, 'ideas':False, 'category':'ingredient'} for e in ingredients]
	discover = random.sample(ret_ingredients, 6)
	for e in discover:
		e['discover'] = True
	ideas = random.sample(discover, 3)
	for e in ideas:
		e['ideas'] = True
	dishes = options['dishes']
	ret_dishes = [{'name':e['name'], 'image':e['img'], 'discover':False, 'ideas':False, 'category':'dish'} for e in dishes]
	discover = random.sample(ret_dishes, 6)
	for e in discover:
		e['discover'] = True
	ideas = random.sample(discover, 3)
	for e in ideas:
		e['ideas'] = True
	cuisines = options['cuisines']
	ret_cuisines = [{'name':e['name'], 'image':e['img'], 'discover':False, 'ideas':False, 'category':'cuisine'} for e in cuisines]
	discover = random.sample(ret_cuisines, 6)
	for e in discover:
		e['discover'] = True
	ideas = random.sample(discover, 3)
	for e in ideas:
		e['ideas'] = True
	
	ret['data']['timestamp'] = int(time.time())
	ret['data']['items'] = ret_ingredients + ret_dishes + ret_cuisines
	return ret

# ingredient_dict = {
#     "almonds": "https://images.unsplash.com/photo-1508061253366-f7da158b6d46?ixlib=rb-1.2.1&auto=format&fit=crop&w=2100&q=80",
#     "apple": "https://images.unsplash.com/photo-1551445523-324a0fdab051?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=932&q=80",
#     "avocado": "https://images.unsplash.com/photo-1557925922-dac32ff4429f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=933&q=80",
#     "bacon": "https://images.unsplash.com/photo-1592086326871-f7cf2f1801ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80",
#     "banana": "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1400&q=80",
#     "basmati rice": "https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80",
#     "Bay Leaves": "https://images.unsplash.com/photo-1462374382194-b17428f8c5c4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80",
#     "beans": "https://images.unsplash.com/photo-1506620780696-e5cb6c54524e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80",
#     "beef": "https://images.unsplash.com/photo-1556269923-e4ef51d69638?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1942&q=80",
#     "bell pepper": "https://images.unsplash.com/photo-1587656221664-37e89ddebbf6?ixlib=rb-1.2.1&auto=format&fit=crop&w=975&q=80",
#     "blueberries": "https://images.unsplash.com/photo-1425934398893-310a009a77f9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2000&q=80",
#     "bok choy": "https://images.unsplash.com/photo-1511993226957-cd166aba52d8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=943&q=80",
#     "bread": "https://images.unsplash.com/photo-1549931319-a545dcf3bc73?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80",
#     "brie": "https://images.unsplash.com/photo-1584390572125-55f08d0bf3b0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80",
#     "broccoli": "https://images.unsplash.com/photo-1518164147695-36c13dd568f5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1400&q=80",
#     "cabbage": "https://images.unsplash.com/photo-1578208895671-29d47f61294e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1934&q=80",
#     "cardamom": "https://images.unsplash.com/photo-1541533693007-7ea47d894b0c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=976&q=80",
#     "carrots": "https://images.unsplash.com/photo-1445282768818-728615cc910a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80",
#     "cauliflower": "https://images.unsplash.com/photo-1568584952634-e9bb8a163e28?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2252&q=80",
#     "cheddar": "https://images.unsplash.com/photo-1589881133595-a3c085cb731d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1301&q=80",
#     "cheese": "https://images.unsplash.com/photo-1558221693-89a565d7ecd8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=975&q=80",
    # "cherry": "https://unsplash.com/photos/CR28Ot0ckaE",
    # "chia seeds": "https://unsplash.com/photos/MsTOg6rhRVk",
    # "chicken breasts": "https://unsplash.com/photos/J5ZivsKiu9c",
    # "chicken legs": "https://unsplash.com/photos/qvQdLikf7wk",
    # "chicken stock": "https://unsplash.com/photos/oO3sXE73unQ",
    # "chicken thighs": "https://unsplash.com/photos/mjcJ0FFgdWI",
    # "chicken wings": "https://unsplash.com/photos/YgirePmHPZU",
    # "chickpea": "https://unsplash.com/photos/gDrv3jaD9-c",
    # "chocolate": "https://unsplash.com/photos/YemxYB75xvI",
    # "cilantro": "https://unsplash.com/photos/9rt6gV_IjhA",
    # "cod": "https://unsplash.com/photos/dUqX2Eq-2jk",
    # "collard greens": "https://unsplash.com/photos/yItVmeh1XA8",
    # "cookies": "https://unsplash.com/photos/OfdDiqx8Cz8",
    # "corn": "https://unsplash.com/photos/r7NhxSjz7e4",
    # "couscous": "https://unsplash.com/photos/f96pzsJZpc",
    # "cream cheese": "https://unsplash.com/photos/6FbArnPXEVg",
    # "cucumber": "https://unsplash.com/photos/L8GbxVUQ-f0",
    # "edamame": "https://unsplash.com/photos/xxpTa8rJjWY",
    # "egg whites": "https://unsplash.com/photos/osPCHdpXKxk",
    # "eggs": "https://unsplash.com/photos/A4z0UBgAwyc",
    # "english muffin": "https://unsplash.com/photos/A5jf5EmBAf8",
    # "fennel": "https://unsplash.com/photos/8rTwokBwz1w",
    # "fenugreek leaf": "https://unsplash.com/photos/9JxyBXRyq9I",
    # "fettuccine": "https://unsplash.com/photos/h_k7RPxv3yI",
    # "fish": "https://unsplash.com/photos/ZC-hGIK63wQ",
    # "fish sauce": "https://unsplash.com/photos/8502DXwY-7U",
    # "Five spice": "https://unsplash.com/photos/YUIMwavk7AQ",
    # "flour": "https://unsplash.com/photos/fGpO3NSFqtg",
    # "flour tortillas": "https://unsplash.com/photos/HBFAVR5XoO4",
    # "fresh fruit": "https://unsplash.com/photos/V9g1kwNsxwc",
    # "fresh herbs": "https://unsplash.com/photos/mRaNok_Ld6s",
    # "fresh mint": "https://unsplash.com/photos/boadZKqd1YM",
    # "frozen spinach": "https://unsplash.com/photos/4jpNPu7IW8k",
    # "garlic": "https://unsplash.com/photos/gKt9wZp2ujU",
    # "garlic powder": "https://unsplash.com/photos/uUxpNo2r4kw",
    # "garlic salt": "https://unsplash.com/photos/4OfaTz6SdYs",
    # "ginger": "https://unsplash.com/photos/2VePbF_YRK8",
    # "goat cheese": "https://unsplash.com/photos/nVH-5t4LxmY",
    # "granola": "https://unsplash.com/photos/_d1K4GfapEk",
    # "greek yogurt": "https://unsplash.com/photos/4caIPcmVDII",
    # "green beans": "https://unsplash.com/photos/2LYnYgd63Uw",
    # "grapes": "https://unsplash.com/photos/XUvWJUiX3FY",
    # "ground beef": "https://unsplash.com/photos/c3mFafsFz2w",
    # "ground pork": "https://unsplash.com/photos/Bdvtk5scbpE",
    # "ground turkey": "https://unsplash.com/photos/XaDsH-O2QXs",
    # "guacamole": "https://unsplash.com/photos/e-WEn5zBMPc",
    # "ham": "https://unsplash.com/photos/1OfPse1qVLM",
    # "hoisin sauce": "https://unsplash.com/photos/jpkfc5_d-DI",
    # "jasmine rice": "https://unsplash.com/photos/xmuIgjuQG0M",
    # "kale": "https://unsplash.com/photos/5eM6sRTCCUc",
    # "kosher salt": "https://unsplash.com/photos/4OfaTz6SdYs",
    # "lemon": "https://unsplash.com/photos/y_spQMQTFjs",
    # "lettuce": "https://unsplash.com/photos/1qnIDA6gZ1g",
    # "lime": "https://unsplash.com/photos/EqLj8q_Y_Yk",
    # "linguine": "https://unsplash.com/photos/-F_5g8EEHYE",
    # "mango": "https://unsplash.com/photos/BRiT_s3tN6Y",
    # "marinara sauce": "https://unsplash.com/photos/d2B90dLCNy4",
    # "meat": "https://unsplash.com/photos/UC0HZdUitWY",
    # "milk": "https://unsplash.com/photos/p3ViLmVgVJ4",
    # "mushroom": "https://unsplash.com/photos/XJY1C5LVNn8",
    # "Oat milk": "https://unsplash.com/photos/RVnDPsyiLEg",
    # "okra": "https://unsplash.com/photos/CoIJlCZEjnw",
    # "olive oil": "https://unsplash.com/photos/uOBApnN_K7w",
    # "olives": "https://unsplash.com/photos/RuqOeMvPlzQ",
    # "onions": "https://unsplash.com/photos/bC1fXU1v98U",
    # "oregano": "https://unsplash.com/photos/dMWEdVQcBW0",
    # "oyster sauce": "https://unsplash.com/photos/k9AGrP110tg",
    # "paneer": "https://unsplash.com/photos/jTv_cWxEtFs",
    # "parmesan": "https://unsplash.com/photos/kp_kwQmtr4c",
    # "pasta": "https://unsplash.com/photos/t8hTmte4O_g",
    # "pasta sauce": "https://unsplash.com/photos/2CZ0Zpuj-gU",
    # "peach": "https://unsplash.com/photos/O3TlS547j7k",
    # "peanut butter": "https://unsplash.com/photos/Z4zLE_8VZTc",
    # "peas": "https://unsplash.com/photos/8walmVeW47A",
    # "peppers": "https://unsplash.com/photos/83eiYCPC_tU",
    # "pesto": "https://unsplash.com/photos/12eHC6FxPyg",
    # "pork": "https://unsplash.com/photos/P7Um6_hkwbU",
    # "pork belly": "https://unsplash.com/photos/fXg78OFlyu8",
    # "pork chops": "https://unsplash.com/photos/Yr4n8O_3UPc",
    # "potatoes": "https://unsplash.com/photos/LSZfNPVZjTw",
    # "quinoa": "https://unsplash.com/photos/oZ4Krez3X5o",
    # "ramen noodles": "https://unsplash.com/photos/rAyCBQTH7ws",
    # "rice": "https://unsplash.com/photos/zXNC_lBBVGE",
    # "rice milk": "https://unsplash.com/photos/WmF_XLF4-Rs",
    # "rice noodles": "https://unsplash.com/photos/IQAnyxH9TnE",
    # "rosemary": "https://unsplash.com/photos/Wl-z9lbwkSI",
    # "salmon": "https://unsplash.com/photos/fV3zTanbO80",
    # "sausage": "https://unsplash.com/photos/cSxpCQrRlo8",
    # "sea scallops": "https://unsplash.com/photos/RwDmUKpUP50",
    # "sesame oil": "https://unsplash.com/photos/CUKjQAmTf74",
    # "sesame seeds": "https://unsplash.com/photos/k-JORnd7LnY",
    # "shallot": "https://unsplash.com/photos/GrHWJVA1KTA",
    # "soy milk": "https://unsplash.com/photos/3d4VRbKaYBE",
    # "soy protein powder": "https://unsplash.com/photos/C05u9Xh37to",
    # "soy sauce": "https://unsplash.com/photos/McP48IRa7Mo",
    # "spaghetti": "https://unsplash.com/photos/2CZ0Zpuj-gU",
    # "spinach": "https://unsplash.com/photos/6AAptb2kBak",
    # "squash": "https://unsplash.com/photos/q70dT-fiZ4s",
    # "sriracha sauce": "https://unsplash.com/photos/PFX41973J6M",
    # "strawberries": "https://unsplash.com/photos/kH3Sr9K8EBA",
    # "sweet potato": "https://unsplash.com/photos/QQwqe5WnwKw",
    # "taco shells": "https://unsplash.com/photos/0FXw7F4lJGk",
    # "teriyaki sauce": "https://unsplash.com/photos/d2B90dLCNy4",
    # "thai basil": "https://unsplash.com/photos/wS-5JFH8-oU",
    # "tofu": "https://unsplash.com/photos/PqsImnjuElM",
    # "tomatoes": "https://unsplash.com/photos/UD_j10SKj5g",
    # "tortilla": "https://unsplash.com/photos/HBFAVR5XoO4",
    # "Tumeric": "https://unsplash.com/photos/yTnjFssdo7w",
    # "tuna": "https://unsplash.com/photos/UxhIU5f5GN4",
    # "turkey": "https://unsplash.com/photos/GyV6SL_fKsI",
    # "vanilla": "https://unsplash.com/photos/tgYIwIk0D4U",
    # "vegan cheese": "https://unsplash.com/photos/bBCRrplhhZ4",
    # "vegan chocolate chips": "https://unsplash.com/photos/-TnkKAJ7LZQ",
    # "vegetable broth": "https://unsplash.com/photos/dOdtMzvjoc4",
    # "vegetarian bacon": "https://unsplash.com/photos/XMAflF2mtZo",
    # "walnuts": "https://unsplash.com/photos/Qs1tI95CCF0",
    # "whipping cream": "https://unsplash.com/photos/3nCRXsHdCNM",
    # "yeast": "https://unsplash.com/photos/gMZNtPDqobg",
    # "yogurt": "https://unsplash.com/photos/NFHeBysjCTI"
# }


# dishes = {
#     "Katsu": "https://images.unsplash.com/photo-1569050467447-ce54b3bbc37d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1300&q=80",
#     "Sushi": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80",
#     "Crepes": "https://images.unsplash.com/photo-1515467837915-15c4777ba46a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2253&q=80",
#     "Pancakes": "https://images.unsplash.com/photo-1541288097308-7b8e3f58c4c6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80",
#     "Khao Soi": "https://images.unsplash.com/photo-1514540746696-d285708190bb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80",
#     "Udon": "https://images.unsplash.com/photo-1558985212-324add95595a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80",
#     "Bowls": "https://images.unsplash.com/photo-1533244769204-d345e73a30c1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1980&q=80",
#     "Shakshuka": "https://images.unsplash.com/photo-1590412200988-a436970781fa?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=975&q=80",
#     "Ropa Vieja": "https://images.unsplash.com/photo-1523986490752-c28064f26be3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80",
#     "Kefta": "https://images.unsplash.com/photo-1520218508822-998633d997e6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80",
#     "Cuban Mojo": "https://images.unsplash.com/photo-1567953921490-6f671d196d1d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=975&q=80",
#     "Pad thai": "https://images.unsplash.com/photo-1559314809-0d155014e29e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80",
#     "Lasagna": "https://images.unsplash.com/photo-1581904243918-7aac00cefed2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=933&q=80",
    # "Fried Rice": "https://unsplash.com/photos/CvLZ6hbIemI",
    # "Yakisoba": "https://unsplash.com/photos/eSaQDaGLgwY",
    # "Burritos": "https://unsplash.com/photos/F10nTHkCiW8",
    # "Hummus": "https://unsplash.com/photos/FBbGyco88GU'",
    # "Toasts": "https://unsplash.com/photos/FFqNATH27EM",
    # "kebabs": "https://unsplash.com/photos/FlljpnwuJO4",
    # "Croque Madame": "https://unsplash.com/photos/FQWtCUiE4GM",
    # "Dumplings": "https://unsplash.com/photos/GZe_M6TUJ_k",
    # "Ravioli": "https://unsplash.com/photos/h7xulIktCg8",
    # "Jambalaya": "https://unsplash.com/photos/HDi8KXLm6kg",
    # "Tortellini": "https://unsplash.com/photos/HrcpO5MCedQ",
    # "Teriyaki": "https://unsplash.com/photos/IiZ2Gqxm5Pg",
    # "Granola": "https://unsplash.com/photos/iNWjJJXeym4",
    # "Hamburgers": "https://unsplash.com/photos/jh5XyK4Rr3Y",
    # "Tamales": "https://unsplash.com/photos/Jj1J3y9YEeo",
    # "Guacamole": "https://unsplash.com/photos/K7bd0WoYfoo",
    # "Empanadas": "https://unsplash.com/photos/kKzKFWA2Wig",
    # "tzatziki": "https://unsplash.com/photos/kQloRmVQYIs",
    # "Miso soup": "https://unsplash.com/photos/LDxq4MnYB5U",
    # "Smoothies": "https://unsplash.com/photos/lnz6eLsQrMM",
    # "Salads": "https://unsplash.com/photos/LzeNab6mRZY",
    # "couscous": "https://unsplash.com/photos/M-tzZD5z720",
    # "Drunken noodles": "https://unsplash.com/photos/MGFPFWSZfgM",
    # "Huevos Rancheros": "https://unsplash.com/photos/mkOpQDcFrx0",
    # "Daal": "https://unsplash.com/photos/mlwXrYYAOms",
    # "pizza": "https://unsplash.com/photos/MqT0asuoIcU",
    # "Omelettes": "https://unsplash.com/photos/N0u8bLrB_-g",
    # "Soba": "https://unsplash.com/photos/nAV0ojj-m4k",
    # "Tom Yum Soup": "https://unsplash.com/photos/oO3sXE73unQ",
    # "Souvlaki": "https://unsplash.com/photos/OyZJU94P4WM",
    # "Tempura": "https://unsplash.com/photos/P4ukp0mMlAQ",
    # "Chicken Curry": "https://unsplash.com/photos/PqsImnjuElM",
    # "Croque Monsieur": "https://unsplash.com/photos/Qc4i5V_pHEA",
    # "Fettuccine": "https://unsplash.com/photos/QeAbvIAJSLw",
    # "Ratatouille": "https://unsplash.com/photos/R02KgL5Ti3Y",
    # "Waffles": "https://unsplash.com/photos/S4dXp25NiLg",
    # "Ramen": "https://unsplash.com/photos/TWTxHN2QIGc",
    # "Sandwiches": "https://unsplash.com/photos/U0PiIS4Uvkc",
    # "Quesadillas": "https://unsplash.com/photos/u6oot_dGiug",
    # "Eggs": "https://unsplash.com/photos/uh0zvg5VjlA",
    # "Tikka Masala": "https://unsplash.com/photos/V0xp-dTS3z0",
    # "Noodles": "https://unsplash.com/photos/v2z6Yhp_6Gc",
    # "Risotto": "https://unsplash.com/photos/VNu0yM4kFdA",
    # "Quiches": "https://unsplash.com/photos/vrNs8Y8exAQ",
    # "Soups": "https://unsplash.com/photos/VVPC-DEBi2I",
    # "Cuban sandwich": "https://unsplash.com/photos/WcN0BupzoVg",
    # "Chow mein": "https://unsplash.com/photos/wiyl0_FGGKo",
    # "Chorizo": "https://unsplash.com/photos/Wp3qbHlw1mI",
    # "tortillas": "https://unsplash.com/photos/Wqgpy1qdV4c",
    # "Cuban Pork": "https://unsplash.com/photos/XgKtCnzbi34",
    # "Wontons": "https://unsplash.com/photos/xqiTvFFee6Y",
    # "Gyoza": "https://unsplash.com/photos/YHSeJVrqW58",
    # "Yakitori": "https://unsplash.com/photos/YRzmSMMv8WE",
    # "Gyros": "https://unsplash.com/photos/yw3L6Sg9exs",
    # "Grilled cheese": "https://unsplash.com/photos/ZB8NK8cB4EE",
    # "French Toast": "https://unsplash.com/photos/zcUgjyqEwe8",
    # "Tacos ": "https://unsplash.com/photos/ZQf4jzkpz1k",
    # "Gumbo": "NONE",
    # "Rigatoni": "NONE",
    # "Taquitos": "NONE",
# }

# cuisines = {
#     "American": "https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1934&q=80",
#     "Southern": "https://images.unsplash.com/photo-1574025343720-8eaa3bb9be37?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2689&q=80",
#     "Chinese": "https://images.unsplash.com/photo-1563245372-f21724e3856d?ixlib=rb-1.2.1&auto=format&fit=crop&w=2329&q=80",
#     "Cuban": "https://images.unsplash.com/photo-1574803636191-b2bbb307e9c6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=942&q=80",
#     "French": "https://images.unsplash.com/photo-1571157577110-493b325fdd3d?ixlib=rb-1.2.1&auto=format&fit=crop&w=934&q=80",
#     "German": "https://images.unsplash.com/photo-1568486504489-9e70d75313b8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80",
#     "Greek": "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?ixlib=rb-1.2.1&auto=format&fit=crop&w=2255&q=80",
#     "Hungarian": "https://images.unsplash.com/photo-1527976746453-f363eac4d889?ixlib=rb-1.2.1&auto=format&fit=crop&w=2689&q=80",
#     "Indian": "https://images.unsplash.com/photo-1565557623262-b51c2513a641?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2724&q=80",
#     "Italian": "https://images.unsplash.com/photo-1555072956-7758afb20e8f?ixlib=rb-1.2.1&auto=format&fit=crop&w=934&q=80",
#     "Japanese": "https://images.unsplash.com/photo-1519077204685-ed90d0cc05b7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2689&q=80",
#     "Mediterrean": "https://images.unsplash.com/photo-1565560665129-4831aa15206c?ixlib=rb-1.2.1&auto=format&fit=crop&w=975&q=80",
#     "Mexican": "https://images.unsplash.com/photo-1582234372722-50d7ccc30ebd?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1400&q=80",
#     "Moroccan": "https://images.unsplash.com/photo-1517314597476-e1788060b6cb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=933&q=80",
#     "Portuguese": "https://images.unsplash.com/photo-1591107576521-87091dc07797?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80",
#     "Southwestern": "https://images.unsplash.com/photo-1586561945641-98a839abd3f7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80",
#     "Spanish": "https://images.unsplash.com/photo-1571167366136-b57e07761625?ixlib=rb-1.2.1&auto=format&fit=crop&w=975&q=80",
#     "Thai": "https://images.unsplash.com/photo-1562565651-7d4948f339eb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2689&q=80",
#     "European": "https://images.unsplash.com/photo-1561668048-fe9c092832e0?ixlib=rb-1.2.1&auto=format&fit=crop&w=2102&q=80",
#     "Asian": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80"
# }

# print(json.dumps(dict(zip(cuisines.split('\n'), photos.split('\n'))), indent=4))

# with open('info.json', 'r+') as f:
# 	all_info = {}
# 	all_info['ingredients'] = [{"name":k, "img":v} for k, v in ingredient_dict.items()]
# 	all_info['dishes'] = [{"name":k, "img":v} for k, v in dishes.items()]
# 	all_info['cuisines'] = [{"name":k, "img":v} for k, v in cuisines.items()]
# 	f.seek(0)
# 	f.write(json.dumps(all_info, indent=4))
# 	f.truncate()
