# data types
'''
Number(int,float,complex)
string(str)
tuple
list
dictinary(dict)
set
'''
# boolean types(bool)
'''
True
False
'''
# Number
a=5
b=5.0
c=2+4j
print(type(a))
print(type(b))
print(type(c))
# string
a="  hello   world"
b='''hello
  data'''
c='hello world'
#  012345678910
'''
print(type(a))
print(b)
print(c)
print(a.upper())
print(a.isupper())
print(a.islower())
print(a.capitalize())
print(a.title())
print(a.index("d"))
print(a[10])
print(a[0:5])
print(a[-2])
print(a.index("w"))
print(a.replace("world","ashok"))
# print(a.lstrip())
print(a. strip(' '))
print("{} string data ".format(a))
print(dir(a))'''
x={"x":4,"y":10}
print("(x) hello (y)".format_map(x))
y={"x":4,"y":10}
print("(x) hello (y)".format_map(**y))