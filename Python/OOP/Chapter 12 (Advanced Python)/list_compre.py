list1  = [2,32,41,2,3,4,1]
# list comprehension is an easy way to make a list from an existing list

list2 = [item for item in list1 if item > 5]
print(list2)