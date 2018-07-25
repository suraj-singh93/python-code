file_name = input()
count = 0
countupper =0
with open(file_name) as fb:
    for line in fb:
        count += len(line.split())

fb.close()
print(count)

with open(file_name) as fb:
    for c in fb.read():

        if c.isupper():
            countupper += 1



print(countupper)
fb.close()
