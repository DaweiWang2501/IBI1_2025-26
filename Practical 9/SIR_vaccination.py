import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Basic parameters
N = 10000
beta = 0.3
gamma = 0.05
steps = 1000
vaccination_rates = list(range(0, 101, 10))

plt.figure(figsize=(6, 4), dpi=150)

for idx, vacc_percent in enumerate(vaccination_rates):
    V = int(N * vacc_percent / 100)
    S = N - V - 1
    I = 1
    R = 0

    # In case vaccination is 100%, keep one infected and no susceptible
    if S < 0:
        S = 0
        V = N - 1

    I_history = [I]

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

        new_infections = min(new_infections, S)
        new_recoveries = min(new_recoveries, I)

        S -= new_infections
        I += new_infections - new_recoveries
        R += new_recoveries

        I_history.append(I)

    color_position = idx / max(1, len(vaccination_rates) - 1)
    plt.plot(I_history, color=cm.viridis(color_position), label=f"{vacc_percent}%")

plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model with different vaccination rates")
plt.legend()
plt.tight_layout()
plt.savefig("C:/Users/ASUS/OneDrive - International Campus, Zhejiang University/桌面/大学/上课文件、手册及其分组/大一下/IBI 1/IBI1_2025-26/IBI1_2025-26/Practical 9/SIR_vaccination.png")
plt.close()
