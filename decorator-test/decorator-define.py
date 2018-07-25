class decorator_cls:
    def __init__(self,func):
        self.func = func
        #print("class decorator: %s" %(self.func))

    def __call__(self, *args, **kwargs):
        #print("object called")
        self.func(*args)

def decorator_func(F):
    #print("func decorator called %s" %(F))

    def wrapper(*args):
        #print("func decorator called")
        return args[0] + args[1] + len(args)
    return wrapper


@decorator_cls
def func(*args):
    print(args[0] + args[1])

@decorator_func
def func1(*args):
    return args[0] + args[1]
#

if __name__ == "__main__":
    func(6,7)
    print(func1(6,7))