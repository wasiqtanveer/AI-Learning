# property decorator
class human:
    country_name = "USA"
    
    @property
    def countre(self):
        return self.country
    
    @countre.setter
    def countre(self,value):
        self.country = value
        
        
new = human()

new.country = "Pakistan"
print(new.country)