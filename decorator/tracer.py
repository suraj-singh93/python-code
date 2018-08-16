## Tracer: print number of object created till now.

def decorator_tracer(aclass):
    instance_count = 0
    def oncall(*args, **kwargs):
        nonlocal instance_count
        instance_count += 1
        print("total object created:  {0}".format(instance_count))
        return aclass(*args, **kwargs)
    return oncall

@decorator_tracer
class test(object):
    def __init__(self):
        pass



if __name__ == '__main__':
    for i in range(3): test()

## output
    # total object created:  1
    # total object created:  2
    # total object created:  3








