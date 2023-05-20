
# what is merge sort? -- Merge sort is on of sorting algorithm that merge and sort two sorted array
# for example -- arr1[1, 3, 4, 6] and arr2[2, 5, 30]
# and the new array after merge and sort is newarr[1, 2, 3, 4, 5, 6, 30]

class MergeSort :
    def __init__(self, arr1, arr2):
        self.array1= arr1
        self.array2 = arr2

    def arrMergeSort(self):
 # if one of two array is empty it will return another array, then it does not need to merge and sort the array
        if len(self.array1)==0:
            return self.array2
        if len(self.array2)==0:
            return self.array1
        
        mergeArr = []
        item1 = self.array1[0]
        item2 = self.array2[0]
        i=0
        j=0
        len1 = len(self.array1)
        len2 = len(self.array2)
        while i<len1 or j<len2:
            if j == len2-1 or item1 < item2:
                mergeArr.append(item1)
                if i == len1-1 :
                    item1 = item2
                else:
                    item1= self.array1[i]
                    i += 1

            else:
                mergeArr.append(item2)
                if j == len2-1 :
                    item2 = item1
                else:
                    item2 = self.array2[j]
                    j += 1

        return mergeArr
    
arr1 = [1, 3, 4] 
arr2 = [4, 5, 30]
mergeObj = MergeSort(arr1, arr2)
print(mergeObj.arrMergeSort())