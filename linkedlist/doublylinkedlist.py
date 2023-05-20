
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Linkedlist:
    def __init__(self, value):

        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return self.retrive()

    def prepend(self, value):
        new_node = Node(value)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.length +=1
        return self.retrive()
    def insert(self, value, position):

        if position == 1:
           return self.prepend(value)
        elif position >= self.length:
            return self.append(value)

        else:
            new_node = Node(value)
            temp_node = self.head
            for i in range(1, position-1):
                temp_node = temp_node.next

            new_node.next = temp_node.next
            temp_node.next.prev = new_node
            new_node.prev = temp_node
            temp_node.next = new_node
            self.length +=1
        return self.retrive()

    def retrive(self):
        value = []
        temp_node = self.head
        while temp_node != None:
            value.append(temp_node.value)
            temp_node = temp_node.next
        return value
    
    def reverse(self):
        node_list = []
        if self.tail.prev == None:
            node_list.append(self.tail.value)
            return  node_list
        current_node = self.tail
        while current_node:
            node_list.append(current_node.value)
            current_node = current_node.prev
        return node_list
    def remov(self, postion):
        if postion == 1:
            temp_node = self.head.next
            temp_node.prev = None
            del self.head
            self.head = temp_node
            self.length -= 1
            return self.reverse()
        elif postion <= self.length and postion > 1:
            if postion == self.length:
                temp_node = self.tail.prev
                temp_node.next = None
                del self.tail
                self.tail = temp_node
                return self.retrive()
            temp_node = self.head
            for i in range(1, postion-1):
                temp_node = temp_node.next
            
            del_node = temp_node.next
            next_node = del_node.next
            temp_node.next = next_node
            next_node.prev = temp_node
            del del_node
            self.length -= 1
            
            return self.reverse()
        else:
            return "position dose not exist"
    

obje1 = Linkedlist(10)
print(obje1.retrive())
print(obje1.reverse())
obje1.append(5)
obje1.append(16)
obje1.prepend(1)
print(obje1.length)
print(obje1.insert(12, 3))
print(obje1.tail.value)
print(obje1.head.value)
print(obje1.retrive())
print(obje1.remov(1))
print(obje1.reverse())
#print(obje1.reverse())

# print(obje1.tail.value)
# print(obje1.head.value)