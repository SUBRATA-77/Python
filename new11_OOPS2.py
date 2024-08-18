# class Bank_account:
#           def __init__(self,username,userpassword):
#                   self.username=username
#                   self.__userpassword=userpassword#__is used to make a variable private
#                   print("User name: ",username,"User Password ",userpassword)
#           def changepassword(self,password):
#                   self._userpassword=password
#                   print("After changing the password ",self._userpassword)
                    
# data=Bank_account("Hello","abc@12")
# data.changepassword("Hi")
# vars=10
# print(type(vars))

'''Inheritance'''
# class Car:
#           def __init__(self):
#                 print("Car start")
#                 print("Car Stop")
#           @staticmethod
#           def start():
#                 print("car starting....")
#           @staticmethod
#           def stop():
#                  print("car stopping.....")
# class Toyota_Car(Car):
#        def __init__(self,name):
#               self.name=name

# c1=Toyota_Car("Fortuner")
# c2=Toyota_Car("Hilux")
# c1.start()
# c2.stop()

'''Inheritance Types :-1.Single level 2.MultiLevel 3.Multiple'''

'''Example of Multiple Inheritance'''
# class A:
#        varA="Welcome to class A"
# class B:
#        varB="Welcome to class B"
# class C(A,B):
#        varC="Welcome to class C"
# c1=C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)
'''Super Method'''
class Car:
          def __init__(self,type):
               print("The car is of type: ",type)
          @staticmethod
          def start():
                print("car starting....")
          @staticmethod
          def stop():
                 print("car stopping.....")
class Toyota_Car(Car):
       def __init__(self,name,type):
              self.name=name
              super().__init__(type)


t1=Toyota_Car("Hilux","Diesel")