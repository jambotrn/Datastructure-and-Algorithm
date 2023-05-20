class Node(object):
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class Btree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if not self.root:
            self.root = newNode
            return 'One node inserted as Root'
        else:
            currentNode = self.root

            while True:
                if value > currentNode.value:
                    if not currentNode.right:
                        currentNode.right = newNode
                        return currentNode.right
                    currentNode = currentNode.right
                else:
                    if not currentNode.left:
                        currentNode.left = newNode
                        return currentNode.left
                    currentNode = currentNode.left
    def search(self, value):
        if not self.root:
            return None
        currentNode = self.root
        while currentNode:
            if value > currentNode.value:
                currentNode = currentNode.right
            elif value < currentNode.value:
                currentNode = currentNode.left
            elif value == currentNode.value:
                return True
        return False
    
    def delete(self, value):
        if not self.root:
            return None
        currentNode = self.root
        parentNode = None
        while currentNode:
            if value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            elif value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value == currentNode.value:

                # option 1 no right child
                if currentNode.right == None:
                    if parentNode == None:
                        self.root = currentNode.left

                    # if parent < current value, make left child a right child of parent
                    elif currentNode.value > parentNode.value:
                        parentNode.right = currentNode.left

                    # if parent > current value, make current left child a child of parent
                    elif currentNode.value < parentNode.value:
                        parentNode.left = currentNode.left
            
                # option 2: right child which does not have left child
                elif currentNode.right.left == None:
                    currentNode.right.left = currentNode.left
                    if parentNode == None :
                        self.root == currentNode.right
                    else:
                        # if parent > current, make right child of the left the parent
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.right

                        # if parent < current, make right child a right child of the parent
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.right
                
                # Option 3: Right child that has a left child
                else:
                    # find the Right child's left most child
                    leftmost = currentNode.right.left
                    leftmostParent = currentNode.right
                    while leftmost.left != None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left
                    
                    # Parent's left subtree is now leftmost's right subtree
                    leftmostParent.left = leftmost.right
                    leftmost.left = currentNode.left
                    leftmost.right = currentNode.right
                    if parentNode == None:
                        self.root = leftmost
                    elif currentNode.value < parentNode.value:
                        parentNode.left = leftmost
                    elif currentNode.value > parentNode.value:
                        parentNode.right = leftmost
                
                return True


#           20
#        15    29
#      10 18     50
#    5   11    35    74
    
BtObj = Btree() 
# print(BtObj.search(25))
# print(BtObj.insert(20))
# print(BtObj.root.value)
# test = (BtObj.insert(25))
# (BtObj.insert(2))
# (BtObj.insert(15))
# (BtObj.insert(22))
# print(BtObj.search(25))
BtObj.insert(20)
BtObj.insert(29)
BtObj.insert(15)
BtObj.insert(10)
BtObj.insert(18)
BtObj.insert(5)
BtObj.insert(11)
BtObj.insert(50)
BtObj.insert(35)
BtObj.insert(74)
print(BtObj.root.right.right.value)
BtObj.delete(50)
print(BtObj.root.right.right.value)
print(BtObj.root.right.right.left.value)
