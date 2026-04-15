import numpy as np
import matplotlib.pyplot as plt

# Basic parameters
N = 10000
beta = 0.3
gamma = 0.05
steps = 1000

# Initial conditions
S = N - 1
I = 1
R = 0

# Track values over time
S_history = [S]
I_history = [I]
R_history = [R]

# Pseudocode
# 1. For each time step:
# 2.   For every susceptible person, decide whether they become infected.
#      Infection probability = beta * (I / N).
# 3.   For every infected person, decide whether they recover.
#      Recovery probability = gamma.
# 4.   Update S, I, and R.
# 5.   Save the updated values.
for _ in range(steps):
    infection_prob = beta * (I / N)
    infection_prob = min(max(infection_prob, 0), 1)

    if S > 0:
        new_infections = np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob]).sum()
    else:
        new_infections = 0

    if I > 0:
        new_recoveries = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma]).sum()
    else:
        new_recoveries = 0

    # Guard against impossible values
    new_infections = min(new_infections, S)
    new_recoveries = min(new_recoveries, I)

    S -= new_infections
    I += new_infections - new_recoveries
    R += new_recoveries

    S_history.append(S)
    I_history.append(I)
    R_history.append(R)

plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_history, label="susceptible")
plt.plot(I_history, label="infected")
plt.plot(R_history, label="recovered")
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.legend()
plt.tight_layout()
plt.savefig("C:/Users/ASUS/OneDrive - International Campus, Zhejiang University/桌面/大学/上课文件、手册及其分组/大一下/IBI 1/IBI1_2025-26/IBI1_2025-26/Practical 9/SIR.png")
plt.close()
