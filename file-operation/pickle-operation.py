import pickle

list_of_cities = ["mum","jaipur","delhi","gurgaon"]
fp = open("write-pickle.pkl", "wb")
pickle.dump(list_of_cities,fp)
fp.close()

fp = open("write-pickle.pkl","rb")
cities_list = pickle.load(fp)
print(type(cities_list))
print(cities_list)
fp.close()

### multi-object pickle

dict_state = {"harayana": "chandigarh" , "UP": "lucknow" , "UK": "dehradun"}

pickle_object = (list_of_cities,dict_state)

fp = open("pickle_file.pkl" , "wb")
pickle.dump(pickle_object,fp)
fp.close()
fp = open("pickle_file.pkl" , "rb")
list_of_cities,dict_state = pickle.load(fp)
print(list_of_cities,dict_state)