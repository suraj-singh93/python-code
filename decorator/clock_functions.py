### function decorator: trace run time

import time

def timer(label=''):

    def decorator(func):

        def wrapper(*args,**kwargs):
            curr_time = time.clock()
            result =  func(*args,**kwargs)
            print("%s(label=%s) run_time: %.5f"
                  %(func.__name__, label, (time.clock() - curr_time)))
            return result

        return wrapper

    return decorator

@timer('addition')
def add_operation(a,b):
    print("{} + {} = {}".format(a, b, a + b))

@timer('multiplication')
def mul_operation(a, b):
    print("{} * {} = {}".format(a, b, a * b))

if __name__ == "__main__":
    add_operation(2, 3)
    mul_operation(2, 3)


#output:

    # 2 + 3 = 5
    # add_operation(label=addition) run_time: 0.00008
    # 2 * 3 = 6
    # mul_operation(label=multiplication) run_time: 0.00001

