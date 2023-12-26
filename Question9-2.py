import matplotlib.pyplot as plt
import numpy as np

def f_a(x):
    return x - 2**(-x)

def df_a(x):
    return 1 + 2**(-x) * np.log(2)

def f_b(x):
    return x + 1 - 2 * np.sin(np.pi * x)

def df_b(x):
    return 1 - 2 * np.pi * np.cos(np.pi * x)

def f_c(x):
    return 2 * x * np.cos(2 * x) - (x + 1)**2

def df_c(x):
    return 2 * (2 * x * np.sin(2 * x) + np.cos(2 * x)) - 2 * (x + 1)

def f_d(x):
    return np.log(abs(x)) - 2 * x + x**2

def df_d(x):
    return 1/x - 2 + 2 * x

def MetodoBissecao(f, a, b, tolerance=1e-6, max_iterations=100):
    
    seq_aprox = []
    
    if f(a) * f(b) > 0:
        return []
    
    previous_midpoint = None

    while max_iterations > 0:
        midpoint = (a + b) / 2
        seq_aprox.append(midpoint)
        if f(midpoint) == 0 or (previous_midpoint is not None and abs(midpoint - previous_midpoint) < tolerance):
            break  # Encontrou uma raiz exata ou convergiu
        elif f(midpoint) * f(a) < 0:
            b = midpoint
        else:
            a = midpoint

        previous_midpoint = midpoint
        max_iterations -= 1

    return seq_aprox

def MetodoNewton(f, df, x0, tolerance=1e-6, max_iterations=100):
    
    seq_aprox = []
    x = x0
    previous_x = None
    
    while max_iterations > 0:
        x = x - f(x) / df(x)
        seq_aprox.append(x)

        if previous_x is not None and abs(x - previous_x) < tolerance:
            break  # Convergiu
        elif abs(f(x)) < tolerance:
            break  # Encontrou uma raiz exata

        previous_x = x
        max_iterations -= 1
    
    return seq_aprox


def Solve(f, df, intervalo):
    a, b = intervalo
    tol = 1e-6
    
    seq_aprox_bissecao = MetodoBissecao(f, a, b, tol)
    seq_aprox_newton = MetodoNewton(f, df, (a + b) / 2, tol)
    
    x_values = np.linspace(a, b, 100)
    y_values = [f(x) for x in x_values]
    
    plt.plot(x_values, y_values, label='f(x)')
    plt.scatter(seq_aprox_bissecao, [f(x) for x in seq_aprox_bissecao], c=range(len(seq_aprox_bissecao)), cmap='viridis', label='Bisseção')
    plt.scatter(seq_aprox_newton, [f(x) for x in seq_aprox_newton], c=range(len(seq_aprox_newton)), cmap='viridis', label='Newton')
    plt.colorbar(label="Indice da Sequência")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico de y = f(x) com Sequência de Aproximações')
    plt.legend()
    plt.show()
    

def main():
    Solve(f_a, df_a, (0, 1))
    Solve(f_b, df_b, (0, 0.5))
    Solve(f_c, df_c, (-3, -2))
    Solve(f_d, df_d, (3, 5))
    
    
    
   
    
main()