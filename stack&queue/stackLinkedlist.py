
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top.value
    
    def push(self, value):
        new_node = Node(value)
        if self.top:
            new_node.next = self.top
            self.top = new_node
        else:
            self.top = new_node
            self.bottom = new_node
        self.length +=1

   
    def pop(self):

        if self.top == None:
            return None
        current_node = self.top
        self.top = current_node.next
        self.length -= 1
        return current_node.value
        # stack_element = []
        # current_node = self.top
        # while current_node:
        #     stack_element.append(current_node.value)
        #     current_node = current_node.next
        # return stack_element



stackObj = Stack()

stackObj.push('google')
stackObj.push('udemy')
stackObj.push('discord')
print(stackObj.pop())
print(stackObj.peek())
print(stackObj.length)
print(stackObj.bottom.value)