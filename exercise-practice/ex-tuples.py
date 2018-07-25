#            Tuples

#A tuple is an (immutable) ordered list of values. A tuple is in many ways
# similar to a list; one of the most important differences
#  is that tuples can be used as keys in dictionaries,
#  while lists cannot. Here is a trivial example:


d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
t = (5, 6)        # Create a tuple

print(d)
print(type(t))    # Prints "<class 'tuple'>"
print(d[t])       # Prints "5"
print(d[(1, 2)])  # Prints "1"
a = set(t)
print(a)
b = [2,3,2]
c = (2,3)
a = set(b)
print(a)
a =set(c)
print(a)

d = {(x,x+2):x for x in range(10)}
print(d)
