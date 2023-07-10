"""
     Python is an object-oriented programming language. The concept of object-oriented programming (OOP) has been a major buzzword in the 
computer world for at least a couple decades. The term object stems from the fact 
that the model resembles objects in the real word in that each object is a thing 
that has certain attributes and characteristics that make it unique.
"""
import datetime as dt

#Creating a Class

class Member:
    pass

#Creating an Instance from a Class

#To create instances(objects) you need to give the class an init method!
#It have a specific name __init__(short of initialize)
#The self part is just a variable name and is used to refer to the object being created at the moment


class Member:
    def __init__(self,uname,fname):
        #Giving an Object It's Attributes
        self.uname = uname
        self.fname = fname
        self.show_date = dt.date.today()
    
    #Giving Class Methods
    def show_date(self):
        return f"{self.uname} joined on {self.date_joined:%m/%d/%y}"
        
        
member1 = Member("Mike","Mike Kal")

print(member1.show_date)