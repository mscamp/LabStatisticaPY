def phi(x: float, m: float, q: float) -> float:
    return m * x + q

def Q_squared(x_coord: list[float], y_coord: list[float], y_sigma: list[float], m: float, q: float):
    
    sum: float = 0.0

    for i in range(len(x_coord)):
        sum += ((y_coord[i] - phi(x_coord[i], m , q)) / y_sigma[i])**2

    return sum