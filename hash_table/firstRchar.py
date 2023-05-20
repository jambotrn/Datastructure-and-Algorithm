# google interview question
# what is the first recurring character or duplicate item in
# the below given array

# Given an array = [2,5,1,2,3,5,1,2,4]
# It sholud return 2

# Given an array = [2,1,1,2,3,5,1,2,4]
# It should return 1
# Given an array = [2,3,4,5]
# It should return undifine

class RecurringChar:
    def __init__(self,arr):
        self.R_array = arr
    
    def R_chaker(self):
        newDict = dict()
        for item in self.R_array:
             if item in newDict:
                 return item
             newDict[item]=item
        return "undifine"



array1 = [2,5,1,2,3,5,1,2,4]
array2 = [2,1,1,2,3,5,1,2,4]
array3 = [2,3,4,5]

dictObj1 = RecurringChar(array1)
print(dictObj1.R_chaker())

dictObj2 = RecurringChar(array2)
print(dictObj2.R_chaker())

dictObj3 = RecurringChar(array3)
print(dictObj3.R_chaker())