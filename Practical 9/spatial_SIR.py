import numpy as np
import matplotlib.pyplot as plt

# States
SUSCEPTIBLE = 0
INFECTED = 1
RECOVERED = 2

# Parameters
size = 100
beta = 0.3
gamma = 0.05
steps = 100

# Make population grid
population = np.zeros((size, size), dtype=int)

# Choose one random outbreak point
outbreak = np.random.choice(range(size), 2)
population[outbreak[0], outbreak[1]] = INFECTED

# Pseudocode
# 1. For each time step, find all infected cells.
# 2. For every infected cell, inspect its 8 neighbouring cells.
# 3. If a neighbour is susceptible, infect it with probability beta.
# 4. Allow the infected cell itself to recover with probability gamma.
# 5. Use a copy of the population so updates do not interfere within the same step.
# 6. Plot the grid at selected times to show spread through space and time.

def neighbours(x, y, max_size):
    coords = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < max_size and 0 <= ny < max_size:
                coords.append((nx, ny))
    return coords

plot_times = [0, 10, 50, 100]
fig, axes = plt.subplots(2, 2, figsize=(8, 8), dpi=150)
axes = axes.flatten()
plot_index = 0

if 0 in plot_times:
    axes[plot_index].imshow(population, cmap='viridis', interpolation='nearest', vmin=0, vmax=2)
    axes[plot_index].set_title('time 0')
    plot_index += 1

for t in range(1, steps + 1):
    new_population = population.copy()
    infected_positions = np.argwhere(population == INFECTED)

    for x, y in infected_positions:
        for nx, ny in neighbours(x, y, size):
            if population[nx, ny] == SUSCEPTIBLE:
                if np.random.random() < beta:
                    new_population[nx, ny] = INFECTED

        if np.random.random() < gamma:
            new_population[x, y] = RECOVERED

    population = new_population

    if t in plot_times:
        axes[plot_index].imshow(population, cmap='viridis', interpolation='nearest', vmin=0, vmax=2)
        axes[plot_index].set_title(f'time {t}')
        plot_index += 1

for ax in axes:
    ax.set_xticks([])
    ax.set_yticks([])

plt.suptitle('Spatial SIR model')
plt.tight_layout()
plt.savefig('C:/Users/ASUS/OneDrive - International Campus, Zhejiang University/桌面/大学/上课文件、手册及其分组/大一下/IBI 1/IBI1_2025-26/IBI1_2025-26/Practical 9/spatial_SIR.png')
plt.close()
