def algoritmo_tsp_backtracking(D, L):
    n = len(D)  # número de cidades
    visitado = [False] * n  # vetor para rastrear as cidades visitadas
    rota = [0]  # começar da cidade 0
    melhor_distancia = float('inf')  # iniciar com infinito
    melhor_rota = None

    def backtrack(cidade_atual, distancia_atual, nivel):
        nonlocal melhor_distancia, melhor_rota
        if distancia_atual > L:  # poda a rota se ultrapassar o limite L
            return

        if nivel == n and D[cidade_atual][0] > 0:  # todas as cidades foram visitadas
            distancia_total = distancia_atual + D[cidade_atual][0]  # retornar à cidade inicial
            if distancia_total < melhor_distancia:
                melhor_distancia = distancia_total
                melhor_rota = rota[:] + [0]
            return

        for prox_cidade in range(n):
            if not visitado[prox_cidade] and D[cidade_atual][prox_cidade] > 0:
                visitado[prox_cidade] = True
                rota.append(prox_cidade)

                backtrack(prox_cidade, distancia_atual + D[cidade_atual][prox_cidade], nivel + 1)

                # backtracking: desfaz a escolha
                visitado[prox_cidade] = False
                rota.pop()

    # Início do backtracking
    visitado[0] = True  # começar na cidade 0
    backtrack(0, 0, 1)

    if melhor_distancia <= L:
        return True, melhor_rota
    else:
        return False, melhor_rota
