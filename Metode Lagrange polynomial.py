import numpy as np
import matplotlib.pyplot as plt

#Data
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Function 
def lagrange_polynomial(x_values, y_values, x):
    n = len(x_values)
    polynomial = 0
    for i in range(n):
        product = y_values[i]
        for j in range(n):
            if j != i:
                product *= (x - x_values[j]) / (x_values[i] - x_values[j])
        polynomial += product
    return polynomial

# Interpolate for 5 <= x <= 40
x_interpolate = np.linspace(5, 40, 100)
y_interpolate = np.zeros(len(x_interpolate))
for i in range(len(x_interpolate)):
    y_interpolate[i] = lagrange_polynomial(x, y, x_interpolate[i])

# Plot the interpolated data
plt.plot(x_interpolate, y_interpolate, color='Pink', label='Interpolated Data')
plt.scatter(x, y, color='Green', label='Given Data')
plt.xlabel('Tegangan (kg/mm²)')
plt.ylabel('Waktu Patah (jam)')
plt.title('Grafik Lagrange Polynomial Interpolation')
plt.legend()
plt.box(False)
plt.grid(False)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()