import matplotlib.pyplot as plt


def f(x):
    return x**2 - 4

def bissecao(f, a, b, tol):
    seq_aprox = []
    if f(a) * f(b) > 0:
        return None
    
    while abs(b - a) > tol:
        c = (a + b) / 2
        seq_aprox.append(c)
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return seq_aprox

def linspace(a, b, n):
    delta = (b - a) / (n - 1)
    return [a + i * delta for i in range(n)]

def Solve():
    x_values = linspace(0, 10, 100)
    y_values = [f(x) for x in x_values]

    a = 0
    b = 10
    tol = 1e-6
    seq_aprox = bissecao(f, a, b, tol)
    
    plt.plot(x_values, y_values, label='f(x)')
    plt.scatter(seq_aprox, [f(x) for x in seq_aprox], c=range(len(seq_aprox)), cmap='viridis', label='Sequência de Aproximações')
    plt.colorbar(label="Indice da Sequência")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico de y = f(x) com Sequência de Aproximações')
    plt.legend()
    plt.show()
    
Solve()
