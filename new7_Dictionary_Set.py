# dict={
#           "name":"Subrata",
#           "Roll":10800121170,
#           "Designation":"Student",
#           "marks":[92,91,85],
#           12:15
# }
# print(dict)
# # #to Assign to add a new Value
# # dict["name"]="Subrata Gorai" #It's Only For Reassigning
# # print(dict)
# dict["Address"]="Barabani Station Para"
# print(dict)

# Dictonaries are mutuable , But not contians duplicate keys


#Nested Dictonary
# dict1={
#           12:15,
#           "subjects":{
#                     "chem":85,
#                     "phy":87

      
#           }
# }
# print(dict1)
# print(dict1["subjects"]["chem"])
# print(dict1.keys())
# print(dict1.items())
# print(len(dict1))
# print(dict1.values())
# We can typecast the values which are returned by the keys  and values
# print(list(dict1.values()))
# print(dict1.get(12))
# We need get method over index method if we type any key value pair which are out of the dictionary
#index method give us error but get method returns none value
# dict1.update({"age":23,"name_01":"Hello"})
# print(dict1)

# -----------------SET in Python--------------
#1.Set are immutable
#2.We cannot store list or dictonary in SETS
# # SETS are Unordered 
# collection_set={1,2,3,4}
# print(type(collection_set))
# #Empty SET
# collection_set1=set({})
# print(type(collection_set1))
# #SETS are mutuable but it's values are immutable
# collection_set1.add(1)
# collection_set1.add("Hello")
# collection_set1.add(1)
# print(collection_set1)
# collection_set1.remove(1)
# collection_set1.remove(1)
# print(collection_set1)
# set1={12,2,3,4}
# set2={2,4,8,9,4}
# print(set1.union(set2))
# print(set2.intersection(set2))
dict={}
str=input("Enter the subject name:- ")
num1=int(input("Enter the marks"))
dict[str]=num1
str=input("Enter the subject name :- ")
num1=int(input("Enter the marks"))
# dict[str]=num1
dict.update({str:num1})
print(dict)