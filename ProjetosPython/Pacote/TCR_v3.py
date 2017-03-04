# coding: utf-8

def mdcAEE(valor1, valor2): # Algoritmo de Euclides Extendido
    x0,x1,y0,y1 = 1,0,0,1 # Matriz Identidade
    mdc = valor1
    n = valor2
    while n!=0:
        q,mdc,n = mdc//n, n, mdc%n # n1 // n2 => parte inteira da divisão de n1 por n2
        x0,x1 = x1, x0-q*x1
        y0,y1 = y1, y0-q*y1
    return (mdc,x0) 

def inversoMultiplicativo(a, P): # Inverso Multiplicativo de "a" mod "P" = x, onde "a*x = 1 mod P"
    mdc,x0 = mdcAEE(a, P)
    if mdc != 1: return False
    return x0 % P

def verificarCoPrimo(mA, mB):
    if mdcAEE(mA, mB)[0] == 1:
        return True
    return False

def verificarVetorCoPrimos(vetor):
    for i in range(0,len(vetor)-1):
        for j in range(i+1,len(vetor)):
            if verificarCoPrimo(vetor[i], vetor[j]) == False:
                print("Altere o vetor dos Módulos: %d e %d não são Coprimos." % (vetor[i], vetor[j]) )
                return False
    return True

def teoremaChinesDosRestos(restos, modulos):
    M = 1
    for m in modulos:
        M *= m
    ratios = []
    for m in modulos:
        ratios.append(M//m)
    B = []
    for i in range(len(modulos)):
        B.append(inversoMultiplicativo(ratios[i], modulos[i]))
    x = 0
    for i in range(len(modulos)):
        x += restos[i]*B[i]*ratios[i]
    return x % M
    
modulos = [64,23] #[[23, 14], [41, 32], [64, 38], [97, 61], [99, 43]] = 934
restos = [38,14] 
if verificarVetorCoPrimos(modulos):
    solucao = teoremaChinesDosRestos(restos, modulos)
    print(solucao)
