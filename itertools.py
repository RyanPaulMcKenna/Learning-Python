# prodcut, permutations, combinations, accumulate, groupby, and 
# infinite iterators
from itertools import product

a = [1,2]
b = [3,4]

prod = product(a,b) # cartesian product of ordered pairs
print(list(prod))

a = [1,2]
c = [3]
prod = product(a,c, repeat=2) # cartesian product of ordered pairs
print(list(prod))

from itertools import permutations
alpha = [1,2,3]
perm = permutations(alpha) # every unqiue combination, order matters
print(list(perm))

from itertools import combinations, combinations_with_replacement
beta = [1,2,3,4]
comb = combinations(beta,2) # combinations of length 2, order doesn't matter
print(list(comb))

comb_wr = combinations_with_replacement(beta,2)
print(list(comb_wr))


from itertools import accumulate # compute sums of elements behind each
gamma = [1,2,3,4]
acc = accumulate(gamma)
print(gamma)
print(list(acc))

import operator # computer operator result on previous computation
acc2 = accumulate(gamma, func=operator.mul)
print(gamma)
print(list(acc2))

acc3 = accumulate(gamma, func=max) # compute max of each with previous
print(gamma)
print(list(acc3))


from itertools import groupby
omega = [1,2,3,4]

def smaller_than_3(x):
    return x < 3

# true: [1,2] false: [3,4]
group_obj = groupby(omega, key=smaller_than_3)
group_obj = groupby(omega, key=lambda x: x < 3) # as lambda func
for key, value in group_obj:
    print(key,list(value))



persons = [{'name': 'Tim', 'age': 25},
{'name': 'Dan', 'age': 25},
{'name': 'Lisa', 'age': 27},
{'name': 'Claire', 'age': 28}]

group_by_age = groupby(persons, key=lambda x: x['age'])
for key, value in group_by_age:
    print(key,list(value))


#infinite iterations
from itertools import count, cycle, repeat

#start at 10 and go forever
for i in count(10):
    print(i)
    if i == 15:
        break

# cycle through infinitely
phi = [1,2,3]
cycle_count = 5
for i in cycle(phi):
    if i == 3:
        cycle_count = cycle_count - 1
        print(i)
    if cycle_count == 0:
        break
    

#repeat 1, 4 times, no second arg mean inf times
for i in repeat(1,4):
    print(i)










