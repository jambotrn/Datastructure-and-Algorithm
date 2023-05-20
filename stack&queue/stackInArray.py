
class Stack:
    def __init__(self):
        self.arrLink=[]

    def peek(self):
        return self.arrLink[len(self.arrLink)-1]
    
    def push(self, value):
        self.arrLink.append(value)
        return value
       
    def pop(self):
        return self.arrLink.pop()
        

newObj = Stack()
newObj.push('google')
newObj.push('udemy')
newObj.push('Discorse')
print(newObj.peek())
print(newObj.pop())
print(newObj.peek())
print(newObj.pop())
print(newObj.peek())