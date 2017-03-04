# coding: utf-8

from random import randint

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
                #print("Altere o vetor dos Módulos: %d e %d não são Coprimos." % (vetor[i], vetor[j]) )
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

def gerarVetorModulosCoPrimos(n):
    vetor = []
    for i in range(0,n):
        vetor.append(randint(10,99))
        while verificarVetorCoPrimos(vetor) == False:
            vetor[i] = randint(10,99)
    vetor.sort()
    return vetor

def produtoKmenores(k, vetor):
    N = 1
    for i in range(0,k):
        N *= vetor[i]
    return N
    
def produtoKmenos1Maiores(k, vetor):
    M = 1
    for j in range(len(vetor)-k+1,len(vetor)):
        M *= vetor[j]
    return M

def gerarSenha(N, M):
    Senha = randint(M+1,N-1)
    return Senha

def partilharSenha(n,k):
    M = 99
    N = 0
    while M >= N:
        modulos = gerarVetorModulosCoPrimos(n)
        N = produtoKmenores(k, modulos)
        M = produtoKmenos1Maiores(k, modulos)
    senha = gerarSenha(N, M)
    senhasPartidas = []
    for mod in modulos:
        y = senha % mod
        senhasPartidas.append([mod,y])
    return senhasPartidas

def recuperarSenha(n,k):
    vetorModulo = []
    vetorResto = []
    for i in range(nPares):
        modulo = int(input("Pessoa%d, Primeiro número:" % (i+1) ))
        vetorModulo.append(modulo)
        resto = int(input("Pessoa%d, Segundo número:" % (i+1) ))
        vetorResto.append(resto)
        print("")
    if verificarVetorCoPrimos(vetorModulo):
        senha = teoremaChinesDosRestos(vetorResto, vetorModulo)
        return senha
    else:
        return False
    
print("******* Sistema de Partilha de Senha *********")
n = int(input("Número total de pessoas:"))
k = int(input("Número mínimo de pessoas necessárias para recuperar a senha:"))
print("Conjunto de senha =",partilharSenha(n,k))
print("")
print("--- Recuperação da Senha ---")
nPares = 0
while nPares < k or nPares > n:
    nPares = int(input("Número de pessoas presentes para recuperar a senha (>=%d e <=%d):" % (k,n) )) 
senha = recuperarSenha(n, k)
if senha != False:
    print("Senha Geral =",senha)
else:
    print("Erro ao digitar os pares de senha.")

      
