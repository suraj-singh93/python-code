squared = list((map(lambda x: x**2,[2,3,4,5] )))
print(squared)

def multiple(value):
    return value*3

list_of_items = list(map(multiple,squared))
print(list_of_items)