from tree import TreeNode
from restaurant import Restaurant
from random import randint, seed

seed(10)
CATEGORY_LIST = ['Chinese', 'Italian', 'French', 'Spainish', 'Thaise', 'Japanese', 'Korean', 'American', 'Indian', 'Indonesian', 'Irish', 'Britain', 'Germen', 'Austrian', 'Mediterranean', 'Dutch']
POSTAL_CODES = [i for i in range(1011, 1020)] + [i for i in range(1130, 1140)] + [i for i in range(1271, 1280)]
DISH_NUM_MIN = 3
DISH_NUM_MAX = 6
POSTAL_NUM = 6
CANTEEN_NUM_MIN = 2
CANTEEN_NUM_MAX = 5


def generateRandomData():
    index = TreeNode('restaurant index')
    for c in CATEGORY_LIST:
        category = TreeNode(c)
        index.addChild(category)
        zipCodes = generatePostalCodes()
        for z in zipCodes:
            postal = TreeNode(z)
            category.addChild(postal)
            restaurants = generateRestaurants(c)
            for r in restaurants:
                postal.addChild(r)
    return index


def generateCuisines(category):
    cuisines = []
    num = randint(DISH_NUM_MIN, DISH_NUM_MAX)
    for i in range(num):
        d = category[:3].lower() + '_dish_' + str(randint(1, DISH_NUM_MAX))
        while d in cuisines:
            d = category[:3].lower() + '_dish_' + str(randint(1, DISH_NUM_MAX))
        cuisines.append(d)
    return cuisines

def generatePostalCodes():
    postals = []
    for i in range(POSTAL_NUM):
        p = POSTAL_CODES[randint(0, len(POSTAL_CODES)-1)]
        while p in postals:
            p = POSTAL_CODES[randint(0, len(POSTAL_CODES)-1)]
        postals.append(p)
    return postals

def generateNameAddr(category, option):
    nameAppend = ['restaurant', 'canteen', 'cafe', 'snacks']
    streetAppend = ['xx', 'yy', 'zz', 'ff', 'kk']
    if option == 'name':
        rand = randint(0, len(nameAppend)-1)
        name = category[0] + '_' + nameAppend[rand] + '_' + str(randint(99, 9999))
        return name
    elif option == 'address':
        rand = randint(0, len(streetAppend)-1)
        address = 'street ' + streetAppend[rand] + ' ' + str(randint(10, 100))
        return address
    else:
        raise Exception('either name or address for generateNameAddr function')

def generateRestaurants(category):
    rest_num = randint(CANTEEN_NUM_MIN, CANTEEN_NUM_MAX)
    restaurants = []
    for i in range(rest_num):
        r = Restaurant()
        r.setName(generateNameAddr(category, 'name'))
        r.setAddress(generateNameAddr(category, 'address'))
        r.setCuisines(generateCuisines(category))
        if len(restaurants) > 1:
            while r.findDup(restaurants):
                r.setName(generateNameAddr(category, 'name'))
                r.setAddress(generateNameAddr(category, 'address'))
        restaurants.append(r)
    return restaurants


indexTree = generateRandomData()
# indexTree.traverse()