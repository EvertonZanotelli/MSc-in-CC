import time

def karatsuba_multiplicacao(numero1, numero2):
    # Converte os números em strings para facilitar a manipulação
    str_numero1 = str(numero1)
    str_numero2 = str(numero2)

    # Caso base: se um dos números tem apenas um dígito, usamos a multiplicação tradicional
    if len(str_numero1) == 1 or len(str_numero2) == 1:
        return numero1 * numero2

    # Calcula o tamanho dos números e divide pela metade (arredondando para cima)
    tamanho = max(len(str_numero1), len(str_numero2))
    metade = tamanho // 2

    # Divide os números em duas partes
    parte1_numero1 = int(str_numero1[:-metade]) if len(str_numero1[:-metade]) > 0 else 0
    parte2_numero1 = int(str_numero1[-metade:])
    parte1_numero2 = int(str_numero2[:-metade]) if len(str_numero2[:-metade]) > 0 else 0
    parte2_numero2 = int(str_numero2[-metade:])

    # Calcula os produtos intermediários recursivamente
    ac = karatsuba_multiplicacao(parte1_numero1, parte1_numero2)
    bd = karatsuba_multiplicacao(parte2_numero1, parte2_numero2)
    ad_bc = karatsuba_multiplicacao(parte1_numero1 + parte2_numero1, parte1_numero2 + parte2_numero2) - ac - bd

    # Calcula o resultado final usando a fórmula de Karatsuba
    return (10**(2*metade)) * ac + (10**metade) * ad_bc + bd

# Exemplo de uso
numero_X = 2348197263
numero_Y = 5342465464
inicio = time.time()
resultado = karatsuba_multiplicacao(numero_X, numero_Y)
fim = time.time()
tempo = fim - inicio
print(tempo)
print(resultado)

