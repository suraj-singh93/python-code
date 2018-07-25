def decorate_method(F):
    
    def wrapper(*args):
        print("class_id: %s" %(id(args[0])))
        return args[0].x + args[1] + args[2]
    return wrapper






class method_deocrated:
    def __init__(self,x):
        self.x = x

    @decorate_method
    def perform_add(self,a,b):
        return self.x + a + b


if __name__ == "__main__":
    test_instance = method_deocrated(2)
    print("id of test instance %s" %(id(test_instance)))
    x = test_instance.perform_add(2,3)
    print(x)
