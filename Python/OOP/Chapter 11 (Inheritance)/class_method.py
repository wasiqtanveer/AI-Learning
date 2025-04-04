class employee:
    name = "wasiq"
    @classmethod #with this removed the output will be "wasiq"
    def get_name(cls):
        return f"the name in class method is {cls.name}"
        
    
new = employee()
new.name = "Ali"
print(new.get_name())
# in the above program the object attribute will take precedence over the class attribute
# so the output will be "Ali" instead of "wasiq",but if we want to access the class attribute
# to tackle this we use @classmethod , in this way we willl be able to call the class attribute

