# counter, namedtuple, orderedDict, defaultdict, deque

from collections import Counter
a = "aaaaaabbbccc"
my_counter = Counter(a)
print(my_counter) # dictionary of frequency of chars in string
# list of tuples of 2 most common chars
print(my_counter.most_common(2))
print(my_counter.elements()) # list of all elements


from collections import namedtuple # similar to a struct
Point = namedtuple('Point', 'x,y') #name: Point, field: x,y
pt = Point(1,-4)
print(pt)
print(pt.x)
print(pt.y)

from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(ordered_dict)

from collections import defaultdict
d = defaultdict(int) # when access invalid key returns default val
#, zero for int
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d['d'])


# double ended queue, can add and remove items from both ends efficently
from collections import deque
deq = deque()

deq.append(1) 
deq.append(2)

deq.appendleft(3)
print(deq)

deq.popleft()
print(deq)

deq.pop() # remove last: 2
deq.popleft() # remove left-most: 3

deq.clear() # remove all
deq.extend([4,5,6]) # append the left, 6 will be left-most element 

#rotates 2 places to the right like a ring
deq.rotate(2)
#rotates 2 places to the left
deq.rotate(-2)


