class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    def peek(self):
        return self.first
    
    def enqueue(self, value):
        new_node = Node(value)
        self.length += 1
        if self.first == None:
            self.first = new_node
            self.last = new_node
        self.last.next = new_node
        self.last = self.last.next
    
    def dequeue(self):
        if self.first:
            curr_node = self.first
            self.first = curr_node.next
            self.length -= 1
            return curr_node.value
        else:
            return 'queue is emty'


new_obj = Queue()

print(new_obj.dequeue())
new_obj.enqueue('amir')
new_obj.enqueue('samir')
new_obj.enqueue('kabir')
new_obj.enqueue('subir')
print(new_obj.dequeue())
print(new_obj.dequeue())
print(new_obj.dequeue())
print(new_obj.dequeue())
print(new_obj.dequeue())
print(new_obj.dequeue())