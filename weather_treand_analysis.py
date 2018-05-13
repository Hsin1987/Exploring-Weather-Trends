import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from pathlib import Path

# 0. Browse all the csv file in the folder.
# 1. List all the table for city temperature data. (It means the list ignore global_data.csv)
# 2. Let the use choose input file >> Loading the File >> Plotting the line chart with city & global data.
# 3. Calculate the moving average temp.
# 3-1. Let the user choose the moving average windows
# 3-2. Calculate the moving average.
# 4. Plot the line chart for comparing the weather trend.


def plot(city_d, global_d, column, plt_name):
    plt.plot(city_d.index, city_d[column],
             color='green', marker='o', linestyle='dashed', linewidth=2, markersize=1)
    plt.plot(global_d.index, global_d[column],
             color='red', marker='X', linewidth=2, markersize=1)
    plt.title('Temp. Trend: Regional v.s Global ')
    plt.xlabel('YEAR')
    plt.ylabel('Temperature (ºC) ')
    plt.savefig(plt_name + '.png')
    plt.close()
    return


def subplot(city_d, global_d, column, plt_name):
    plt.suptitle(plt_name, fontsize=16)
    plt.subplot(211)
    plt.plot(city_d.index, city_d[column],
             color='green', marker='o', linestyle='dashed', linewidth=2, markersize=1)
    plt.xlabel('YEAR')
    plt.ylabel('Temperature (ºC) ')

    plt.subplot(212)
    plt.plot(global_d.index, global_d[column],
             color='red', marker='X', linewidth=2, markersize=1)
    plt.xlabel('YEAR')
    plt.ylabel('Temperature (ºC) ')
    plt.subplots_adjust(left=0.2, wspace=0.8, top=0.9)
    plt.savefig(plt_name + '_sub.png')
    plt.close()
    return


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
key_input = input("Choose the city by its index:")
#key_input = 0 # Taipei
city_data = pd.read_csv(list_city[int(key_input)]).set_index('year')

global_comparision = global_data.loc[city_data.index]

# 2-1. plot the original data.
plot(city_data, global_comparision, 'avg_temp', 'Annual_Average_Temp_Comparison')
subplot(city_data, global_comparision, 'avg_temp', 'Annual_Average_Temp_Comparison')


# 3. Calculate the moving average temp.
city_data['MA'] = city_data['avg_temp'].rolling(window=20).mean()
global_comparision['MA'] = global_comparision['avg_temp'].rolling(window=20).mean()
plot(city_data, global_comparision, 'MA', 'Moving_Average_Temp_Comparison')
subplot(city_data, global_comparision, 'MA', 'Moving_Average_Temp_Comparison')

# Correlation
matplotlib.style.use('ggplot')
plt.scatter(city_data['MA'], global_comparision['MA'])
plt.xlabel('Taipei_MS(ºC)')
plt.ylabel('Global_MS (ºC) ')
plt.title('Correlation', fontsize=16)
plt.savefig('Correlation.png')
plt.show()
plt.close()
print('Correlation: ', city_data['MA'].corr(global_comparision['MA']))
