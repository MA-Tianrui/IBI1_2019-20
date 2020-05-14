import numpy as np
import matplotlib.pyplot as plt

# define basic variables
total = 10000
beta = 0.3
gamma = 0.05
plt.figure(figsize = (6, 4), dpi = 150)



for rate in range(0, 11):  # test vaccinated ratio from 0 to 100%
    recovered = 0
    vaccinated = total*rate//10  # calculate the vaccinated
    if rate == 10:
        infected = 0
        susceptible = 0
    else:
        infected = 1
        susceptible = total - vaccinated - 1
    infectedRecord = [infected]
# loop over 1000 time points
    for timePoint in range(1, 1001):
# new infected from susceptible
        newInfected = np.random.choice(range(2), susceptible, p = [1 - beta*infected/total, beta*infected/total])
# new recovered from infected
        newRecovered = np.random.choice(range(2), infected, p = [1 - gamma, gamma])
# total number of new infected and recovered
        newInfectedNum = newInfected.sum()
        newRecoveredNum = newRecovered.sum()
# count the number of three groups at the end of this time point
        susceptible = susceptible - newInfectedNum
        infected = infected + newInfectedNum - newRecoveredNum
        recovered = recovered + newRecoveredNum
# record the number of infected
        infectedRecord.append(infected)
# draw the plot
    infectedArray = np.array(infectedRecord)
    timeArray = np.array(range(0, 1001))
    plt.plot(timeArray, infectedArray, label = str(rate) + '0%')

# set labels and title
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()

plt.show()