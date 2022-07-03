#unpacking operators
#operators that unpack values from iterable objects in python.
# single asterix * for any iterable, double asterix ** for dictionaries only.

# print_unpacked list
my_list = [1, 2, 3]
print(*my_list)

# extraction
my_list = [1, 2, 3, 4, 5, 6]
a, *b, c = my_list
print(a)
print(b)
print(c)

# merging_lists
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list)

# string_to_list.py
a = [*"RealPython"]
print(a)

# mysterious_statement.py same as to_list.py above.
*a, = "RealPython"
print(a)


# correct_function_definition.py 
def my_function(a, b, *args, **kwargs):
    pass


def my_sum(a, b):
    return a + b


def my_sum_list(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3]
print(my_sum_list(list_of_integers))

# *args varying number of positional arguments
# * is the unpacking operator in python.

def my_sum_args(*nums):
    result = 0
    # Iterating over the Python args tuple
    for x in nums:
        result += x
    return result

print(my_sum_args(1, 2, 3))

## **kwargs are the same as args for for key-value pairs, named arguments.
def concatenate(**words):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in words.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))