
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
arr = [1,2,3,5,4,8]
newd = dict()
for item in arr:
    if item in newd:
      print('yes')
    newd[item] = item
print(newd)