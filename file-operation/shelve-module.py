import shelve
tele_dict = shelve.open("shelveFile")

#tele_dict['sachin'] = {"first_nane": "rahul" , "last_name": "raman" , "phone": 9873444005}
#tele_dict['sparsh'] = {"first_name": "romit" , "last_name": "singh" , "phone" : 9344455555}
#tele_dict.close()

tele_dict =shelve.open("shelveFile")
print(tele_dict['sachin'])

print(type(tele_dict['list_cities']))
tele_dict.close()
