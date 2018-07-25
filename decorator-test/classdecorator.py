# 1st exapmle
def classdecorator(F):
    print("class decorated")
    class wrapper:
        def __init__(self,x):
            self.x = x
    return wrapper

@classdecorator
class decoratedclass:
    def __init__(self):
        pass

a = decoratedclass(1)
print(a.x)
print(getattr(a ,'x'))
#help(getattr)

#2nd example
def decorateclass(cls):
    class wrapper:

        def __init__(self,*args):
            print("instance creations")
            self.wrapped =  cls(*args)


        def __getattr__(self, item):
            return getattr(self.wrapped, item)

    return wrapper

@decorateclass
class decoratedclasst:
    def __init__(self,x):
        self.x = x

    def method_sum(self,y):
        return self.x + y


if __name__ == "__main__":
    t = decoratedclasst(2)

    print(t.method_sum(2))

    y = decoratedclasst(3)
    print(y.method_sum(3))