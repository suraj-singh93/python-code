def function1(obj):
    return obj.x + 3

class MetaClass(type):

    def __new__(meta,classname,supers,classdict):
        classdict['method'] = function1
        return type.__new__(meta,classname,supers,classdict)




class Super:
    attr = 1
    def __init__(self):
        pass

print("makeing subclasses")
class Sub(Super, metaclass=MetaClass):

    def __init__(self,x):
        self.x = x


if __name__ == "__main__":

    t = Sub(1)
    print(t.method())


