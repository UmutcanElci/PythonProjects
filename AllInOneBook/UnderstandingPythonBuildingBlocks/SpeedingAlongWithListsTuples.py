scores = [88,92,78,90,96,83]
students = ["Mark","Amber","Todd","Anita","Sandy"]

has_Anita = "Anita" in students
print(has_Anita)# Returns True

#When we add something to list we use append

students.append("Bob")
#It's add the bob the Last index of the list

#In other hand Insert is same thing as append do ith little difference 

new_student = "Lupe"
students.insert(0,new_student)

#Insert function we need to give the location also to add the value

#Tuples
#A tuple is just an immutable list
#You can't change it after it's defined.
prices = (29.95, 9.98, 4.95, 79.98, 2.95)

#Sets 
#sets as a means of a organizing data
#Difference between list and sets is set have no specific order.
#Even though you amy define the set with the items in a certain order,  none of the items get index numbers.

sample_Set = {1.95,56.3,32.64,2.5,1}
