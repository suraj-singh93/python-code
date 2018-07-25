class test:
    a = 2
    def __init__(self):
        pass

t1 = test()
print(t1.a)
t2 = test()
print(t2.a)
t1.a = 3
print(t1.a)
print(t2.a)