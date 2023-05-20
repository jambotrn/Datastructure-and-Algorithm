
class Hashtable:
    def __init__(self, size):
        # we use 'None' for the value of all list element because 
        # python dose not support to define the size of list
        # thats why we multiply the size with value and store it 
        self.data = [None]*size

    def _hash(self, key):
        hash = 0
        for k in range(0, len(key)):
            # ord() method conver the cherecter to its unique code of character
            hash = (hash + ord(key[k])*k) % len(self.data)
        return hash
    
    def set(self, key, value):
        address = self._hash(key)
        if self.data[address] == None:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data
    
    def get(self, key):
        address = self._hash(key)
        currentBucket = self.data[address]
        if currentBucket:
            for i in range(len(currentBucket)):
                if currentBucket[i][0]== key:
                    return currentBucket[i][1]
                
        return "out of index"
    def key(self):
        keys = []
        for key in self.data:
            if key != None:
                keys.append(key[0][0])
        return keys

hashObj = Hashtable(50)

print(hashObj._hash('hello'))
print(hashObj.set('hello', 10000))
print(hashObj.get('hello'))
print(hashObj.set('name', 'Amir'))
print(hashObj.get('name'))
print(hashObj.key())

