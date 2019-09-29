#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import json
from scipy.io import netcdf

with netcdf.netcdf_file('MSR-2.nc', mmap=False) as netcdf_file:
    variables = netcdf_file.variables
print(*variables, sep=', ')
print(variables['time'].dimensions)
print(variables['Average_O3_column'].dimensions)
print(variables['time'].units, variables['Average_O3_column'].units)
Dushanbelong = 68.75
Dushanbelat = 38.57
a = np.searchsorted(variables['longitude'].data, Dushanbelong, sorter=None)#Вычисляем узел сетки с похожими коориданатми
b = np.searchsorted(variables['latitude'].data, Dushanbelat, sorter=None)
plt.plot(variables['time'][:], variables['Average_O3_column'][:, b, a], label = 'All data', color='grey')#рисуем график зависимости озона от времени
plt.plot(variables['time'][::12], variables['Average_O3_column'][::12, b, a], label = 'January', color='orange')#для января
plt.plot(variables['time'][6::12], variables['Average_O3_column'][6::12, b, a], label = 'July', color='purple')
plt.xlabel("Months since 1970-01-15")
plt.ylabel('Dobson units')
plt.grid()
plt.legend()
plt.suptitle('Monthly average data 1979-2018')
plt.savefig('ozon.png')
plt.show()
minall=min(variables['Average_O3_column'][:, b, a])#вычисляем минимальные/максимальные/средние значения для данных за весь период, январь и июль
avgall=np.mean(variables['Average_O3_column'][:, b, a])
maxall=max(variables['Average_O3_column'][:, b, a])
minjan=min(variables['Average_O3_column'][::12, b, a])
avgjan=np.mean(variables['Average_O3_column'][::12, b, a])
maxjan=max(variables['Average_O3_column'][::12, b, a])
minjul=min(variables['Average_O3_column'][6::12, b, a])
avgjul=np.mean(variables['Average_O3_column'][6::12, b, a])
maxjul=max(variables['Average_O3_column'][6::12, b, a])

data={"city": "Dushanbe",
    "coordinates": [68.75, 38.57],
    "jan": {
        "min": str(minjan),
        "max": str(maxjan),
        "mean": str(avgjan)
    },
    "jul": {
        "min": str(minjul),
        "max": str(maxjul),
        "mean": str(avgjul)
    },
    "all": {
        "min": str(minall),
        "max": str(maxall),
        "mean": str(avgall)
    }}
with open("ozon.json", "w") as f:#записываем в файл
    json.dump(data, f, indent=2) #indent=2 делается исключительно для визуально удобного представления данных в ozon.json, вообще говоря, это не требуется и усложняет работу с файлом
