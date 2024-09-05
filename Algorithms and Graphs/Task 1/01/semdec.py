import sys
from math import sqrt
from operator import itemgetter 
import time 
import re
contador = 0
filtraponto=re.compile("(-?\\d+.?\\d*)\\s(-?\\d+.?\\d*)")

# Calcula a distancia entre os pontos p1=(x1,y1) e p2=(x2,y2)

def distancia(p1, p2):
    return sqrt(pow(float(p1[0])-float(p2[0]),2) + pow(float(p1[1])-float(p2[1]),2))

# Solução para P que não usa divisão e conquista

def forcabruta(pontos):

    menordistancia=float("inf")
    
    if len(pontos) > 1:
        menordistancia=distancia(pontos[0],pontos[1])

        for i in range(0,len(pontos)-1):
            contador = contador + 1
            for j in range(i+1,len(pontos)):
                contador +=1
                if distancia(pontos[i],pontos[j]) < menordistancia:
                    menordistancia = distancia(pontos[i],pontos[j])

    return menordistancia


# Abre o arquivo de entradas e cria um array de pontos 

def read_file(entrada):
    pontos=[]
    # Formato do arquivo
    # x1 y1
    # x2 y2
    arquivo=open(entrada,'r')
    for linha in arquivo.readlines():
        linha = linha.strip()
        pontotratado=filtraponto.match(linha)
        if pontotratado:
            x = pontotratado.group(1)
            x = float(x)
            y = pontotratado.group(2)
            y = float(y)
            pontos.append((x,y))
            
    pontos.sort()

    return pontos



def main(entrada): 
    
    pontos=read_file(entrada)
    comeco = time.time()
    x = forcabruta(pontos)
    t1 = (time.time() - comeco)
    print
    print("Força Bruta: {}".format(x))
    print("--- {} segundos ---".format( t1 ))
    
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Forneça o arquivo de entradas")
        quit(1)
    main(sys.argv[1])
    print(contador)