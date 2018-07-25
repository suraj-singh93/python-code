def decorator_singleton(cls):
    instance = None
    def oncall(*args,**kwargs):
        nonlocal instance
        if instance == None:
            instance = cls(*args,**kwargs)
        return instance
    return oncall

@decorator_singleton
class test_singleton:
    def __init__(self, a):
        self.a = a

    def sum(self):
        return self.a + 2

if __name__ == "__main__":
    print(id(test_singleton(2)))
    print(id(test_singleton(3)))


