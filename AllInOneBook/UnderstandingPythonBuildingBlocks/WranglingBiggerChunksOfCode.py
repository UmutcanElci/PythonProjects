#Functions provide a way to compartmentalize your code into small tasks that can be called from multiple places in an app.

#To create a function type def (short of definition) and name of the function that you want to create

def hello():
    print("Hello")
    
#TO run the function you created you need to call it first

hello()


#Defining optional parameters 

def hi(userName = "someone"):
    print("Hello, "+userName)

#That's give you the opportunity to input if not the default value is placed

