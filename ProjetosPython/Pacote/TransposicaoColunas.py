# -*- coding: utf-8 -*-
from random import randint

def validarChave(chave):
    alfabeto = getAlfabetoCompleto()
    for caracter in chave:
        if caracter not in alfabeto:
            return False
    return True

def texto_matriz(texto, chave):
    matriz = list('' for x in range(len(chave)))
    y = 0
    for c in texto:
        if y == len(chave):
            y = 0
        matriz[y] += c
        y += 1  
    matrizReordenada = reordenarMatriz(matriz, chave)          
    return matriz, matrizReordenada

def reordenarMatriz(matriz, chave):
    matrizReordenada = list('' for x in range(len(chave)))
    for j in range(len(chave)):
        x = chave[j]-1
        matrizReordenada[x] = matriz[j]
    return matrizReordenada

def cifra(texto, chave):
    complementoTexto = ""
    alfabeto = getAlfabeto()
    complemento = len(texto) % len(chave)
    if complemento > 0:
        for i in range(len(chave) - complemento):
            complementoTexto += alfabeto[randint(0,25)]
        texto += complementoTexto
    print("Texto limpo:",texto)
    matriz, matrizReordenada = texto_matriz(texto, chave)
    print("Matriz = ",matriz)
    print("MatrizReordenada = ",matrizReordenada)
    return ''.join(matrizReordenada)

def decifra(cifrado, chave):
    matrizReordenada = list('' for x in range(len(chave)))
    n = len(cifrado)//len(chave)
    matriz_cifrada = [cifrado[i:i+n] for i in range(0, len(cifrado), n)]
    print("Matriz_cifrada = ",matriz_cifrada)
    for i in range(len(chave)):
        matrizReordenada[i] = matriz_cifrada[chave[i]-1]      
    print("MatrizReordenada = ",matrizReordenada)
    result = ""
    for y in range(n):
        result += ''.join([matrizReordenada[x-1][y:y+1] for x in range(1, len(chave) + 1)])
    return result

def getAlfabeto():
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.'

def getAlfabetoCompleto():
    return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.'

def limparTexto(texto):
    alfabetoCompleto = getAlfabetoCompleto()
    novotexto = texto;
    for caractere in novotexto:
        if not (caractere in alfabetoCompleto):
            novotexto = novotexto.replace(caractere,"")
    return novotexto.upper();

def intChave(chave):
    alfabeto = getAlfabeto()
    vetorPosicao = []
    vetorPosicaoOrdenado = []
    vetorChaveNumeros = []
    for caracter in chave:
        posicao = alfabeto.index(caracter)
        vetorPosicao.append(posicao)
        vetorPosicaoOrdenado.append(posicao)
    vetorPosicaoOrdenado.sort()
    for caracter in vetorPosicao:
        posicao = vetorPosicaoOrdenado.index(caracter)
        if posicao in vetorChaveNumeros:
            vetorChaveNumeros.append(posicao+1)
        vetorChaveNumeros.append(posicao+1)      
    return vetorChaveNumeros

def posicoesLetraChave(letra, chave):
    posicao = 0
    inicio = 0
    vetorPosicoesLetra = []
    while posicao != -1:
        posicao = chave.find(letra,inicio)
        vetorPosicoesLetra.append(posicao)
        inicio = posicao + 1
    return vetorPosicoesLetra[:-1]

def intChaveLetrasRepetidas(chave):
    alfabeto = getAlfabetoCompleto()
    vetorChaveNumeros = list('' for x in range(len(chave)))
    total = 1
    for caracter in alfabeto:
        
        if caracter in vetorChaveNumeros:
            vetorChaveNumeros[chave.index(caracter)] = total + 1
        else:
            vetorChaveNumeros[chave.index(caracter)] = total
        total += 1
    return vetorChaveNumeros

def cifrarDecifrar(opcao,texto,chave):
    chave = intChave(chave)
    print("Chave Numérica:",chave)
    if opcao == "1":
        texto = limparTexto(texto)
        result = cifra(texto, chave)
    if opcao == "2":
        result = decifra(texto, chave)
    return result    

if __name__ == '__main__':
    try:
        opcao = ""
        while opcao != "x":
            opcao = input("""######## TRANSPOSICAO DE COLUNAS ########
            1 - Cifrar
            2 - Decifrar
            x - Sair 
            Digite uma das opções acima: """)
            print("")
            if opcao == "1":
                texto_claro = input("Texto a ser Cifrado: ")
                chave = input("Chave: ")
                print("vetor:", posicoesLetraChave('a', chave))
                while not validarChave(chave):
                    chave = input("Digite uma chave válida (letras do alfabeto): ")
                chave = limparTexto(chave)               
                result = cifrarDecifrar(opcao, texto_claro, chave)
                    
            elif opcao == "2":
                texto_cifrado = input("Texto a ser Decifrado: ")
                chave = input("Chave: ")
                while not validarChave(chave):
                    chave = input("Digite uma chave válida (letras do alfabeto: ")
                chave = limparTexto(chave)  
                result = cifrarDecifrar(opcao, texto_cifrado, chave)
            else:
                print("O aplicativo foi encerrado pelo usuario.")
                break
            print('Resultado: "%s"' % result)
            print("")
        exit()

    except Exception as e:
        print('Erro: %s %s' % (e, type(e)))
        exit(1)
        
        