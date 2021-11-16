# strings are immutable
my_string = "Hello World"
print(my_string)

my_string = 'I\'m a programer'
my_string = "I'm a programer"
# backslash escapes multiline string new line char
my_string = """Multi \
line \
string"""
print(my_string)

my_string = "Hello world"
char = my_string[0]
char = my_string[-1]
print(char)


substring = my_string[0:5]
print(substring) # hello


substring = my_string[::-1] # revese
substring = my_string[0::2] # every second element

greet = "Hello"
friend = "bob"
greeting = greet + " " + friend
print(greeting)


if 'ell' in greeting:
    print("yes")
else:
    print("no")

# remove whitespace
my_string = '       Hello World       '
my_string = my_string.strip()
print(my_string) # "Hello World"

my_string.upper() # make all uppercase
my_string.lower() # make all lowercase
my_string.startswith("hello")
my_string.endswith("world")

my_string.find('w') # return first index with character
my_string.count('d') # return number of d's
my_string.replace("world", "universe") # if can't find, does nothing

my_list = my_string.split(' ') # split to list by delimeter
print(my_list)
# the space below is the delimeter by which to join back together
new_string = ' '.join(my_list)

from timeit import default_timer as timer

my_list = ['a'] * 1000000 # ['a','a','a','a','a','a']
# print(my_list)

#bad makes copies
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop=timer()
print(stop-start)

#good - way faster
start = timer()
my_string = ''.join(my_list)
stop=timer()
print(stop-start)


#formatting strings
# %, .formate(), f-Strings

var = 3.14 
my_string = "the variable is %.2f" % var # s: string, d: integer, f: float .2f decimal points
print(my_string)

#.format
var = 3.14 
my_string = "the variable is {:.2f}".format(var)
print(my_string)

#f_strings
var = 3.14 
my_string = f"the variable is {var}"
print(my_string)

#f-Strings are the best