# Generators are function that return an iterable
# lazy execution, very memory efficent for large datasets

def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()

# for i in g:
#     print(i)

value = next(g) # 1
print(value)

value = next(g) # 2
print(value)

value = next(g) # 3
print(value)

#use as inputs to other funcs
def mygen():
    yield 1
    yield 2
    yield 3

f = mygen()

print(sum(f))

def countdown(num):
    print('starting')
    while num > 0:
        yield num
        num -=1

cd = countdown(4)

print(next(cd)) # 4
print(next(cd)) # 3
print(next(cd)) # 2
print(next(cd)) # 1

# big advantage very  memory efficient when working ith big data
import sys

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1

mill = 1000000
print(sys.getsizeof(firstn(mill))) # 8448728 bytes

print(sys.getsizeof(firstn_gen(mill))) # 112 bytes

def fibonacci(limit):
    # 0 1 1 2 3 5 8 13 ...
    a,b = 0, 1
    while a < limit:
        yield a
        a,b = b, a + b

fib = fibonacci(30)

for i in fib:
    print(i)

# comprhension style generator
mygen1 = (i for i in range(mill) if i % 2 == 0)

# list comprehension: not a generator
mylist = [i for i in range(mill) if i % 2 == 0]

print(sys.getsizeof(mygen1))
print(sys.getsizeof(mylist))
