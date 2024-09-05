import sys
from math import sqrt
from operator import itemgetter 
import time 
import re

filtraponto=re.compile("(-?\\d+.?\\d*)\\s(-?\\d+.?\\d*)")

# Calcula a distancia entre os pontos p1=(x1,y1) e p2=(x2,y2)

def distancia(p1, p2):
    return sqrt(pow(float(p1[0])-float(p2[0]),2) + pow(float(p1[1])-float(p2[1]),2))

# Solução para P que usa divisão e conquista


def vizinho(pontos, Py):
    if len(pontos) <= 3:
        return forcabruta(pontos)
    else:
        return DeC(pontos, Py)
    

def DeC(pontos, Py):

    if len(pontos) <= 3:
        return forcabruta(pontos)
    else:

        # Divide em duas partes
        
        n = len(pontos)
        c = n//2
        
        esquerda = pontos[:c]
        direita = pontos[c:]
        
        Pye=[]
        Pyd=[]
        
        metade=pontos[c][0]
        
        for e in Py:
            if e[0]<metade:
                Pye.append(e)
            else:
                Pyd.append(e)
        
        delta = min( DeC(esquerda, Pye), DeC(direita, Pyd) )
        
        y = []
        for e in Py:
            if ( abs(e[0] - metade ) <= delta) :
                y.append(e)

        delta2 = float("inf")
        
        if (len(y) > 0):

            for i in range(0, len(y)-1):
                j = i+1
                while ( (j < len(y)) and (y[j][1]-y[i][1] <= delta) ):
                    if distancia(y[i],y[j]) < delta2:
                        delta2 = distancia(y[i],y[j])
                    j = j+1
            
            return min(delta, delta2)
        else:

            return delta

# Função para tratar casos menores que 3
def forcabruta(pontos):

    menordistancia=float("inf")
    
    if len(pontos) > 1:
        menordistancia=distancia(pontos[0],pontos[1])

        for i in range(0,len(pontos)-1):
            for j in range(i+1,len(pontos)):
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
    Py = sorted(pontos,key=itemgetter(1))
    comeco = time.time()
    x = vizinho(pontos, Py)
    t2 = (time.time() - comeco)
    print
    print("Divisão e Conquista: {}".format(x))
    print("--- {} Segundos ---".format( t2 ))
    print
  

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Forneça o arquivo de entradas")
        quit(1)
    main(sys.argv[1])