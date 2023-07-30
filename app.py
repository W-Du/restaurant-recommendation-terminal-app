from restaurant import Restaurant
from tree import TreeNode
import util
from data import indexTree
from data import CATEGORY_LIST

def app():
    greeting()
    while True:
        categories = getCategories()
        while categories == -1:
            categories = getCategories()
        zips = getZips(categories)
        restaurants = getRestaurants(categories, zips)
        displayRestaurants(restaurants)
        con = ending()
        if (not con):
            break

        
        
    

def greeting():
    print('This is a restaurant recommendation app')

def getCategories():
    categories = None
    while not categories:
        print('Do you like to see categories? Y/N')
        x = input()
        if x.lower() == 'y' or x.lower() == 'yes':
            print(', '.join(CATEGORY_LIST))
        print('Which category do you prefer?')
        cInput = input().lower()
        categories = util.closetStr(cInput, CATEGORY_LIST)
        if not categories:
            print('We cannot find such category in the app, please try again')
    while len(categories) > 1:
        print('several categories might match: ' + ', '.join(categories))
        print('do you want to select a category from above options? Y for yes, N for no, B for back to index')
        x = input().lower()
        if x == 'y' or x == 'yes':
            new_category = None
            while not new_category:
                print('which one do you prefer?')
                cInput = input().lower()
                new_category = util.closetStr(cInput, categories)
                if not new_category:
                    print('Cannot interpret your input, please try again')
            categories = new_category
        elif x == 'n' or x =='no':
            break
        elif x == 'b':
            return -1 
            break 
    if len(categories) == 1:
        print('your category is: ' + categories[0])
    else:
        print('your categories are: ' + ', '.join(categories))     
    return categories

def getZips(categories):
    while True:
        print('Do you want to search for a restaurant by location? Y/N')
        x = input().lower()
        if x == 'n' or x == 'no':
            return None
            break
        elif x == 'y' or x == 'yes':
            zips = None
            zipOptions = util.getZipbyCategory(categories, indexTree)
            while not zips or len(zips) == len(zipOptions):
                print('please choose from the following zips: ' +', '.join([str(p) for p in zipOptions]))
                zInput = input()
                try:
                    covert = int(zInput)
                except Exception:
                    print('please enter a number')
                    continue
                zips = util.closetPostal(zInput, zipOptions)
                print('check. zips = ', zips)
            if len(zips) == 1:
                print('you chose the location of zip code: ', str(zips[0]))
            else:
                print('you chose an area of following zip codes: ', ', '.join([str(p) for p in zips]))
            return zips
            break
                
         

def getRestaurants(categories, zips=None):
    restaurants = []
    numRestaurants = 0
    if zips is None:
        numRestaurants = 0
        for c in categories:
            numRestaurants += util.checkNumByCategory(c, indexTree)
        if numRestaurants > 5:
            print(f'there are {numRestaurants} restaurants in categories selected, the following are five randomly selected')
            restaurants = util.getRestaurantsByCategory(categories, indexTree, 5)
            return restaurants
        else:
            restaurants = util.getRestaurantsByCategory(categories, indexTree)

    else:
        for c in categories:
            numRestaurants += util.checkNumByZip(c, zips, indexTree)
            restaurants += util.getRestaurantsByZip(c, zips, indexTree)
        if numRestaurants > 5:
            print(f'there are {numRestaurants} restaurants in categories and zip codes selected, the following are five randomly selected')
            restaurants = util.getRandomRestaurant(restaurants, 5)
        else:
            print(f'there are {numRestaurants} restaurants in categories and zip codes selected')
    return restaurants
        
def displayRestaurants(restaurants):
    print('-------------------------')
    for r in restaurants:
        r.toString()
        print('\n')
    print('-------------------------')

def ending():
    while True:
        print('Look for another restaurant? Y/N')
        x = input().lower()
        if x == 'n' or x == 'no':
            return False
            break
        elif x == 'y' or x == 'yes':
            print('\n')
            return True
            break
        else:
            print('what did you say?')
        

        
        
app()
