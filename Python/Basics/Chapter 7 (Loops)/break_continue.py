# for i in range(10):
#     if (i == 5):
#         break # as i = 5  break the loop no matter what
    
#     print(i)   
for i in range(10): 
    if (i == 5 or i == 2 or i == 3):
          
        continue # as i = 5  skip the number and continue    
    print(i)       
    # ============ using pass in loop    
    for i in range(10):  
        pass #in case you want to populate this section later or not at all, without pass it will throw error