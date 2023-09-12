from abc import ABC , abstractclassmethod


class Person(ABC):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
    @abstractclassmethod
    def display_info(self):
        pass
    


class Student(Person):
    def __init__(self, name, age,student_id):
        super().__init__(self,name,age)
        self.student_id = student_id
        self.grades = []
        
    def add_grade(self, grade):
        self.grades.append(grade)
        
    def calculate_avg_grade(self):
        if len(self.grades) == 0 :
            return 0
        return sum(self.grades) / len(self.grades)
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")
        
    def display_grade(self):
        print(f"{self.name} : {self.calculate_avg_grade}")
        
        
        