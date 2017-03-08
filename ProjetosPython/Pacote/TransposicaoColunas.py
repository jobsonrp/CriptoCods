# -*- coding: utf-8 -*-
from random import randint

def valida_chave(chave):
    try:
        colunas = list()
        for n in chave:
            colunas.append(int(n))
        colunas_ordenadas = sorted(colunas)
        for i in range(1, len(chave)):
            if i != colunas_ordenadas[i-1]:
                print(colunas_ordenadas)
                raise ValueError()
        return colunas
    except ValueError as e:
        raise Exception('A Chave não pode conter letras repetidas.')

def texto_matriz(texto, num_colunas, chave):
    matriz = list('' for x in range(num_colunas))
    matrizReordenada = list('' for x in range(num_colunas))
    y = 0
    for c in texto:
        if y == num_colunas:
            y = 0
        matriz[y] += c
        y += 1     
    print("Matriz =", matriz)
    print("Chave =", chave)
    print("c-0", chave[0])
    for j in range(num_colunas):
        print("************** j = ",j)
        print("Chave j = ", chave[j])
        x = chave[j]-1
        print("m x = ",matriz[x] )
        matrizReordenada[x] = matriz[j]
    return matriz, matrizReordenada

def cifra(texto, chave):
    complementoTexto = ""
    alfabeto = getAlfabeto()
    complemento = len(texto) % len(chave)
    if complemento > 0:
        for i in range(len(chave) - complemento):
            complementoTexto += alfabeto[randint(0,25)]
        texto += complementoTexto
    print(texto)
    matriz, matrizReordenada = texto_matriz(texto, len(chave), chave)
    print(matriz)
    print(matrizReordenada)
    return ''.join(matrizReordenada)

def decifra(cifrado, chave):
    matrizReordenada = list('' for x in range(len(chave)))
    """if (len(cifrado) % len(chave)) > 0:
        raise Exception('Texto cifrado não pode ser decifrado com essa chave')"""
    n = len(cifrado)//len(chave)
    matriz_cifrada = [cifrado[i:i+n] for i in range(0, len(cifrado), n)]
    print("Matriz_cifrada = ",matriz_cifrada)
    for j in range(len(chave)):
        print("************** j = ",j)
        print("Chave j = ", chave[j])
        x = chave[j]-1
        print("m x = ",matriz_cifrada[x] )
        matrizReordenada[x] = matriz_cifrada[j]
    print("matrizReordenada = ",matrizReordenada)
    result = ""
    for y in range(n):
        result += ''.join([matrizReordenada[chave.index(x)][y:y+1] for x in range(1, len(chave) + 1)])
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
    chave = limparTexto(chave)
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
        vetorChaveNumeros.append(posicao+1)   
    print(vetorChaveNumeros)   
    return vetorChaveNumeros

def cifrarDecifrar(opcao,texto,chave):
    chave = intChave(chave)
    colunas = valida_chave(chave)
    if opcao == "1":
        texto = limparTexto(texto)
        result = cifra(texto, colunas)
    if opcao == "2":
        result = decifra(texto, colunas)
    return result    

if __name__ == '__main__':
    try:
        opcao = ""  
        while opcao != "x":
            opcao = input("""Digite uma das opções abaixo:
            1 - Cifrar
            2 - Decifrar
            x - Sair 
            """)
            
            if opcao == "1":
                texto_claro = input("Texto a ser Cifrado: ")
                chave = input("Chave: ")               
                result = cifrarDecifrar(opcao, texto_claro, chave)
                    
            elif opcao == "2":
                texto_cifrado = input("Texto a ser Decifrado: ")
                chave = input("Chave: ")
                result = cifrarDecifrar(opcao, texto_cifrado, chave)
            else:
                print("O aplicativo foi encerrado.")
                break
            print('Resultado: "%s"' % result)
            print("")
        exit()

    except Exception as e:
        print('Erro: %s %s' % (e, type(e)))
        exit(1)
        
        