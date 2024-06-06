import numpy as np


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

print("Koefisien Beda Terbagi:", coef)

x_interp = 27  
y_interp = polinom_newton(coef, x, x_interp)
print(f"Nilai interpolasi pada x = {x_interp}: y = {y_interp}")

def interpolasi(x_titik, y_titik, x_interp):
    coef = beda_terbagi(x_titik, y_titik)
    return polinom_newton(coef, x_titik, x_interp)

x_titik_interp = [17, 19, 23] 
y_titik_interp = [interpolasi(x, y, xi) for xi in x_titik_interp]
for xi, yi in zip(x_titik_interp, y_titik_interp):
    print(f"Nilai interpolasi pada x = {xi}: y = {yi}")
