def f(x):
    return x**3 - 9*x + 3

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

def main():
    print(bissecao(f, 0, 1, 1e-6))
    
main()