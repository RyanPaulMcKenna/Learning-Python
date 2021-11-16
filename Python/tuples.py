mytuple = ("Max", 28, "Boston")
mytuple = "Max", 28, "Boston"
print(mytuple, type(mytuple))

mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)

item = mytuple[0] # Max
item = mytuple[1] # Max
item = mytuple[-1] # Boston

 # mytuple[0] = "Tim" error tuples are immutable

for x in mytuple:
    print(x)

if "Max" in mytuple:
    print("Yes")
else:
    print("No")

mytuple1 = ('a','p','p','l','e')
print(len(mytuple1))
print(mytuple1.count('p'))
print(mytuple1.index('a')) 
#convert between list and tuple
my_list = list(mytuple)
mytuple2 = tuple(my_list) 
print(my_list)
print(mytuple2)

a = (1,2,3,4,5,6,7,8,9,10)
# from start to (but not including) index 5
b = a[:5]
#from index 2 to the end
c = a[2:]
#every second element
d = a[::2]
# reverse the tuple
e = a[::-1]

#unpacking
mytuple3 = "Max",28, "Boston"
name, age, city = mytuple3
# i1 is the first, i3 is the last and *i2 is a list containing
#  all others elements
i1, *i2, i3 = mytuple3
print(i2) # 28

## Memory comparison - tuple uses less memory
import sys 
my_list = [0,1,2,"Hello", True]
my_tuple = (0,1,2,"Hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# create a list and tuple 1 million times
# tuple is nearly 100 times faster
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))

