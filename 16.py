import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

POPULATION_RANGE = 1_000_000_000
POPULATION_SIZE = 1_000_000
NSAMPLES = 10000
SAMPLE_SIZE = 50

population = np.random.randint(0, POPULATION_RANGE, POPULATION_SIZE)
samples = np.random.choice(population, (NSAMPLES, SAMPLE_SIZE))

population_mean = np.mean(population)
samples_means = np.mean(samples, axis=1)
samples_means_mean = np.mean(samples_means)

plt.hist(samples_means, bins=50)

plt.show()

print(f'Anakütle ortalaması: {population_mean}')
print(f'Örnek ortalamalarının Ortalaması: {samples_means_mean}')