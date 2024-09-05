from itertools import permutations


def algoritmo_tsp_forca_bruta(n, D, L):
    # Inicializa a lista de cidades excluindo a cidade inicial (0)
    cidades = list(range(1, n))
    # Gera todas as permutações possíveis das cidades
    permutacoes = permutations(cidades)

    menor_distancia = float('inf')
    melhor_rota = None

    # Para cada permutação de cidades
    for perm in permutacoes:
        # Calcula a distância total da rota, começando da cidade inicial (0)
        distancia_atual = D[0][perm[0]]
        for i in range(n - 2):
            distancia_atual += D[perm[i]][perm[i + 1]]

        # Adiciona a distância de volta à cidade inicial (0)
        distancia_atual += D[perm[n - 2]][0]

        # Verifica se a distância total é menor que o menor encontrado até agora
        if distancia_atual < menor_distancia:
            menor_distancia = distancia_atual
            melhor_rota = [0] + list(perm) + [0]
        
        # Verifica se a distância total é menor ou igual ao limite L
        if distancia_atual <= L:
            return True, melhor_rota

    # Se nenhuma permutação atender ao limite de distância, retorna a menor rota encontrada
    if melhor_rota:
        return False, melhor_rota
    else:
        return False, None