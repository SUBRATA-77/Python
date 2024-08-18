# class Student:
#           name="Subrata"

# s1=Student()
# print(s1.name)


# #Concept of constructors
# class Student:
#           college_name="ABC College" #class variable/Attribute
#           #default constructors
#           def _init_(self):
#                   print("default called")
#           #parameterized constructors
#           def __init__(self,fullname,marks):
#                     self.name=fullname #object variable/Instance Attribute
#                     self.marks=marks
          
# class Student1:
#         name="Hello World"
#         def __init__(self):#--It will be automatically called when a object of a class created
#                print("Hello World01")

# Student1()
# k=Student("Subrata",98)
# print(k.name,k.marks)



#Concept of constructors
# class Student:
#           college_name="ABC College" #class variable/Attribute
#           #default constructors
#           def _init_(self):
#                   print("default called")
#           #parameterized constructors
#           def __init__(self,fullname,marks,college_name):
#                     self.name=fullname #object variable/Instance Attribute
#                     self.marks=marks
#                     self.college_name=college_name
#           @staticmethod
#           def hello():
#                   print("Welcome") #it is a object independent
#                   return "hello"

# data=Student("Subrata","93","Asansol Enginnering College ")
# print(data.name)
# print(data.college_name)
# print(data.marks)
# print(data.hello())

#OOPS pillars
# Abstractions->
class Car:
          def __init__(self):
                  self.acc=False
                  self.brk=False
                  self.clucth=False
          def start(self):
                  self.acc=True #This is a example of abstarction because we didn't know how it's performing works
                  self.brk=True
                  self.clucth=True
                  print("Car Started")

# del method is used to delete attribute or function of a class