import numpy as np
import matplotlib.pyplot as plt

def beda_terbagi(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    
    coef[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    
    return coef[0, :]  

def polinom_newton(coef, x_data, x):
    n = len(coef) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p

x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

coef = beda_terbagi(x, y)

def interpolasi(x_titik, y_titik, x_interp):
    coef = beda_terbagi(x_titik, y_titik)
    return polinom_newton(coef, x_titik, x_interp)

x_vals = np.linspace(5, 40, 500)  
y_vals = [interpolasi(x, y, xv) for xv in x_vals]  

plt.plot(x, y, 'ro', label='Data asli')  
plt.plot(x_vals, y_vals, 'b-', label='Interpolasi polinom Newton')  

plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Newton')
plt.legend()
plt.grid(True)
plt.show()
