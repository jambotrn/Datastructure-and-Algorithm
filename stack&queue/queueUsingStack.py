
class QueueUsingStack:

    def __init__(self) -> None:
        self.first = []
        self.last = []

    def enqueue(self, value):
        length = len(self.first)

        for i in range(length):
            self.last.append(self.first.pop())
        self.last.append(value)

    def dequeue(self):
        length = len(self.last)
        for i in range(length):
            self.first.append(self.last.pop())
        return self.first.pop()
    
    def peek(self):
        if len(self.last) > 0:
            return self.last[0]
        elif len(self.first) > 0:
            return self.first[len(self.first)-1]

    def empty(self):
        return not self.first and not self.last
    
newObj = QueueUsingStack()
print(newObj.empty())
newObj.enqueue('google')
newObj.enqueue('asccenture')
newObj.enqueue('IBM')
print(newObj.peek())
print(newObj.last)
print(newObj.dequeue())
print(newObj.dequeue())
print(newObj.peek())
print(newObj.first)

