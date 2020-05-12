import numpy as np
import matplotlib.pyplot as plt

population = np.zeros((100, 100))
beta = 0.3
gamma = 0.05

outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1



plt.figure(figsize = (6, 4), dpi = 150)
plt.imshow(population, cmap='plasma', interpolation = 'nearest')
plt.show()

for time in range(1, 101):
    populationResult = np.where(population == 1, np.random.choice(range(1,3), 1, p=[1-gamma, gamma])[0], population)
    infectedIndex = np.where(population==1)
    for i in range(len(infectedIndex[0])):
        row = infectedIndex[0][i]
        column = infectedIndex[1][i]
        for rowNeighbour in range(row-1, row+2):
            for columnNeighbour in range(column-1, column+2):
                if rowNeighbour != -1 and columnNeighbour != -1 and rowNeighbour != 100 and columnNeighbour != 100:
                    if population[rowNeighbour][columnNeighbour] == 0:
                        populationResult[rowNeighbour,columnNeighbour] = np.random.choice(range(2), 1, p=[1-beta, beta])[0]
    population = populationResult
    if time in [10, 50, 100]:
        plt.figure(figsize = (6, 4), dpi = 150)
        plt.imshow(populationResult, cmap='plasma', interpolation = 'nearest')
        plt.show()
        print(1 in population)
        print(2 in population)