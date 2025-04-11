try:
    with (
      open("1.txt") as f1, 
      open("2.txt") as f2, 
      open("3.txt") as f3 
    ):
        # Add your code here to work with the files f1, f2, and f3
        pass
        
except Exception as e:
    print(e)