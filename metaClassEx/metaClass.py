class MetaTwo(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaTwo.new: ', meta, classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In MetaTwo.init:', Class,classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))


class Eggs:
    pass

print('making class')

class Spam(Eggs, metaclass=MetaTwo):
    data = 1
    priv_a = 4
    def meth(self, arg):
        return self.data



print('making instance')
# X = Spam()
# print('data:', X.data, X.meth(2))


# a = {'x':1}
# a.pop('x')
# print(a)
