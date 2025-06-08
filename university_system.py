class person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def speak(self):
            print(f"my name is {self.first_name} {self.last_name}")
            print(f"i have {self.age} years")
            
            
class student(person):
    def __init__(self, first_name, last_name, age, reg_no):
         super().__init__(first_name, last_name, age)
         self.reg_no = reg_no
        
    def talk(self):
        print(f"my registration number is: {self.reg_no}")
        
class lecturer(person):
    def __init__(self, first_name, last_name, age, course_unit):
         super().__init__(first_name, last_name, age)
         self.course_unit = course_unit
         
    def define(self):
        print(f"i teach {self.course_unit}")
        
class staff(person):
    pass

student1 = student("Ian","Noah",25,"U23007")
lecturer1 = lecturer("Ntambi","Geof",45,"Data Science")
staff1 = staff("Eron","Mary",21)

student1.speak()
student1.talk()
print("________________________")

lecturer1.speak()
lecturer1.define()
print("________________________")


staff1.speak()
