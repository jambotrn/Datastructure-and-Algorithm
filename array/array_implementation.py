

class Array_implementation:

    def __init__(self):
        self.length = 0
        self.data = []

    def get(self, index):
        return self.data[index]

    def push(self, item):
        # self.data[self.length] = item;  would'nt work because in python if a list is empty we don't assine a
        # value in a index.
        self.data.append(item)
        self.length += 1
        return self.data

    def pop(self):
        lastItem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return lastItem
    
    def delete(self, index):
        item = self.data[index]
        self.shift_item(index)
        return item

    def shift_item(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]

mycar = Array_implementation()

mycar.push('volvo')
mycar.push('tata')
mycar.push('bmw')

print(mycar.data)

print(mycar.delete(1))
print(mycar.data)
