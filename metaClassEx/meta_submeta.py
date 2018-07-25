class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):
        print('In SuperMeta.call: ', classname, supers, classdict, sep='\n...')
        return type.__call__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In SuperMeta init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))

print('making metaclass')

class SubMeta(type, metaclass=SuperMeta):
    def __new__(meta, classname, supers, classdict):
        print('In SubMeta.new: ', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In SubMeta init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))

class Eggs:
    pass

print('making class')

class Spam(Eggs, metaclass=SubMeta):
    data = 1
    def __init__(self,x):
        self.x = x
    def meth(self, arg):
        return self.data + arg

if __name__ == "__main__":
    print('making instance')
    x = Spam(2)
    print(x.meth(2))

    print(x.__class__)
    print(x.__dict__)

    print(Spam.__class__)
    print(SubMeta.__class__)
    print(SuperMeta.__class__)
    print(Spam.__bases__)
    print(Spam.__mro__)
    print(type(Spam))
    print(type(SubMeta))
    print(type(SuperMeta))


