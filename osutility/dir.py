import os
import sys
import re
import ast

def list_file(path):
    try:
        for file in os.listdir(path):
            schildpath = os.path.join(path,file)
            if os.path.isdir(schildpath):
                print(schildpath)
                list_file(schildpath)
            else:
                print(schildpath)
    except FileNotFoundError:
        print("Path doesn't exist")




if __name__== "__main__":
    # print(os.name)
    # print(os.getcwd())
    # print(os.path.relpath('/Users/suraj/Desktop/','/Users/suraj'))
    #
    # try:
    #     print(os.listdir('/Users/suraj/Desktop/'))
    # except FileNotFoundError as ex:
    #     print(ex)
    #
    # print(os.path.split('/Users/suraj/Desktop'))
    # print(os.path.join(os.sep, 'Users','suraj'))
    # os.listdir()
    # print(os.environ.keys)
    #
    # print(os.environ['VIRTUAL_ENV'])
    data = "{'user': 'bob', 'age': 10, 'grades': ['A', 'F', 'C']}"
    print(ast.literal_eval(data),data,type(data))
    with open('config' , 'r+') as fb:
        for line in fb.readlines():
            if 'A_DICT' in line.strip('\n'):
                line = line.strip()
                key,value = line.split('=')[0],line.split('=')[1]
                print(value.lstrip(),type(value))
                d = ast.literal_eval(value.lstrip())
                print(type(d))
                for key in d:
                    print(key)
                    if key == 'A':
                        print("y")
                        d[key] == 10
                print(d)












    # for file in os.walk("/Users/suraj/Desktop/study/robot-framework"):
    #     print(file)
    # list_file("/Users/suraj/Desktop/study/robot-framework")
    # import pdb
    #
    # x = zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5))
    # print(x.__next__())
    # num_list = [10,7,14,35,49,70,0,77,1,140,147]
    # result = [item for item in num_list if item % 5 and not item % 7 ]
    # print([item*2 for item in num_list])
    # print("result: %s" %(result))