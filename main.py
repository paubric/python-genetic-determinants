import numpy as np
import matplotlib.pyplot as plt

# Genetic parameters
n = 4
population_size = 100
survival_rate = 0.5
mutation_magnitude = 0.01
epochs = 20

# 1
A = [
    [4, -3, 2, 4],
    [3, 4, -1, -2],
    [6, 5, -3, 5],
    [-1, 1, -4, 9]]
"""
# 2
A = [
    [4, -3, 2, 4],
    [3, 4, -1, -2],
    [6, 5, -3, 5],
    [7, -1, 1, 6]]
"""
A = np.asarray(A)

population = np.zeros((population_size, n))
fit = np.zeros((population_size))
avg_fit_evolution = []
best_fit_evolution = []

# Initial info
print('n= ' + str(n) + '\n')
print('[*] Original matrix...\n')
print(A, '\n')

"""
# TO DO: normalize/denormalize values for faster convergence

# Normalize matrix
def normalize(A):
    max = np.max(A)
    min = np.min(A)
    delta = max - min
    A -= min
    A = np.multiply(A, 1/delta)
    print('[*] Normalizing matrix...\n')
    print(A)
    return A, min, max, delta

An, min, max, delta = normalize(A)
"""

# For every epoch
for epoch in range(0, epochs):
    print('\nEpoch: ', epoch)

    # If initial epoch, generate random population
    if (epoch == 0):
        population = np.random.randn(population_size, n)

    # Calculate individual fitness
    for i in range(0, population_size):
        scaled = np.multiply(A, population[i])
        sum = 0
        for line in scaled:
            sum += abs(np.sum(line))
        fit[i] = sum

    # Sort individuals by fitness
    population = np.asarray(sorted(population, key=lambda individual: abs(fit[np.where(population==individual)[0][0]])))
    fit = sorted(fit, key = lambda fit: abs(fit))

    # Stats
    avg = np.mean(fit)
    print('Average: ', avg, '\n')
    avg_fit_evolution.append(avg)
    best_fit_evolution.append(fit[0])

    # Crossover
    for i in range(int(population_size * survival_rate), population_size):
        population[i] = population[int(i - population_size * survival_rate)]

    # Mutation
    if (epoch < epochs - 1):
        population += mutation_magnitude * np.random.randn(population_size, n)

# Our best candidate, and the initial matrix multiplied by it
print(population[0])
print(A*population[0])

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111)
plt.title('Genetic Determinants')
plt.plot(avg_fit_evolution)
plt.plot(best_fit_evolution)
ax.set_xlabel('Generation')
ax.set_ylabel('Fitness')
plt.legend(['Average population fitness', 'Peak population fitness'])
plt.show()
