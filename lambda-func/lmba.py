## to print all number in a list divided by 7 but not by 5


def func(x):
    if  x % 5  and not x % 7:
        return x

a = [1,0,8,7,14]
## solution first using filter
b = list(filter(lambda x: int(x % 5) and not x % 7, a))
print(b)

### Solution using list comparhension
print([x for x in a if x % 5 and not x % 7 ])



