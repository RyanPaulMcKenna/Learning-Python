#unordered, mutable, no duplicates
myset = {1,2,3,1,2,3}
print(myset)

# set from a lsit
myset = set([1,2,3])
# check how many unqiue letters in a word
myset = set("Hello")

#dictionary :
myset = {}
#empty set
myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

myset.remove(3)

try:
    myset(100)
except:
    print("Error") # key error

myset.discard(4) # does not throw exception
myset.clear() # empty the set
myset.add(1)
myset.pop() # returns and removes any element

for i in myset:
    print(i)

if 1 in myset:
    print("Huzzar!")

#union and intersection
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

union = odds.union(evens)
print(union) # combine without duplications

intersection = odds.intersection(evens)
print(intersection)

evenPrimes = evens.intersection(primes)


#difference
oddPrimes = primes.difference(evens)
print(oddPrimes)
#symetric difference - only contains what neither share
# - only contains what both don't have in common
justTwo = primes.symmetric_difference(evens)


# update similar to union
oddsandevens = odds.update(evens)

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

#subset superset and disjoint
print(primes.issubset(evens)) # false
print(union.issuperset(primes)) # true
print(evens.isdisjoint(odds)) # true


# make actual copy not reference copy
setA = {1,2,3,4}
cpy_setA = setA.copy()
cpy_setA = set(setA)


#frozenset - an immutable set
a = frozenset([1,2,3,4])
# a.remove(1) error




