import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_values, y_values, x):
    
    def basis_polynomial(i, x):
        result = 1
        for j in range(len(x_values)):
            if j != i:
                result *= (x - x_values[j]) / (x_values[i] - x_values[j])
        return result
    
    interpolation = 0
    for i in range(len(x_values)):
        interpolation += y_values[i] * basis_polynomial(i, x)
    return interpolation

x_values = [5, 10, 15, 20, 25, 30, 35, 40]
y_values = [40, 30, 25, 40, 18, 20, 22, 15]

x_range = np.linspace(5, 40, 100)
y_interpolated = [lagrange_interpolation(x_values, y_values, x) for x in x_range]

plt.plot(x_values, y_values, 'o', label='Data asli')
plt.plot(x_range, y_interpolated, '-', label='Interpolasi Lagrange')
plt.xlabel('Tegangan, x (kg/mm²)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Lagrange')
plt.legend()
plt.grid(True)
plt.show()
