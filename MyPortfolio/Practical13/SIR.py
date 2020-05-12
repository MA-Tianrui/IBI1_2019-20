import numpy as np
import matplotlib.pyplot as plt

# define basic variables
susceptibleRecord = [9999]
infectedRecord = [1]
recoveredRecord = [0]

susceptible = 9999
infected = 1
recovered = 0
total = 10000
beta = 0.3
gamma = 0.05

# loop over 1000 time points

for timePoint in range(1, 1001):
# new infected from susceptible
    newInfected = np.random.choice(range(2), susceptible, p = [1 - beta*infected/total, beta*infected/total])
# new recovered from infected
    newRecovered = np.random.choice(range(2), infected, p = [1 - gamma, gamma])
    newInfectedNum = newInfected.sum()
    newRecoveredNum = newRecovered.sum()
# count the number of three groups at the end of this time point
    susceptible = susceptible - newInfectedNum
    infected = infected + newInfectedNum - newRecoveredNum
    recovered = recovered + newRecoveredNum
# record the number of three groups
    susceptibleRecord.append(susceptible)
    infectedRecord.append(infected)
    recoveredRecord.append(recovered)

# draw the plot
susceptibleArray = np.array(susceptibleRecord)
infectedArray = np.array(infectedRecord)
recoveredArray = np.array(recoveredRecord)
timeArray = np.array(range(0, 1001))

plt.figure(figsize = (6, 4), dpi = 150)
plt.plot(timeArray, susceptibleArray, label = 'susceptible')
plt.plot(timeArray, infectedArray, label = 'infected')
plt.plot(timeArray, recoveredArray, label = 'recovered')

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()

plt.show()