'''Остановки у метро
Объединить наборы данных из предыдущих задач.
Посчитать, у какой станции метро больше всего остановок (в радиусе 0.5 км).'''

import pandas as pd
import numpy as np
from pprint import pprint

# считывание базы данных по московским станциям метро
metro_station_base = pd.read_excel('repair_of_escalators/repair_of_escalators.xlsx', encoding = 'cp1251')
metro_station_base = metro_station_base[metro_station_base.index <= 50]

# считывание базы данных по московским автобусным остановкам
bus_stop_base = pd.read_excel('bus_stop_list/bus_stop_list.xlsx', encoding='cp1251')
# bus_stop_base = bus_stop_base[bus_stop_base.index <= 500]
# преобразование в кортеж для ускорения решения

# msb = list(zip(    metro_station_base['Longitude_WGS84'],
#                     metro_station_base['Latitude_WGS84'],
#                     metro_station_base['Name'],
#                     metro_station_base['NameOfStation'],
#                 )
#               )
#
# bsb = list(zip(    bus_stop_base['Longitude_WGS84'],
#                     bus_stop_base['Latitude_WGS84'], )
#               )


def distance(coord_1, coord_2):

    r_earth = 6371000

    long_1 = coord_1[0]*np.pi/180
    lati_1 = coord_1[1]*np.pi/180

    long_2 = coord_2[0]*np.pi/180
    lati_2 = coord_2[1]*np.pi/180

    d_x = np.sin(long_1 - long_2)
    d_y = np.sin(lati_1 - lati_2)

    # точная оценка
    d_rad = np.arccos( np.sin(long_1) * np.sin(long_2)
        + np.cos(long_1) * np.cos(long_2) * np.cos(lati_1 - lati_2))

    # грубая оценка
    # d_rad = (d_x ** 2 + d_y ** 2) ** 0.5

    return d_rad*r_earth


print(distance((55.6864963, 37.856904), (55.6842382, 37.8542378)))


def close_plus(d, dots, rad):
    '''
    функция возвращает 1 если точка находится ближе чем rad хотя бы к одной из точеу dots, иначе 0
    '''

    answ = False

    for dot in dots:
        cond = (dot[0]- d[0])**2 + (dot[1]- d[1])**2 < rad **2
        answ = int(answ or cond)

    return int(answ)

metro_stationa_chosen = {}

def main_calc(msb_s, bsb_s):

    closer_than = 500  # метров

    count = 0
    print("---------- Start calculating ------------")

    for m_station in msb_s:

        coord_1 = (m_station[0], m_station[1])
        end_ = ''
        count += 1
        if count % 100 == 0: end_ = '\n'
        else: end_ = ''

        print('*', end = end_)

        for b_station in bsb_s:

            bsb_index = 0

            coord_2 = (b_station[0], b_station[1])

            # print(coord_2)

            sn = m_station[2]

            in_range = distance(coord_1, coord_2) <= closer_than

            if in_range and (sn not in metro_stationa_chosen):
                metro_stationa_chosen[sn] = 1
            elif in_range and (sn in metro_stationa_chosen):
                metro_stationa_chosen[sn] += 1

    print("---------- Finish ------------")

    pprint(metro_stationa_chosen)


# if __name__ == '__main__':
#     main_calc(msb, bsb)