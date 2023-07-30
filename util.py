from data import CATEGORY_LIST, POSTAL_CODES
import math
from random import randint, seed

seed(10)

def closetStr(string, lst):
    idx = 0
    queue = [[lst, idx]]
    while queue:
        cur, idx = queue.pop(0)
        tocheck = []
        for t in cur:
            if t.lower()[idx] == string.lower()[idx]:
                tocheck.append(t)
        if idx + 1 >= len(string) and tocheck:
            return tocheck   
        elif tocheck:
            queue.append([tocheck, idx + 1])
        else:
            if len(cur) == len(lst):
                return None
            else:
                return cur


def closetPostal(numStr, lst):
    numLst = [str(i) for i in lst]
    res = closetStr(numStr, numLst)
    if res and len(res) == len(lst):
        return None
    elif not res:
        min = math.inf
        for n in lst:
            if abs(n - int(numStr)) < min:
                res = n
    return [int(i) for i in res]
        

def checkNumByZip(category, zips, tree):
    count = 0
    zipsInCategory = [i.value for i in tree.getChild(category).children]
    for p in zips:
        if p in zipsInCategory:
            count += len(tree.getChild(category).getChild(p).children)
    return count

def checkNumByCategory(category, tree):
    cateTree = tree.getChild(category)
    postallst = [p.value for p in cateTree.children]
    return checkNumByZip(category, postallst, tree)
    

def getRestaurantsByZip(categroy, zips, tree, n=None):
    restaurants = []
    for p in zips:
        zipTree = tree.getChild(categroy).getChild(p)
        if zipTree:
            restaurants += zipTree.children
    if n and n < len(restaurants):
        return getRandomRestaurant(restaurants, n)
    else:
        return restaurants
        
def getRestaurantsByCategory(categories, tree, n=None):
    restaurants = []
    for c in categories:
        cateTree = tree.getChild(c)
        for p in cateTree.children:
            restaurants += p.children        
    if n and n < len(restaurants):
        return getRandomRestaurant(restaurants, n)
    else:
        return restaurants

def getZipbyCategory(categories, tree):
    zips = set()
    for c in categories:
        for p in tree.getChild(c).children:
            zips.add(p.value)
    return zips

def getRandomRestaurant(restaurants, n):
    randomRest = []
    if n >= len(restaurants):
        raise Exception('getRandomRestaurants n too large')
    while len(randomRest) < n:
        r = restaurants[randint(0, len(restaurants) - 1)]
        if r not in randomRest:
            randomRest.append(r)
    return randomRest


    
    

