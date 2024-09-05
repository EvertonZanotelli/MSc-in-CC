import time

def multiplicar_numeros_grandes(numero1, numero2):

    comeco = time.time()

    # Converte as strings para inteiros
    numero1 = int(numero1)
    numero2 = int(numero2)

    # Multiplica os números
    produto = numero1 * numero2

    # Converte o produto de volta para string
    produto_str = str(produto)

    fim = (time.time() - comeco)

    print(f"Produto: {produto_str}")
    print(f"Tempo de execução: {fim} segundos")

    return produto_str


# Obtenha os números do usuário
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

# Multiplica os números
multiplicar_numeros_grandes(numero1, numero2)