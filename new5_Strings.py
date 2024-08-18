# str1="My name is Subrata Gorai"
# str2="I am only my freind"
# strcon=str1+" "+str2 #String Concatination
# print(strcon)


# k=len(str1)
# print(k,type(k))


str="Hello World"
# print(str[1])
#str[1]='a' #-->It's not allowed reassining

print(str[1:6])#end Index not included

print(str[1:])
print(str[:6])
#a  p  p   l   e 
#-5 -4 -3  -2  -1


print(str.endswith("rld")) #endswith  function
print(str.lower()) #capitilize  for capital the first letter
str=str.capitalize()
print(str)
str=str.replace('o','a')
print(str)
print(str.count('l'))