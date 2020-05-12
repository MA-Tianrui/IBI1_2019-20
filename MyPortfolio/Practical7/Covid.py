import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir('C:\cygwin64\home\90951\IBI')
covid_data = pd.read_csv('full_data.csv')

# task a, showing all rows, and every third column between (and including) 0 and 15
aTask = covid_data.iloc[0:16, 2]
print(aTask)

# define a function used in following task
def FindRow(location):
    
    row = []
    for i in range(0, 7996):
        location0 = covid_data.iloc[i, 1]
        if location0 == location:
            row.append(True)
        else:
            row.append(False)
    
    return(row)

# task b, used a Boolean to show "total cases" for all rows corresponding to Afghanistan
afghanRow = FindRow('Afghanistan')
bTask = covid_data.loc[afghanRow, 'total_cases']
print(bTask)

# task c
# 1.compute the mean and median of new cases for the entire world
# 2.create a boxplot of new cases worldwide
# 3.plotte both new cases and new deaths worldwide
worldRow = FindRow('World')
world_data = covid_data.loc[worldRow, :]

arrayWorldNewCases = np.array(world_data.loc[:, 'new_cases'])
arrayWorldNewDeaths = np.array(world_data.loc[:, 'new_deaths'])
arrayWorldDate = np.array(world_data.loc[:, 'date'])

worldMean = np.mean(arrayWorldNewCases)
worldMedian = np.median(arrayWorldNewCases)
print('The mean of new cases for the entire world:', worldMean)
print('The median of new cases for the entire world:', worldMedian)

plt.boxplot(arrayWorldNewCases, 
            patch_artist = True, 
            showmeans = True, 
            meanline = True)
plt.title('New cases worldwide')
plt.ylabel('number')
plt.show()

plt.plot(arrayWorldDate, arrayWorldNewCases, '+', label = 'new cases')
plt.plot(arrayWorldDate, arrayWorldNewDeaths, '+', label = 'new deaths')
plt.xticks(arrayWorldDate[0:len(arrayWorldDate):4], rotation = 270)
plt.xlabel('date')
plt.ylabel('number')
plt.title('New cases and new deaths worldwide developing over time')
plt.legend()
plt.show()

# answer for question.txt
for state in ['South Korea', 'Iran']:
    stateRow = FindRow(state)
    arrayNewCases = np.array(covid_data.loc[stateRow, 'new_cases'])
    arrayDate = np.array(covid_data.loc[stateRow, 'date'])
    plt.plot(arrayWorldDate, arrayNewCases, '+', label = 'new cases in ' + state)
plt.xticks(arrayDate[0:len(arrayDate):4], rotation = 270)
plt.xlabel('date')
plt.ylabel('number')
plt.title('New cases developing over time in South Korea and Iran')
plt.legend()
plt.show()