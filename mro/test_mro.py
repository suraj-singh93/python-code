class A(object):
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

class E(D):
    pass


if __name__== "__main__":
    a = E()
    print(E.__mro__)
    print(A.__class__)
    print(E.__bases__)
    print(D.__bases__)
    # import pdb
    # pdb.set_trace()