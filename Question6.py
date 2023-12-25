def f(x):
    return x**3 - 9*x + 3

def df(x):
    return 3*x**2 - 9

def MetodoBissecao(f, a, b, tolerance=1e-6, max_iterations=100):
    if f(a) * f(b) > 0:
        return None
    
    previous_midpoint = None

    while max_iterations > 0:
        midpoint = (a + b) / 2
        if f(midpoint) == 0 or (previous_midpoint is not None and abs(midpoint - previous_midpoint) < tolerance):
            return midpoint  # Encontrou uma raiz exata ou convergiu
        elif f(midpoint) * f(a) < 0:
            b = midpoint
        else:
            a = midpoint

        previous_midpoint = midpoint
        max_iterations -= 1

    return (a + b) / 2

    
def MetodoNewton(f, df, x0, tolerance=1e-6, max_iterations=100):
    x = x0
    previous_x = None
    
    while max_iterations > 0:
        x = x - f(x) / df(x)

        if previous_x is not None and abs(x - previous_x) < tolerance:
            return x  # Convergiu
        elif abs(f(x)) < tolerance:
            return x  # Encontrou uma raiz exata

        previous_x = x
        max_iterations -= 1
    
    return x

def main():
    resultado_bissecao = MetodoBissecao(f, 0, 1)
    print(f'Raiz encontrada pelo método da bisseção: {resultado_bissecao}')
    resultado_newton = MetodoNewton(f, df, 0.5)
    print(f'Raiz encontrada pelo método de Newton: {resultado_newton}')
    
if __name__ == '__main__':
    main()