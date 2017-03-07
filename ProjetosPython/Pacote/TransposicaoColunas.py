# -*- coding: utf-8 -*-

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
        raise Exception('Chave precisa conter somente números sequenciais a partir de 1 (não ordenados)')


def texto_matriz(texto, num_colunas):
    matriz = list('' for x in range(num_colunas))
    y = 0
    for c in texto:
        if y == num_colunas:
            y = 0
        matriz[y] += c
        y += 1
    return matriz


def cifra(texto, chave):
    complemento = len(texto) % len(chave)
    if complemento > 0:
        texto = texto.ljust(len(texto) + len(chave) - complemento) # Completa o texto com espaço (" ") para que ( len(novoTexto) % len(chave) ) = 0
    matriz = texto_matriz(texto, len(chave))
    print(matriz)

    matriz_reordenada = [matriz[x - 1] for x in chave]
    return ''.join(matriz_reordenada)


def decifra(cifrado, chave):
    if (len(cifrado) % len(chave)) > 0:
        raise Exception('Texto cifrado não pode ser decifrado com essa chave')

    n = len(cifrado)//len(chave)
    matriz_cifrada = [cifrado[i:i+n] for i in range(0, len(cifrado), n)]
    print(matriz_cifrada)

    result = ''
    for y in range(n):
        result += ''.join([matriz_cifrada[chave.index(x)][y:y+1] for x in range(1, len(chave) + 1)])

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
    return vetorChaveNumeros

def cifrarDecifrar(opcao,texto,chave):
    texto = limparTexto(texto)
    chave = intChave(chave)
    colunas = valida_chave(chave)
    if opcao == "1":
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
                break
            print('Resultado: "%s"' % result)
            print("")
        exit()

    except Exception as e:
        print('Erro: %s %s' % (e, type(e)))
        exit(1)
        
        