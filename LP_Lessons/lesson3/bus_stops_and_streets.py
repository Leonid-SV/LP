'''Остановки
Считать из csv-файла (с http://data.mos.ru/datasets/752) количество остановок, вывести улицу, на которой больше всего остановок.'''

# считывание списка остановок и улиц

import pandas as pd
from pprint import pprint

bus_stop_base = pd.read_csv('bus_stop_list/bus_stop_list.csv', sep = ';', encoding='cp1251')

bus_stop_streets = bus_stop_base['Street']

print(bus_stop_streets)

street_counter = {}
max = 0

for street in bus_stop_streets:

    if street in street_counter and street != 'проезд без названия':
        street_counter[street] += 1
    else:
        street_counter[street] = 1

for street_name, n_stops in street_counter.items():
    if n_stops > max:
        max = n_stops
        street_with_max_stop = street_name

print('1. ************************************')

print(f'На улице \"{street_with_max_stop}\" максимальное количество остановок, а именно: {max}')