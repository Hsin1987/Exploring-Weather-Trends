import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 0. Browse all the csv file in the folder.
# 1. List all the table for city temperature data. (It means the list ignore global_data.csv)
# 2. Let the use choose input file >> Loading the File >> Plotting the line chart with city & global data.
# 3. Calcuate the moving average temp.
# 3-1. Let the user choose the moving average windows
# 3-2. Calculate the moving average.
# 4. Plot the line chart for comparing the weather trend.


# 0. Browse all the csv file in the folder.
p = Path('.')
list_city = list(p.glob('**/*.csv'))
i = 0
for item in list_city:
    if 'global' in item.name:
        global_data = pd.read_csv(list_city.pop(i).name).set_index('year')
    i += 1         

# 1. List all the table for city temperature data.
print("List of City:")
i = 0
for city in list_city:
    print("    " + str(i) + ":  " + city.name)
    i += 1

# 2. Let the use choose input file >> Loading the File >> Plotting the line chart with city & global data.
#key_input = input("Choose the city by its index:")
key_input = 0 # Taipei
city_data = pd.read_csv(list_city[int(key_input)]).set_index('year')

global_comparision = global_data.loc[city_data.index]

# 2-1. plot the original data.
plt.plot(city_data.index, city_data['avg_temp'],
         color='green', marker='o', linestyle='dashed', linewidth=2, markersize=1)
plt.plot(global_comparision.index,  global_comparision['avg_temp'],
         color='red', marker='X', linewidth=2, markersize=1)
plt.title('Temp. Trend: Regional v.s Golbal ')
plt.xlabel('YEAR')
plt.ylabel('Temperature (ºC) ')
plt.show()

