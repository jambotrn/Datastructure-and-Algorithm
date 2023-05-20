
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self, value):

        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return self.retrive()

    def prepend(self, value):
        new_node = Node(value)
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
    def remov(self, postion):
        if postion == 1:
            temp_node = self.head.next
            del self.head
            self.head = temp_node
            self.length -= 1
            return self.retrive()
        elif postion <= self.length and postion > 1:
            temp_node = self.head
            for i in range(1, postion-1):
                temp_node = temp_node.next
            
            del_node = temp_node.next
            temp_node.next = del_node.next
            del del_node
            self.length -= 1
            if temp_node.next == None:
                self.tail = temp_node
            return self.retrive()
        else:
            return "position dose not exist"

obje1 = Linkedlist(10)
obje1.append(5)
obje1.append(16)
obje1.prepend(1)
print(obje1.tail.value)
print(obje1.retrive())
print(obje1.length)
print(obje1.insert(12, 3))
print(obje1.tail.value)
print(obje1.head.value)
print(obje1.remov(5))
print(obje1.tail.value)
print(obje1.head.value)