#Errors and Exceptions

try:
    a = 5 + '10' # mixing types illegally
except:
    print("TypeError")


try:
    import submodule  # module that does not exist
except:
    print("ModuleNotFoundError")

try:
    f = open('somefile.txt')
except:
    print("FileNotFoundError")

try:
    a = [1,2,3]
    a.remove(4)
except:
    print("ValueError")

try:
    a = [1,2,3]
    a[3]
except:
    print("Index Error")

try:
    my_dict = {'name': 'Max'}
    my_dict['age']
except KeyError:
    print("KeyError")


# Raise your own exceptions
try:
    x=-5
    if x < 0:
        raise Exception('x should be positive')
except Exception as e:
    print(e)

#assertion
#x=-5
#assert(x>=0), 'x is not positive'

# catch multiple types of exceptions and use else clause
try:
    x = 5 / 1
    b = a + 4
    #b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('It\'s all good!')
finally:
    print('That\'s a rap.') # runs regardles of except & else, used for cleanup

# subclassing Exeption class
class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small',x)

try:
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)




