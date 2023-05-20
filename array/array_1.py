# what is an array ?

#  An array is a special variable, which can hold more than one value at a time.
#  Variable array is somewhere in memory and the computer knows it.
#  When I do array[2], i'm telling the computer, hey go to the array and grab the 3rd
#  item from where the array is stored.

class Array_implement:
    def  __init__(self, arr):
        self.mycar = arr

    def display_car(self):
        for car in self.mycar:
            print(car)


cars = ["Ford", "Volvo", "BMW"]

carName = Array_implement(cars)
carName.display_car() # O(n)

# add new item at the end of the array 
cars.append("Tata") # O(1)

# remove one item at the end of the array
cars.pop() # O(1) because it only remove the item at the end of array 

# insert a item in a specifying position
cars.insert(0, "Honda") # O(n) because it shift all the item after its index in array

# print(cars[2]) # O(1)
print(cars)

# what is different between static array an dynamic array 
# static array is a array which define fixed size of memory in memory block . whenever it need to extend size of 
# array it wouldn't do that. but in dynamic array whenever need to extend array size it just copy the previous 
# array and allocate new size in memory in another memory block.