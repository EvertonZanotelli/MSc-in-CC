import matplotlib.pyplot as plt
import time

def encontrar_i_sequencial_crescente(X, valor_desejado):

  esquerda = 0
  direita = len(X) - 1

  while esquerda <= direita:
    meio = (esquerda + direita) // 2

    if X[meio] == valor_desejado:
      return meio
    elif X[meio] < valor_desejado:
      esquerda = meio + 1
    else:
      direita = meio - 1

  return -1


def plotar_grafico_entradas_crescentes(limite_entradas):

  inicio = time.time()
  tempo_execucao = []

  for n in range(1, limite_entradas + 1):
    X = list(range(1, 21))
  
    

    for valor in range(n):
      encontrar_i_sequencial_crescente(X, 19)

    fim = time.time()
    tempo = fim - inicio
    tempo_execucao.append(tempo)

  plt.plot(range(1, limite_entradas + 1),tempo_execucao)
  plt.xlabel("Número de entradas (n)")
  plt.ylabel("Tempo de execução (s)")
  plt.title("Tempo de Execução vs. Número de Entradas")
  plt.show()

# Exemplo de uso
limite_entradas = 100000 # Ajustar o limite de entradas
plotar_grafico_entradas_crescentes(limite_entradas)
