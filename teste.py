import numpy as np
import matplotlib.pyplot as plt

# Definindo o intervalo de valores
x = np.linspace(-2.5, 2.5, 400)

# Definindo as funções
def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

# Função para plotar uma função de ativação
def plot_function(func, x, title):
    plt.figure(figsize=(8, 5))
    plt.plot(x, func(x), label=title)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.grid()
    plt.legend()
    plt.show()

# Plotando as funções uma por uma
plot_function(relu, x, 'ReLU')
plot_function(sigmoid, x, 'Sigmoid')
plot_function(tanh, x, 'tanh')
