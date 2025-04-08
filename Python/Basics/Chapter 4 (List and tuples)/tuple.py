# unlike lists tuple are immutable , meaning they can be manippulated
tuple = (1,2,3,4)
tup = (1,) # single element tuple must contain a comma at the end or it will be considered an int
tpl = ()

print(type(tuple))

# tuple methods 
new  = tuple.count(2)
neww  = tuple.index(4)
print(new)
print(neww)


# tuple are ordered and unchangeable, meaning they cannot be changed or modified