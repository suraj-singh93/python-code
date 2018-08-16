# Use functions to decorate class

# style-1
def decorate_class_1(F):
    print("class decorated")
    class wrapper:
        def __init__(self,x):
            self.x = x
    return wrapper



# style-2
def decorate_class_2(cls):
    class wrapper:

        def __init__(self,*args):
            print("instance creations")
            self.wrapped =  cls(*args)


        def __getattr__(self, item):
            return getattr(self.wrapped, item)

    return wrapper


@decorate_class_1
class decoratedclass:
    def __init__(self):
        pass

@decorate_class_2
class decorated_class:
    def __init__(self,x):
        self.x = x

    def method_sum(self,y):
        return self.x + y


if __name__ == "__main__":
    a = decoratedclass(1)
    print(a.x)
    ## print(getattr(a ,'x'))
    t = decorated_class(2)
    print(t.method_sum(2))



#output:

    # class decorated
    # 1
    # instance creations
    # 4
