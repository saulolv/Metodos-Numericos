def find_smallest_n():
    n = 0
    resultado = 1.0 + 2**(-n)
    while resultado > 1.0:
        n += 1
        resultado = 1 + 2**(-n)
    return n

def main():
    print(f'O menor n que satisfaz 1 + 2**(-n) = 1 é {find_smallest_n()}')
    
if __name__ == '__main__':
    main()