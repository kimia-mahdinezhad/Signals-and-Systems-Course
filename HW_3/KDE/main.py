from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import math


def seaborn_plots():
    plot1 = plt.figure(1)
    plot1.suptitle('Seaborn X Plot')
    sns.kdeplot(x, color="red")

    plot2 = plt.figure(2)
    plot2.suptitle('Seaborn Y Plot')
    sns.kdeplot(y, color="green")


def calculate_KDE(arr):
    n = 6

    # Calculate Average
    average = 0
    for i in range(n):
        average += arr[i]
    average /= 6

    # Calculate Standard Deviation
    standard_deviation = 0
    for i in range(n):
        standard_deviation += pow(arr[i] - average, 2)
    standard_deviation /= 6
    standard_deviation = math.sqrt(standard_deviation)

    # Calculate Function
    calculated = np.array([])

    pre = 1 / (math.sqrt(2 * math.pi) * standard_deviation * n)

    for i in np.arange(-1, 5, 0.1):
        exp_val = 0
        for k in range(n):
            k_average = 0
            for j in range(k +1):
                k_average += arr[j]
            k_average /= (k + 1)

            exp_val += (np.exp((-1/2) * pow((i - k_average) / standard_deviation, 2)))
        value = pre * exp_val
        calculated = np.append(calculated, value)

    return calculated


x = np.array([1, 1.02, 2, 2, 3, 4.2])
y = np.array([1.02, 2.009, 3.001, 3, 3.01, 4.5])

seaborn_plots()

# Draw X Plot
x_plot_value = calculate_KDE(x)
plot3 = plt.figure(3)
plot3.suptitle('Calculated X Plot')
plt.plot(x_plot_value, color="red")

# Draw Y Plot
y_plot_value = calculate_KDE(y)
plot4 = plt.figure(4)
plot4.suptitle('Calculated Y Plot')
plt.plot(y_plot_value, color="green")

plt.show()
