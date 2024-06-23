def phi(x: float, a: float, b: float, c: float) -> float:
    return (a * x**2 + b * x + c)

def Q_squared(x_coord: list[float], y_coord: list[float], y_sigma: list[float], a: float, b: float, c: float):
    
    sum: float = 0.0

    for i in range(len(x_coord)):
        sum += ((y_coord[i] - phi(x_coord[i], a , b, c)) / y_sigma[i])**2

    return sum