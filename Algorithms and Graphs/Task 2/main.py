from time import perf_counter

from bruteforce import algoritmo_tsp_forca_bruta
from nearest_neighbor import algoritmo_tsp_vizinho_mais_proximo
from backtracking import algoritmo_tsp_backtracking

### n = 5
n = 5  # número de cidades
D = [
    [0, 10, 15, 20, 10],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 15],
    [10, 30, 20, 15, 0]
]  # matriz de distâncias
L = 100  # limite de distância

## Força bruta
start_time_bruteforce = perf_counter()
bruteforce, bruteforce_route = algoritmo_tsp_forca_bruta(n, D, L)
end_time_bruteforce = perf_counter()

bruteforce_elapsed_time = end_time_bruteforce - start_time_bruteforce

print("Tempo de execução: ", bruteforce_elapsed_time)

## Vizinho mais próximo
start_time_nearest_neighbor = perf_counter()
nearest_neighbor, nearest_neighbor_route = algoritmo_tsp_vizinho_mais_proximo(n, D, L)
end_time_nearest_neighbor = perf_counter()

nearest_neighbor_elapsed_time = end_time_nearest_neighbor - start_time_nearest_neighbor

print("Tempo de execução: ", nearest_neighbor_elapsed_time)

## Backtracking
start_time_backtracking = perf_counter()
backtracking, backtracking_route = algoritmo_tsp_backtracking(D, L)
end_time_backtracking = perf_counter()

backtracking_elapsed_time = end_time_backtracking - start_time_backtracking

print("Tempo de execução: ", backtracking_elapsed_time)

## Resultados
timers = [bruteforce_elapsed_time, nearest_neighbor_elapsed_time, backtracking_elapsed_time]
print("Algoritmo mais rápido: ", timers.index(min(timers)))

### n = 10
n = 10  # número de cidades
D = [
    [0, 78, 50, 64, 85, 71, 18, 70, 14, 78],
    [78, 0, 82, 88, 17, 67, 28, 78, 66, 80],
    [50, 82, 0, 12, 83, 25, 83, 71, 88, 26],
    [64, 88, 12, 0, 99, 19, 69, 49, 83, 73],
    [85, 17, 83, 99, 0, 89, 79, 96, 58, 29],
    [71, 67, 25, 19, 89, 0, 24, 53, 67, 51],
    [18, 28, 83, 69, 79, 24, 0, 53, 56, 67],
    [70, 78, 71, 49, 96, 53, 53, 0, 11, 73],
    [14, 66, 88, 83, 58, 67, 56, 11, 0, 16],
    [78, 80, 26, 73, 29, 51, 67, 73, 16, 0]
]  # matriz de distâncias
L = 100  # limite de distância

## Força bruta
start_time_bruteforce = perf_counter()
bruteforce, bruteforce_route = algoritmo_tsp_forca_bruta(n, D, L)
end_time_bruteforce = perf_counter()

bruteforce_elapsed_time = end_time_bruteforce - start_time_bruteforce

print("Tempo de execução: ", bruteforce_elapsed_time)

## Vizinho mais próximo
start_time_nearest_neighbor = perf_counter()
nearest_neighbor, nearest_neighbor_route = algoritmo_tsp_vizinho_mais_proximo(n, D, L)
end_time_nearest_neighbor = perf_counter()

nearest_neighbor_elapsed_time = end_time_nearest_neighbor - start_time_nearest_neighbor

print("Tempo de execução: ", nearest_neighbor_elapsed_time)

## Backtracking
start_time_backtracking = perf_counter()
backtracking, backtracking_route = algoritmo_tsp_backtracking(D, L)
end_time_backtracking = perf_counter()

backtracking_elapsed_time = end_time_backtracking - start_time_backtracking

print("Tempo de execução: ", backtracking_elapsed_time)

## Resultados
timers = [bruteforce_elapsed_time, nearest_neighbor_elapsed_time, backtracking_elapsed_time]
print("Algoritmo mais rápido: ", timers.index(min(timers)))

### n = 15

n = 15  # número de cidades
D = [
    [0, 57, 22, 77, 56, 80, 69, 24, 95, 92, 63, 17, 19, 73, 95],
    [57, 0, 98, 14, 28, 72, 34, 43, 12, 47, 77, 64, 61, 73, 30],
    [22, 98, 0, 88, 22, 21, 61, 69, 31, 35, 81, 29, 19, 12, 48],
    [77, 14, 88, 0, 28, 24, 55, 99, 77, 34, 57, 18, 40, 89, 69],
    [56, 28, 22, 28, 0, 77, 74, 67, 12, 85, 64, 21, 59, 42, 85],
    [80, 72, 21, 24, 77, 0, 44, 50, 82, 25, 90, 20, 61, 84, 29],
    [69, 34, 61, 55, 74, 44, 0, 34, 77, 33, 10, 38, 67, 56, 94],
    [24, 43, 69, 99, 67, 50, 34, 0, 23, 70, 12, 83, 53, 21, 31],
    [95, 12, 31, 77, 12, 82, 77, 23, 0, 56, 67, 60, 34, 43, 10],
    [92, 47, 35, 34, 85, 25, 33, 70, 56, 0, 64, 49, 83, 92, 26],
    [63, 77, 81, 57, 64, 90, 10, 12, 67, 64, 0, 33, 40, 44, 53],
    [17, 64, 29, 18, 21, 20, 38, 83, 60, 49, 33, 0, 68, 74, 89],
    [19, 61, 19, 40, 59, 61, 67, 53, 34, 83, 40, 68, 0, 58, 70],
    [73, 73, 12, 89, 42, 84, 56, 21, 43, 92, 44, 74, 58, 0, 26],
    [95, 30, 48, 69, 85, 29, 94, 31, 10, 26, 53, 89, 70, 26, 0]

]  # matriz de distâncias
L = 10000  # limite de distância

## Força bruta
start_time_bruteforce = perf_counter()
bruteforce, bruteforce_route = algoritmo_tsp_forca_bruta(n, D, L)
end_time_bruteforce = perf_counter()

bruteforce_elapsed_time = end_time_bruteforce - start_time_bruteforce

print("Tempo de execução: ", bruteforce_elapsed_time)

## Vizinho mais próximo
start_time_nearest_neighbor = perf_counter()
nearest_neighbor, nearest_neighbor_route = algoritmo_tsp_vizinho_mais_proximo(n, D, L)
end_time_nearest_neighbor = perf_counter()

nearest_neighbor_elapsed_time = end_time_nearest_neighbor - start_time_nearest_neighbor

print("Tempo de execução: ", nearest_neighbor_elapsed_time)

## Backtracking
start_time_backtracking = perf_counter()
backtracking, backtracking_route = algoritmo_tsp_backtracking(D, L)
end_time_backtracking = perf_counter()

backtracking_elapsed_time = end_time_backtracking - start_time_backtracking

print("Tempo de execução: ", backtracking_elapsed_time)

## Resultados
timers = [bruteforce_elapsed_time, nearest_neighbor_elapsed_time, backtracking_elapsed_time]
print("Algoritmo mais rápido: ", timers.index(min(timers)))
