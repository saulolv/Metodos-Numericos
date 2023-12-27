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


def Solve(f, df, intervalo, alternative):
    a, b = intervalo
    tol = 1e-4

    min_iterations_bissecao = len(MetodoBissecao(f, a, b, tol))
    min_iterations_newton = len(MetodoNewton(f, df, (a + b) / 2, tol))
    print(f"Para a função {alternative}: O método da bisseção convergiu ou chegou no limite de interações em: {min_iterations_bissecao} iterações.")
    print(f"Para a função {alternative}: O método de Newton convergiu em ou chegou no limite de interações em: {min_iterations_newton} iterações.\n")

def main():
    Solve(f_a, df_a, (0, 1), "A")
    Solve(f_b, df_b, (0, 0.5), "B")
    Solve(f_c, df_c, (-3, -2), "C")
    Solve(f_d, df_d, (3, 5), "D")
    
main()