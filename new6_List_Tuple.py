# marks=[2,8,8,7,8,6,2.3,8.6]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(len(marks))
# #Python list are different than arrays in C or JAVA Because it can store more than one data type
# #List are mutuable and it can reassign or modify the values

# print(marks[1:])
# # List Methods are
# #Sorting
# marks.sort()
# print(marks)
# #Reverse Sorting
# marks.sort(reverse=True)
# print(marks)
# #Adding value at the end
# marks.append(40)
# print(marks)
# #Insertion in specific Index
# marks.insert(4,88.9)
# print(marks)
# #Remove method removes the first Occurance Of an Element
# marks.reverse()
# marks.remove(2)
# print(marks)
# #Pop the element in a List at a given index
# marks.pop(4)




##---------Tuples--------------
#Tuple are Same as list but it's Immutable built in data type in Python
tup=(1,2,3,4,8,9,10)
print(type(tup))
print(tup)
print(tup[0])
#For single value tuple should be written in the fashion of Tup=(1,) if We write Tup=(1)  it's treated like integer



List1=[1,2,1]
List2=List1.copy()
List2.reverse()
print(List2)
if(List1==List2):
          print("Palindrome")
else:
        print("Not Palindrome")