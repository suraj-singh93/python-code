from collections import Counter
list_of_dept = []
with open("dept.csv") as fb:
    for line in fb:
        *name , dept = line.split(',')
        list_of_dept.append(dept.rstrip())

counter = Counter(list_of_dept)
print(counter)
for key,value in counter.items():
    print(key,value)
