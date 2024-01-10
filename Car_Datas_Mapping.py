import pandas as pd
import numpy as np 
import requests
import time
import googlemaps
import datetime
import math
import statistics
import folium
from datetime import date
from datetime import datetime

car_data = pd.read_csv('/Users/yashpatel/Desktop/final_cars.csv')
final_row = car_data.columns.values
car_data.loc[len(car_data)] = final_row
car_data.columns = ['Name', 'Address', 'Coords']
addy_list = car_data['Address'].tolist()
print(type(addy_list[0]))
#print(addy_list[o])
country_list = [i for i in addy_list if i.split(',')[-1][1:] == 'United States']
print(len(country_list))
print(len(addy_list))
print(country_list[0].split(',')[-2][1:3])
nj_list = [i for i in country_list if i.split(',')[-2][1:3] == 'NJ']
print(len(nj_list))
print(nj_list[0])
nj_coords = []
nj_props = []
row = car_data.loc[car_data['Address'] == nj_list[0]]
print(row['Coords'].values)
for addy in nj_list:
   row = car_data.loc[car_data['Address'] == addy]
   nj_coords.append(row['Coords'].values[0])
   nj_props.append(row['Name'].values[0])
print(len(nj_coords))
print(len(nj_list))
print(len(nj_props))
print(nj_props[0])
print(type(nj_props[0]))


#print(car_data['Country'])
#print(car_data['Address'][-13:])
#sub_data = car_data.loc[car_data['Address'][-13:] == "United States"]
#print(sub_data['Address'])

coords = car_data['Coords']
print(coords[0])
props = car_data['Name']


m = folium.Map(location=[20,0], tiles="OpenStreetMap", zoom_start=2)
for i,v in enumerate(nj_coords):
    cords = v.split(',')
    lat = float(cords[0][1:])
    long = float(cords[1][1:-1])
    folium.Marker(
        location=[lat ,long ],
        popup=nj_props[i],
    ).add_to(m)
print(m)
m.show_in_browser()
now = str(datetime.now())
m.save('folium_tester' + now + '.html')
