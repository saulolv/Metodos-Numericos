def AbsoluteError(p, p_star):
    return p - p_star

def RelativeError(p, p_star):
    return (p - p_star) / p

def Fatorial(n):
    if n == 1:
        return 1
    return n * Fatorial(n - 1)

def main():
    valores = [
        ('a', 1, 0.9994),
        ('b', 124, 7),
        ('c', 0.0001, 22000),
        ('d', Fatorial(8), 39900),
    ]
    
    for desc, p, p_star in valores:
        print(f'Erro absoluto de {desc}: {AbsoluteError(p, p_star)}')
        print(f'Erro relativo de {desc}: {RelativeError(p, p_star)}\n')

if __name__ == '__main__':
    main()