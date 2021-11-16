#lambdas, short inline funcs, very handy

addTen = lambda x: x + 10
print(addTen(5))


timesTen = lambda x: x * 10
print(timesTen(5))


mult = lambda x,y: x*y
print(mult(2,7))

#sorted, map, filter, reduce

#sorted
points2D = [(1,2),(15,1),(5,-1),(10,4)]
# lambda sorts by the second val of the pairs
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D_sorted)

#sort by sums
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D_sorted)

#map
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

#list comprehension syntax
c = [x*2 for x in a]
print(c)

#filter, lambda get only even numbers
b = filter(lambda x: x%2==0,a)
print(list(b))

#same thing with list comprehensions - best way!
c= [x for x in a if x%2==0]
print(c)

from functools import reduce

# reduce has two args, gets elements from a, similar to accumulate 
product_a = reduce(lambda x,y: x*y,a)
print(product_a)

