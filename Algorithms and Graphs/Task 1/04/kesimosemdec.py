import time
import random
import matplotlib.pyplot as plt

def generate_random_vectors(size):
    return sorted(random.sample(range(1, 200000), size)), sorted(random.sample(range(1, 200000), size))

def achar_kesimo(X, Y, k):
    i, j = 0, 0
    vetord = []

    while i < len(X) and j < len(Y):
        if X[i] < Y[j]:
            vetord.append(X[i])
            i += 1
        else:
            vetord.append(Y[j])
            j += 1
    
    while i < len(X):
        vetord.append(X[i])
        i += 1
    
    while j < len(Y):
        vetord.append(Y[j])
        j += 1
    
    return vetord[k-1]

# Gerar tamanhos crescentes para os vetores
tamanhos = [100, 1000, 5000, 12500, 15000, 17500, 20000]
vezes = []

for size in tamanhos:
    X, Y = generate_random_vectors(size)
    comeco = time.time()
    achar_kesimo(X, Y, 7)  # k = 7 apenas para manter consistência nos testes
    fim = time.time()
    vezes.append(fim - comeco)

# Plotar o gráfico
plt.plot(tamanhos, vezes, marker='o')
plt.xlabel('Tamanho das Entradas')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Relação entre Tamanho das Entradas e Tempo de Execução')
plt.grid(True)
plt.show()
