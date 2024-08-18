class Hi:
          name="Anonynomous"
          def __init__(self,name):
                 '''Method 1 for changing class variable'''
          #        Hi.name=name
                 '''Method 2 for changing class variable'''
                 self.__class__.name=name

h1=Hi("Hello")
print(Hi.name)