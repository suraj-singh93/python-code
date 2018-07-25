'''
use non-local for writing decorator
for fucntions and methods
'''

def decorator(F):

    call_count = 0

    def callable(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        print("trace call count %s: %d" %(F.__name__, call_count))
        return F(*args,**kwargs)
    return callable



def decorate_class(cls):
    class wrapped:
        def __init__(self, *args, **kwargs):
            print("instance initalized")
            self.cls = cls(*args,**kwargs)

        def __getattr__(self, item):
            print("attribute fetch")
            return getattr(self.cls, item)

    return wrapped



@decorator
def decorated_func(a, b, x=1, y=2):
    return a + b + x + y

@decorator
def decorated_func2(*args):
    return args[0] + args[1]

@decorate_class
class test_class:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @decorator
    def decorated_method(self, val1):
        return self.a + self.b + val1


print(decorated_func(1, 2, x=3, y=4))
print(decorated_func(2, 3, x=4, y=10))
print(decorated_func2(2, 3))
obj1 = test_class(1, 2)
print(obj1.decorated_method(10))













