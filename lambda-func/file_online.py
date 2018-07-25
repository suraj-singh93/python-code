with open("test") as fb:
    count = 0
    for text in fb.read():
        if text.isupper():
            count += 1


print(count)

with open("test") as fb: count = sum(1 for ch in fb.read() if ch.isupper())
print(count)


x = list(map(lambda x: int(x), ["1" , "10" , "5" , "3"]))
x.sort()
print(x)