marks = {
    "wasiq" : 95,
    "samar" : 90,
    "sajid" : 99,
    "nasir" : 9,
}

print(marks)
print(marks.items()) # gives a list(an array) of key value pairs
print(marks.keys()) # gives the keys (items at he left)
print(marks.values()) # gives the values (items at he right)
print(marks.get("wasiq")) 
"""
gives the value of the specific key, it is different form marks(["wasiq"]) in the way that
if there is no wasiq in the first it will return none, while with the other
it will return error
"""

marks.update({"nasir" : 80})
print(marks) 
""" 
after update the marks dictionary is printed, if the key is avalible it's value will be 
updated if not than the key and its corresponding value will be added to the dictionary
"""
#  ======================== More methods ================================

print(marks.setdefault("dasf" , 600)) #Returns the value of a key; if key is not found, inserts key with the default value.
marks.pop("wasiq") # removes the item based on provided key
print(marks) 
marks.popitem() #Removes and returns the last inserted key-value pair.
print(marks) 
marks.clear() # removes all elements from the dictionary.
print(marks) 

print("wasiq" in marks) # checks whether key is avalible or not and than return true or false base don search
