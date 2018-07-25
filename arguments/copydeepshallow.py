import copy

dict_of_capital = [['delhi','newdelhi'],['UP','lucknow'], ['UK', 'dehradun'],['bihar', 'patna']]

dict_of_capital1 = copy.copy(dict_of_capital)
dict_of_capital2 = copy.deepcopy(dict_of_capital)

print(id(dict_of_capital),id(dict_of_capital1),id(dict_of_capital2))
print(id(dict_of_capital[0]),id(dict_of_capital1[0]),id(dict_of_capital2[0]))
print(id(dict_of_capital[0][0]),id(dict_of_capital1[0][0]),id(dict_of_capital2[0][0]))

#dict_of_capital2[0][0] = 'mum'
dict_of_capital1[0][0] = 'gaya'
#del dict_of_capital

print(dict_of_capital2)
print(dict_of_capital1)
print(dict_of_capital)
print(id(dict_of_capital[0][0]),id(dict_of_capital1[0][0]),id(dict_of_capital2[0][0]))
print(id(dict_of_capital[0]),id(dict_of_capital1[0]),id(dict_of_capital2[0]))

print("new")
a = [[0,1],[2,3],[4,5]]
b = copy.copy(a)
c = copy.deepcopy(a)
print(id(a),id(b),id(c))
print(id(a[0]),id(b[0]),id(c[0]))
print(id(a[0][0]),id(b[0][0]),id(c[0][0]))
b[0][0] = 6
print(id(a[0]),id(b[0]),id(c[0]))
print(id(a[0][0]),id(b[0][0]),id(c[0][0]))




