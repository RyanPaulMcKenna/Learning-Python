# lists are mutable.
mylist = ["banana", "cherry", "apple"]
print(mylist)

# banana
item = mylist[0]
print(item)
# last 
item = mylist[-1]
print(item)

for x in mylist:
    print(x)

if "banana" in mylist:
    print("yes")
else:
    print("no")

# length
print(len(mylist))

mylist.append("lemon")
mylist.insert(1, "blueberry")
print(mylist)

item = mylist.pop()
item = mylist.remove("cherry")
mylist.reverse()
mylist.sort()
new_list = sorted(mylist)
mylist = [0] * 5
print(mylist)

mylist2 = [1,2,3,4,5]
new_list = mylist + mylist2
print(new_list)

# Doesnt include end
a = mylist[0:5]
print(a)
#reverse
a = mylist2[::-1]
print(a)
# start at index colon step size
a = a[0::2]
print(a)

# all of these do the same thing, make a copy
mylist = mylist.copy()
mylist = list(mylist)
mylist = mylist[:]

#list comprehension, quick and elegant way of creating lists
mylist = [1,2,3,4,5,6]
b = [x * x for x in mylist]

print(mylist)
print(b)
