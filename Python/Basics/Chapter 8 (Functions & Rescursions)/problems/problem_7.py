word = input("Enter a the word to remove from the list: ")
lists = ["wasiq" , "haziq" , "daoud" , "saleh" , "faiq"]

def remove(lists,word):
    new = []
    for i in lists: # returns the list if even a sigle letter is matches(that letter is removed)
        if i != word:
            new.append(i.strip(word))
    return new

    # if word in lists: #return list if the word is completely matched(that word is removed)
    #     lists.remove(word)
    #     lists.strip(word)
    # return lists 

print(remove(lists,word))