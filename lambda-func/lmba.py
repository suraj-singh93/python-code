
def func(x):
    if  x % 5  and not x % 7:
        return x


a = list(filter(lambda x: int(x % 5) and not x % 7, [10,15,14,7,16]))

print(a)

a = [1,0,8,7,14]

print([x for x in a if x % 5 and not x % 7 ])



