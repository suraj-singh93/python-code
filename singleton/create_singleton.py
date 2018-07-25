def conditional_singleton(aclass):
    list_instance = {}

    def oncall(*args, **kwargs):
        nonlocal list_instance
        print(list_instance,args[0])

        if args[0] not in list_instance:
            print("new instance cretaed")
            list_instance[args[0]]  = aclass(*args, **kwargs)

        return list_instance[args[0]]

    return oncall


class parent():
    def __init__(self):
        pass

    def run1(self):
        print("me running")


@conditional_singleton
class Singleton(parent):

    def __init__(self,data):
        self.data = data

    def run(self):
        print(id(self))
        print(self.data)


if __name__ == "__main__":
    x = Singleton(2)
    x.run()
    y = Singleton(3)
    y.run()
    z = Singleton(2)
    z.run()
    z.run1()

