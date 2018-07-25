class base:
    y = 2


class test_get_attr(base):
    def __init__(self,x):
        self.x = x

    def __getattr__(self, item):
        print("attr name: %s" %(item))
        if item == 'test_attr':
            return self.x + 20
        else:
            raise AttributeError(item)







t = test_get_attr(2)
print(t.x)
# print(t.test_attr)
# print(t.y)
# print(t.z)
