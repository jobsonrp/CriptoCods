#Trifid - Criptografia

from random import sample

def getAlfabeto():
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.'

def getAlfabetoCompleto():
    return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.'

def geradorCodigos():
    codigos = []
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                codigos.append(str(i)+str(j)+str(k))
    return codigos

def gerarChave():
    alfabeto = getAlfabeto()
    alfabetoAleatorio = ''.join(sample(alfabeto,len(alfabeto)))
    return alfabetoAleatorio

def criarDicionarioTrifid(chave):
    codigos = geradorCodigos()
    dicionarioLetraCodigo = {}
    for i in range(0, len(chave)):   
        dicionarioLetraCodigo[chave[i]]=codigos[i]
    return dicionarioLetraCodigo

def inverterDicionario(dicionario):
    dicionarioInvertido = {}
    for item in dicionario:
        dicionarioInvertido[dicionario[item]]=item
    return dicionarioInvertido

def limparTexto(texto):
    alfabetoCompleto = getAlfabetoCompleto()
    novotexto = texto;
    for caractere in novotexto:
        if not (caractere in alfabetoCompleto):
            novotexto = novotexto.replace(caractere,"")
    return novotexto.upper();

def cifrarTrifid(texto, chave):
    dicLetraCod, dicCodLetra = getDicionarios(chave)
    texto = limparTexto(texto)
    codigosMisturados = []
    codCifrado = ''
    textoCifrado = ''
    listaCodCifrados = []
    for caracter in texto:
        codigosMisturados.append(dicLetraCod[caracter])
    for linha in range(3):
        for cod in codigosMisturados:
            codCifrado += cod[linha]
    for indice in range(0,len(codCifrado)-1,3):
        listaCodCifrados.append(codCifrado[indice : indice+3])
    for novoCodigo in listaCodCifrados:
        textoCifrado += dicCodLetra[novoCodigo]
    return textoCifrado

def getDicionarios(chave):
    dicionario = criarDicionarioTrifid(chave)
    dicionarioInvertido = inverterDicionario(dicionario)
    print('Dicionario (Chave) =',dicionario)
    print('Dicionario Invertido =',dicionarioInvertido)
    print('Chave =',chave)
    print('')
    return dicionario, dicionarioInvertido

def decifrarTrifid(textocifrado, chave):
    dicLetraCod, dicCodLetra = getDicionarios(chave)
    texto = limparTexto(textocifrado)
    comprimentoTexto = len(texto)
    codCifrados = ''
    textoOriginal = ''
    listCodDecifrados = []
    for caracter in texto:
        codCifrados += dicLetraCod[caracter]
    for posicaoLetra in range(comprimentoTexto):
        listCodDecifrados.append(codCifrados[posicaoLetra] + codCifrados[posicaoLetra + comprimentoTexto] + codCifrados[posicaoLetra + 2*comprimentoTexto])
    for codDecifrado in listCodDecifrados:
        textoOriginal += dicCodLetra[codDecifrado]         
    return textoOriginal

while True:
    print("******* Cifra Trifid *********")
    print('')    
    print('Opções de Funções:')
    print('1 - Para Cifrar uma mensagem.')
    print('2 - Para Decifrar uma mensagem.')
    print('s - Para Sair do sistema.')
    funcao = input('Digite uma das opções mostradas acima:')
    print('')
    if funcao == '1':
        while True:
            print('     Opções para Cifrar:')
            print('     3 - Para gerar uma chave aleatória.')
            print('     4 - Para entrar com uma chave válida.')
            print('     v - Para Voltar.')
            print('')   
            opcao = input('     Digite uma das opções mostradas acima:')
            print('')
            if (opcao == 'v'):
                break 
            if opcao == '3' or opcao == '4':
                if (opcao == '3'):
                    chave = gerarChave()
                elif (opcao == '4'):
                    chave = input('     Digite uma chave válida (26 letras diferentes + 1 símbolo):')
                    chave = limparTexto(chave)
                texto = input('     Digite o texto a ser Cifrado: ')
                texto = limparTexto(texto)
                print('     Texto Limpo =',texto)   
                print('')
                print('############### Resposta ##################')
                textoCifrado = cifrarTrifid(texto, chave)
                print('     Texto Cifrado = ',textoCifrado);
                print('')
            else:
                print('     Numero invalido para opção digitada.')    
    elif funcao == '2':
        chave = input('Digite uma chave válida (26 letras diferentes + 1 símbolo):')
        chave = limparTexto(chave)
        print('')
        texto = input('Digite o texto Cifrado a ser descoberto:')
        texto = limparTexto(texto)
        print('Texto Limpo =',texto) 
        print('')
        print('############### Resposta ##################')
        textoDecifrado = decifrarTrifid(texto, chave)
        print('Texto Decifrado =',textoDecifrado)
        print('')

    elif (funcao == 's'):
        print('Sistema encerrado pelo usuario.')
        break 
        