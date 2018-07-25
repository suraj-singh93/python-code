#import sets
import glob
import re

s = glob.glob('*.py')
link = '  "-1": "https://assets-cdn.github.com/images/icons/emoji/unicode/1f44e.png?v8"'
a = list(re.split(r": +",link))

b = [2]
# b.append(3)
# print(b)
dict1 = {'A': ['xxx', 'yyy', 'zzz'], 'B': ['ooo', 'uuu', 'aaa'], 'C': ['ttt', 'qqq', 'ddd'], 'D': ['ggg', 'ppp', 'hhh']}

dict2 = {'B': ['ooo', 'uuu', 'aaa'], 'C': ['ttt', 'qqq', 'ddd'], 'A': ['xxx', 'yyy', 'zzz'], 'D': ['ggg', 'ppp', 'hhh']}

if dict1 == dict2:
    print('y')


list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = [0,3,5]
#
# index = 0
# for element in list2:
#     list1.pop(element - index)
#     index = index + 1
# print(list1)
# #help(enumerate)
#
# for i,v in enumerate(list1):
#     print(i,v)
#
#
#
# line_to_write = [1,5,10]
#
# file_write = open("file_write" , 'w')
# index = 1
# with open("file_read") as file_read:
#     for line in file_write.readlines():
#         if index in line_to_write:
#             file_write.writelines(line)
#         index = index + 1t(s)
#
#
#
# list1 = ["A1", "A2", "B1", "B2", "C1", "C2"]
# list2 = []
#
#
# list2 = [list1[index] +  list1[index +1] for index in range(0,len(list1),2)]
# print(list2)




