# f=open("demo.txt","r")
# data=f.read()#For reading entire data
# data=f.read(5)#For reading first 5  Characters
# data=f.readline() #For  reading a single line in  a file


# f=open("demo.txt","w")
# data=f.write("Hey there i am doing well today")#Over-Write the entire file
# print(data)


# f=open("demo.txt","a")
# data=f.write("\nHey there i am apending this  lines at  the end of the file")
# f.close()
# with open("demo.txt","r") as f:
#            data=f.read()
#            print(data)
#For deleting a file in python
import os
os.remove("demo.txt")