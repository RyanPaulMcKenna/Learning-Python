# *args = any number of positional args
# **kwargs = any number of keyword args
def foo(a,b, *args, **kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1,2,3,4,5,six=6,seven=7)

# every param after * must be keyword
def baa(a,b, *, c, d):
    print(a,b,c,d)

baa(1,2,c=3,d=4)

# last must be keyword: last=val
def gaa(*args, last):
    for arg in args:
        print(arg)
    print(last)

gaa(1,2,last=3)

def moo(a,b,c):
    print(a,b,c)

#unpacking args

# nums of elements in list must match nums of args in moo
my_list = [0,1,2]
moo(*my_list)

# nums of elements and keys must match moo func
my_dict = {'a':1,'b': 2, 'c': 3}
moo(**my_dict)

def gamma():
    global number
    x = number
    number = 3
    print('number inside func',x)

number = 0
gamma()
print(number)

# python passes object references by value

mult = 7 * 7 # 49

power = 2 ** 3 # 8

zeros = [0] * 10 # list with 10 elements of zero

alt = [0,1] * 10 # list with 10 0,1 ten times

nums = [1,2,3,4,5,6,7]

#unpack
begin, *midd, end = nums

print(begin)
print(midd)
print(end)

my_tup = (1,2,3)
my_set = {4,5,6}
# unpack tupple and set into list
new_list = [*my_tup, *my_set]
print(new_list)

#unapck dicts intos new dicts with **
dict_a={'a':1,'b':2}
dict_b={'c':3,'d':4}
my_dict = {**dict_a,**dict_b}
print(my_dict)

