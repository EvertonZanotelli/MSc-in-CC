import time
import matplotlib.pyplot as plt
import random

def pesquisa(marca):
    vetor = len(marca)
    numero, contador = 0, 0
    for e in marca:
        if contador == 0:
            numero = e
        contador += 1 if e == numero else -1

    contador = 0
    for e in marca:
        if e == numero:
            contador += 1

    if contador > vetor // 2:
        return numero
    return -1

# Função para gerar entradas crescentes de tamanho 1 a n
def generate_input(tamanho):
    return [random.randint(0, 4) for _ in range(tamanho)]

# Listas para armazenar os tamanhos das entradas e os tempos de execução
tamanhos = list(range(5, 100000))
vezes = []

# Medir o tempo de execução para cada tamanho de entrada
for tamanho in tamanhos:
    marca = generate_input(tamanho)
    comeco = time.time()
    pesquisa(marca)
    fim = time.time()
    vezes.append(fim - comeco)

# Plotar o gráfico
plt.plot(tamanhos, vezes, marker='o')
plt.xlabel('Tamanho da entrada')
plt.ylabel('Tempo de execução (s)')
plt.title('Tamanho da entrada x Tempo de execução')
plt.grid(True)
plt.show()
