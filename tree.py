from restaurant import Restaurant

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def addChild(self, child_node):
        self.children.append(child_node)

    def getChild(self, value):
        queue = [self]      
        while queue:
            cur = queue.pop(0)
            if isinstance(cur, Restaurant):
                return None
            elif cur.value == value:
                return cur
            elif cur.hasChildren():
                queue += cur.children
        return None
    
    def __str__(self):
        return str(self.value)
    
    def hasChildren(self):
        return len(self.children) > 0

    def traverse(self):
        stack = [[self, 0]]
        printStr = ''
        while stack:
            cur, level = stack.pop()
            if level > 0 and not isinstance(cur, Restaurant):
                printStr += ' '*(level - 1) + '|-'
            elif level > 0:
                printStr += ' '*(level - 1) + '->'
            printStr += str(cur) + '\n'
            level += 1
            if not isinstance(cur, Restaurant):
                for child in cur.children:
                    stack.append([child, level])
        print(printStr)
        


            


# index = TreeNode('restaurant index')
# p1 = TreeNode(2222)
# p2 = TreeNode(2211)
# c1 = TreeNode('chinese')
# r1 = Restaurant('ccc', 'ccccccccc', ['dfsdf', 'cvcv', 'rewr'])
# index.addChild(c1)
# c1.addChild(p1)
# c1.addChild(p2)
# p2.addChild(r1)

# print(index.getChild(2211))
# index.getChild(2211).traverse()
# index.traverse()



            