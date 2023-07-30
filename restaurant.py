class Restaurant:
    def __init__(self, name='', address='', cuisines=[]):
        self.name = name
        self.address = address
        self.cuisines = cuisines
    
    def setName(self, name):
        self.name = name
    
    def setAddress(self, address):
        self.address = address

    def setCuisines(self, cuisines):
        self.cuisines = cuisines
    
    def toString(self):
        printStr = 'name: ' + self.name + '\n'
        printStr += 'address: ' + self.address + '\n'
        printStr += 'cuisines: ' + ','.join(self.cuisines)
        print(printStr)

    def __str__(self):
        return 'name: ' + self.name

    def findDup(self, rList):
        for r in rList:
            if self.name == r.name or self.address == r.address:
                return True
        return False


# r1 = Restaurant()
# r1.setName('hhh')
# r1.setAddress('bbbbbb')
# r1.addCuisine('c1')
# r1.addCuisine('c2')
# r1.addCuisine('c3')

# print(r1)
# r1.toString()

