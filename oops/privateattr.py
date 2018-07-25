# Since there is a valid use-case for class-private members (namely to avoid name clashes of names
# with names defined by subclasses), there is limited support for such a mechanism,
# called name mangling. Any identifier of the form __spam (at least two leading underscores,
# at most one trailing underscore) is textually replaced with _classname__spam,
#     where classname is the current class name with leading underscore(s) stripped.
#     This mangling is done without regard to the syntactic position of the identifier, as
#     long as it occurs within the definition of a class.

class Foo:


    __attr = 0  # private attribute
    attr1 = 1

    def test(self,x):
        return self.__attr + x


if __name__ == "__main__":
    t = Foo()
    # accessing private attribute in python
    print(t._Foo__attr)
    # can change private attribute
    t._Foo__attr = 3

    print(t.attr1)

    print(t._Foo__attr)

    print(t.test(3))

    print(Foo._Foo__attr)
    print(Foo.test(t, 1))


