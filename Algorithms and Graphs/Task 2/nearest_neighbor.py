def algoritmo_tsp_vizinho_mais_proximo(n, D, L):
    # Inicializa o conjunto de cidades não visitadas, excluindo a cidade inicial (0)
    nao_visitadas = set(range(1, n))
    cidade_atual = 0
    rota = [cidade_atual]
    distancia_total = 0

    # Enquanto houver cidades não visitadas
    while nao_visitadas:
        # Encontra a cidade mais próxima que não foi visitada
        cidade_mais_proxima = min(nao_visitadas, key=lambda cidade: D[cidade_atual][cidade])
        
        # Atualiza a distância total e a cidade atual
        distancia_total += D[cidade_atual][cidade_mais_proxima]
        cidade_atual = cidade_mais_proxima
        
        # Remove a cidade atual do conjunto de não visitadas e adiciona à rota
        nao_visitadas.remove(cidade_atual)
        rota.append(cidade_atual)

    # Retorna à cidade inicial (0)
    distancia_total += D[cidade_atual][0]
    rota.append(0)
    
    # Verifica se a distância total é menor ou igual ao limite L
    if distancia_total <= L:
        return True, rota
    else:
        return False, None
