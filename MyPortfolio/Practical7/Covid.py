import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# you can use following code to find the csv file, 
# but I have put the file here (beside the py file) and you can read it directly
#os.chdir('C:\cygwin64\home\90951\IBI')

# read the csv file
covid_data = pd.read_csv('full_data.csv')



# task a, showing all rows, and every third column between (and including) 0 and 15 row
aTask = covid_data.iloc[0:16, 2]
print(aTask)



# define a function used in following task
def FindRow(location):
    """
    input: location, a string
    return: a list with booleans, row of the loction showed by True, other by False
    """
    row = []
    for i in range(0, len(covid_data.iloc[:, 2])):
        location0 = covid_data.iloc[i, 1]  # only get the location column
        if location0 == location:  # check if we want each location
            row.append(True)
        else:
            row.append(False)
    
    return(row)



# task b, used a Boolean to show "total cases" for all rows corresponding to Afghanistan
# find rows in Afghanistan
afghanRow = FindRow('Afghanistan')
bTask = covid_data.loc[afghanRow, 'total_cases']
print('Total cases in Afghanistan:')
print(bTask)



# task c
# 1.compute the mean and median of new cases for the entire world
# 2.create a boxplot of new cases worldwide
# 3.plot both new cases and new deaths worldwide
worldRow = FindRow('World')
world_data = covid_data.loc[worldRow, :]

# change type
arrayWorldNewCases = np.array(world_data.loc[:, 'new_cases'])
arrayWorldNewDeaths = np.array(world_data.loc[:, 'new_deaths'])
arrayWorldDate = np.array(world_data.loc[:, 'date'])

# 1.compute the mean and median of new cases for the entire world
worldMean = np.mean(arrayWorldNewCases)
worldMedian = np.median(arrayWorldNewCases)
print('The mean of new cases for the entire world:', worldMean)
print('The median of new cases for the entire world:', worldMedian)

# 2.create a boxplot of new cases worldwide
plt.boxplot(arrayWorldNewCases, 
            patch_artist = True, 
            showmeans = True, 
            meanline = True)  # I show mean line, so you can see the green mean line
plt.title('New cases worldwide')
plt.ylabel('number')
plt.show()

# 3.plot both new cases and new deaths worldwide
plt.plot(arrayWorldDate, arrayWorldNewCases, '+', label = 'new cases')  # '+' denote the shape of point
plt.plot(arrayWorldDate, arrayWorldNewDeaths, '+', label = 'new deaths')

# set scales in x
# [0:len(arrayWorldDate):4] set that the interval of dates = 4
plt.xticks(arrayWorldDate[0:len(arrayWorldDate):4], rotation = 270)  # rotation make the x-label erect
plt.xlabel('date')
plt.ylabel('number')
plt.title('New cases and new deaths worldwide developing over time')
plt.legend()
plt.show()



# answer for my question.txt
for state in ['South Korea', 'Iran']:  # for loop help me draw two plots, instead of use the similar code twice
    stateRow = FindRow(state)
    arrayNewCases = np.array(covid_data.loc[stateRow, 'new_cases'])
    arrayDate = np.array(covid_data.loc[stateRow, 'date'])
    plt.plot(arrayWorldDate, arrayNewCases, '+', label = 'new cases in ' + state)  # '+' denote the shape of point

# set scales in x
# [0:len(arrayWorldDate):4] set that the interval of dates = 4
plt.xticks(arrayDate[0:len(arrayDate):4], rotation = 270)  # rotation make the x-label erect
plt.xlabel('date')
plt.ylabel('number')
plt.title('New cases developing over time in South Korea and Iran')
plt.legend()
plt.show()