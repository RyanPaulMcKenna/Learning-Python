#dictionary is collection unorder and mutable, key val pairs

mydict = {"name":"Max", "age": 28, "city":"New York"}
print(mydict)

mydict = dict(name="Mary", age=27, city="Boston")
print(mydict)


value = mydict["name"]
value = mydict["age"]
#value = mydict["blabla"] # exception: key error

#add item
mydict["thing"] = "max@xyz"


#delete item
del mydict["name"]
print(mydict)

mydict.pop("age")

#remove last
mydict.popitem()

if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["name"])
except:
    print("Error")

mydict = {"name":"Max", "age": 28, "city":"New York"}
for key in mydict:
    print(key)

# key method returns list of keys
for key in mydict.keys():
    print(key)

# values method return list of values
for value in mydict.values():
    print(value)

# for key, value in mydict.values():
#     print(key,value)


#copy dictionary, still linked not true copy both have changed
mydict_cpy = mydict
mydict_cpy["email"] = "max@xyz"


#actual copy
mydict_cpy = mydict.copy()
mydict_cpy = dict(mydict)


#merge, basically a union
mydict = {"name":"Max", "age": 28, "email": "max@xyz.com"}
mydict2 = dict(name="Mary", age=27, city="Boston")
mydict.update(mydict2)
print(mydict)


my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

value  = my_dict[3]
print(value) # 9

# can use typles are keys for dictionaries :)
# but not lists as they are mutable
mytuple = (8,7)
mydict = {mytuple: 15}



