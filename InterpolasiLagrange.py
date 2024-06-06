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

x_to_interpolate = 12 
y_interpolated = lagrange_interpolation(x_values, y_values, x_to_interpolate)

print(f"Nilai interpolasi pada x = {x_to_interpolate} adalah y = {y_interpolated}")
