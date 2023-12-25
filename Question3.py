def CalculateIntervalePstar(p, error):
    limite_superior = p + error * p
    limite_inferior = p - error * p
    return limite_inferior, limite_superior

def main():
    error = 10 ** -2
    valores = [
        ('a', 150),
        ('b', 900),
        ('c', 1500),
        ('d', 90),
    ]
    
    for desc, p in valores:
        limite_inferior, limite_superior = CalculateIntervalePstar(p, error)
        print(f'Intervalo de {desc}: [{limite_inferior}, {limite_superior}]')
        

if __name__ == '__main__':
    main()