words = ["donkey" , "boss" , "maybe"]

with open("donkey.txt") as text:
    content = text.read()
    
    for word in words:
        content = content.replace(word , "#"* len(word) )
    
with open("donkey.txt" , "w") as text:
    text.write(content)