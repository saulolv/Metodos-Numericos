import matplotlib.pyplot as plt
import math as m

def f_a(x):
    return x - 2**(-x)

def df_a(x):
    return (2**(x) + m.log(2)) / 2**(x)

def f_b(x):
    return x + 1 - 2 * m.sin(m.pi * x)

def df_b(x):
    return 1 - 2 * m.pi * m.cos(m.pi * x)

def f_c(x):
    return 2 * x * m.cos(2 * x) - (x + 1)**2

def df_c(x):
    return 2 * m.cos(2 * x) - 4 * x * m.sin(2 * x) - 2 * x - 2

def f_d(x):
    return m.log(abs(x)) - 2**x + x**2

def df_d(x):
    return (1/x) - (m.log(2) * (2)**x) + 2 * x

def MetodoBissecao(f, a, b, tolerance=1e-6, max_iterations=100):
    
    seq_aprox = []
    
    if f(a) * f(b) > 0:
        return []

    while max_iterations > 0:
        midpoint = (a + b) / 2
        seq_aprox.append(midpoint)
        if f(midpoint) == 0 or midpoint < tolerance:
            break  # Encontrou uma raiz exata ou convergiu
        elif f(midpoint) * f(a) < 0:
            b = midpoint
        else:
            a = midpoint

        max_iterations -= 1

    return seq_aprox

def MetodoNewton(f, df, x0, tolerance=1e-6, max_iterations=100):
    
    seq_aprox = []
    x = x0
    
    while max_iterations > 0:
        x = x - f(x) / df(x)
        seq_aprox.append(x)

        if abs(x - x0) < tolerance or abs(f(x)) < tolerance:
            break  # Convergiu
        elif abs(f(x)) < tolerance:
            break  # Encontrou uma raiz exata

        max_iterations -= 1
    
    return seq_aprox

def linspace(a, b, n):
    return [a + i * (b - a) / n for i in range(n + 1)]


def Solve(f, df, intervalo):
    a, b = intervalo
    tol = 1e-6
    
    seq_aprox_bissecao = MetodoBissecao(f, a, b, tol)
    seq_aprox_newton = MetodoNewton(f, df, (a + b) / 2, tol)
    
    x_values = linspace(a, b, 100)
    y_values = [f(x) for x in x_values]
    
    # Plotar para o Método da Bisseção
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)  # Subplot 1 (1 linha, 2 colunas, primeiro subplot)
    plt.plot(x_values, y_values, label='f(x)')
    plt.scatter(seq_aprox_bissecao, [f(x) for x in seq_aprox_bissecao], c=range(len(seq_aprox_bissecao)), cmap='viridis', label='Bisseção')
    plt.colorbar(label="Índice da Sequência")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Bisseção')
    plt.legend()

    # Plotar para o Método de Newton
    plt.subplot(1, 2, 2)  # Subplot 2 (1 linha, 2 colunas, segundo subplot)
    plt.plot(x_values, y_values, label='f(x)')
    plt.scatter(seq_aprox_newton, [f(x) for x in seq_aprox_newton], c=range(len(seq_aprox_newton)), cmap='viridis', label='Newton')
    plt.colorbar(label="Índice da Sequência")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Newton')
    plt.legend()

    plt.tight_layout()  # Ajusta a layout para evitar sobreposição
    plt.show()
    

def main():
    Solve(f_a, df_a, (0, 1))
    Solve(f_b, df_b, (0, 0.5))
    Solve(f_c, df_c, (-3, -2))
    Solve(f_d, df_d, (3, 5))
    
main()