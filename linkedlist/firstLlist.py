
class Linkedlist:
    def __init__(self, value):
        # self.head = Node(value)s
        self.head = {'value':value,
                     'next':None
                     }
        # self.head['next'] = None
        self.tail = self.head
        self.length = 1
    def append(self, value):
        new_node = {
            'value' : value,
            'next'  : None
            }
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node ={
            'value':value,
            'next':None
        }
        new_node['next'] = self.head
        self.head = new_node
        self.length +=1


obje1 = Linkedlist(10)
print(obje1.head['value'])
print(obje1.tail)
obje1.append(5)
obje1.append(16)
print(obje1.tail)
print(obje1.head)
obje1.prepend(1)
print(obje1.head)
print(obje1.length)