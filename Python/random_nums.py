import random

a = random.random()
print(a)

b = random.uniform(1,10)
print(a)

c = random.randint(1,10)
c = random.randrange(1,10)
print(a)

d = random.normalvariate(0,1) # random var from normal distrobution

mylist = list("ABCDEFGH")

#random element from mylist
a = random.choice(mylist)
print(a)

a =random.sample(mylist,k=3)
print(a)

# shuffles the letters
random.shuffle(mylist)
print(mylist)

# Reproducable random numbers, for testing only
random.seed(1)
print(random.random())
print(random.randint(1,10))


import secrets

a = secrets.randbelow(10)
print(a)

# highest binary number of that length 4 => 1111 = 15
a = secrets.randbits(4)
print(a)

import numpy as np

arr = np.random.rand(3) # 1D x 3 arr
print(arr)

arr = np.random.rand(3,3) # 3D by 3 elements
print(arr)

# fill with rands from 0 to 10 in a 1 by 3 arr
arr = np.random.randint(0,10,3)
print(arr)

# fill with rands from 0 to 10 in a 3 by 4 arr
arr = np.random.randint(0,10, (3,4))
print(arr)

# for testing rands with nump use this not the standard one
np.random.seed(1)

# shuffles only the first axis
np.random.shuffle(arr)
