import pandas as pd

metro_station_base = pd.read_excel('repair_of_escalators/repair_of_escalators.xlsx', encoding = 'cp1251')
print(metro_station_base.columns)
msb = metro_station_base[['NameOfStation', 'RepairOfEscalators']].fillna(0)

p = msb.RepairOfEscalators[0]

print('*'*40)

station_rep_esc = msb[msb.RepairOfEscalators != 0]['NameOfStation']

print('Станции, на которых идет ремонт эскалатора: ', end = '')
for st in station_rep_esc:
    print(st, end = '; ')

'''
Интерестна возможность получать актульные данные через API.
На сайте есть такая возможность. Пока не реализована, не знаю как.
'''