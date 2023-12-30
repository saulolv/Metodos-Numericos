import matplotlib.pyplot as plt

def generate_x_values(a, b, delta):
    x_values = []
    current_x = a
    
    while current_x <= b:
        x_values.append(current_x)
        current_x += delta
        
    return x_values

def plot_function(f, a, b, delta):
    x_values = generate_x_values(a, b, delta)
    y_values = [f(x) for x in x_values]
    
    # Plota o gráfico usando segmentos de reta
    plt.plot(x_values, y_values, label='f(x)')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico de y = f(x) no intervalo [a, b]')
    plt.legend()
    
    plt.show()
    
# Exemplo de uso:
def f(x):
    return x**1/2

def main():
    plot_function(f, -10, 10, 0.001)

main()