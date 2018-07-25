# The file cities_and_times.txt contains city names and times. Each line contains the name of the city,
# followed by the name of
# the day ("Sun") and the time in the form hh:mm. Read in the file and create an alphabetically ordered list of the form
# [('Amsterdam', 'Sun', (8, 52)), ('Anchorage', 'Sat', (23, 52)), ('Ankara', 'Sun', (10, 52)), ('Athens', 'Sun', (9, 52)),
# ('Atlanta', 'Sun', (2, 52)), ('Auckland', 'Sun', (20, 52)), ('Barcelona', 'Sun', (8, 52)), ('Beirut', 'Sun', (9, 52)),
# ...
#
#  ('Toronto', 'Sun', (2, 52)), ('Vancouver', 'Sun', (0, 52)), ('Vienna', 'Sun', (8, 52)),
# ('Warsaw', 'Sun', (8, 52)), ('Washington DC', 'Sun', (2, 52)), ('Winnipeg', 'Sun', (1, 52)), ('Zurich', 'Sun', (8, 52))]
#
# Finally, the list should be dumped for later usage with the pickle module.

import pdb
import pickle
city_list = []
pdb.set_trace()
fb = open("CityDateTime").readlines()
fb.sort()
for line in fb:
    *city_name,day,time = line.split()
    hours,minutes = time.split(':')
    city_tuple = (" ".join(city_name),day,(int(hours),int(minutes)))
    city_list.append(city_tuple)
    #print(type(city_tuple))
print(city_list)
fp = open("city.pkl","wb")
fp_pickle = pickle.dump(city_list,fp)
fp.close()

