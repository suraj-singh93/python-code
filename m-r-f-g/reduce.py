from functools import reduce
list_of_num = [2,3,4,10,1,10,40]
multile = reduce(lambda x,y:x*y,list_of_num)
print(multile)