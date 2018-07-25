import time

def timer(label=''):

    def decorator(func):

        def wrapper(*args,**kwargs):
            curr_time = time.clock()
            all_time = 0
            print("time: %s" %(curr_time))
            result =  func(*args,**kwargs)
            print("time taken in call function  %s having label %s: %.5f" %(func.__name__, label, all_time + (time.clock() - curr_time)))
            return result

        return wrapper

    return decorator

@timer('====>')
def test(a,b):
    time.sleep(2)
    return a + b

@timer('*******')
def test1(a):
    time.sleep(1)
    return a + 2

print(test(2,3))
print(test1(3))

