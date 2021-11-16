# function decorators
import functools

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        # Do ...
        result = func(*args, **kwargs)
        # Do ...
        print('End')
        return result
    return wrapper

@start_end_decorator # this is a decorator
def print_name():
    print('Alex')


#it does the same as this
#print_name = start_end_decorator(print_name)

print_name()


@start_end_decorator # need kwargs for multi args
def add5(x):
    return x + 5


result = add5(10)
print(result)

print(help(add5))
print(add5.__name__)

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=4)
def greet(name):
    print(f'Hello {name}')

greet('Ryan')

# nested/stacked decorators

def debug(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args,**kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

# multiple decorators are executed in the order they are listed
@debug
@start_end_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return 
    
say_hello('World')


# Class decorator

class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls } times')
        return self.func(*args,**kwargs)



@CountCalls
def say_something():
    print('Something')

# function knows how many times it has been executed
say_something()
say_something()

# useful for: timer for execution time, debug for extra info,
# checker for , register functions, cahce return vals or update state

