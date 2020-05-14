import numpy as np
import matplotlib.pyplot as plt

# initial setting
population = np.zeros((100, 100))
beta = 0.3
gamma = 0.05

# choose the outbreak location
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# the figure at time = 0
plt.figure(figsize = (6, 4), dpi = 150)
plt.imshow(population, cmap='plasma', interpolation = 'nearest')
plt.title('Time = 0')
plt.show()

# loop over 1000 time points
for time in range(1, 101):
    populationResult = np.where(population == 1, np.random.choice(range(1,3), 1, p=[1-gamma, gamma])[0], population)  # choose some infected to recovered and save the result in a new copy matrix
    infectedIndex = np.where(population==1)
    for i in range(len(infectedIndex[0])):  # find the individual beside the infected
        row = infectedIndex[0][i]
        column = infectedIndex[1][i]
        for rowNeighbour in range(row-1, row+2):  # 8 individual around the infected
            for columnNeighbour in range(column-1, column+2):
                if rowNeighbour != -1 and columnNeighbour != -1 and rowNeighbour != 100 and columnNeighbour != 100:  # should not be out of bound
                    if population[rowNeighbour][columnNeighbour] == 0:
                        populationResult[rowNeighbour,columnNeighbour] = np.random.choice(range(2), 1, p=[1-beta, beta])[0]
    population = populationResult
    if time in [10, 50, 100]:  # draw the plot when time = 10, 50, 100
        plt.figure(figsize = (6, 4), dpi = 150)
        plt.imshow(populationResult, cmap='plasma', interpolation = 'nearest')
        plt.title('Time = ' + str(time))
        plt.show()
        

# blue = susceptible, red = infected, yellow = recovered
# however, when there are only infected and susceptible, blue = susceptible, yellow = infected