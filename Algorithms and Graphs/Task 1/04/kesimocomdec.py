import time
import random
import matplotlib.pyplot as plt

def generate_random_vectors(size):
    return sorted(random.sample(range(1, 200000), size)), sorted(random.sample(range(1, 200000), size))

def achar_kesimo(X, Y, k):
    def kesimomenor(A, B, k):
        ladoA, ladoB = len(A), len(B)
        
        # Garantir que A é sempre o menor dos dois vetores
        if ladoA > ladoB:
            return kesimomenor(B, A, k)
        
        # Casos base
        if ladoA == 0:
            return B[k-1]
        if k == 1:
            return min(A[0], B[0])
        
        # Dividir k em duas partes
        i = min(ladoA, k // 2)
        j = min(ladoB, k // 2)
        
        if A[i-1] > B[j-1]:
            # Descartar a primeira parte de B
            return kesimomenor(A, B[j:], k - j)
        else:
            # Descartar a primeira parte de A
            return kesimomenor(A[i:], B, k - i)
    
    return kesimomenor(X, Y, k)

# Gerar tamanhos crescentes para os vetores
tamanhos = [100, 1000, 5000, 12500, 15000, 17500, 20000]
vezes = []

for size in tamanhos:
    X, Y = generate_random_vectors(size)
    start_time = time.time()
    achar_kesimo(X, Y, 7)  # k = 7 apenas para manter consistência nos testes
    end_time = time.time()
    vezes.append(end_time - start_time)

# Plotar o gráfico
plt.plot(tamanhos, vezes, marker='o')
plt.xlabel('Tamanho das Entradas')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Relação entre Tamanho das Entradas e Tempo de Execução')
plt.grid(True)
plt.show()
