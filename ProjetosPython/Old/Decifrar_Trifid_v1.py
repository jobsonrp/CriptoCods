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

def dicionarioTrifidDinamica(chave):
    alfabetoAleatorio = chave
    codigos = geradorCodigos()
    dicionarioLetraCodigo = {}
    for i in range(0, len(alfabetoAleatorio)):   
        dicionarioLetraCodigo[alfabetoAleatorio[i]]=codigos[i]
    return dicionarioLetraCodigo

def gerarDicionarioCodigoLetra(dicionario):
    dicionarioCodigoLetra = {}
    for item in dicionario:
        dicionarioCodigoLetra[dicionario[item]]=item
    return dicionarioCodigoLetra

def limparTexto(texto):
    alfabetoCompleto = getAlfabetoCompleto()
    novotexto = texto;
    for caractere in novotexto:
        if not (caractere in alfabetoCompleto):
            novotexto = novotexto.replace(caractere,"")
    return novotexto.upper();

def decifrarTrifid(textocifrado, chave):
    dicionario = dicionarioTrifidDinamica(chave)
    dicionarioCodigoLetra = gerarDicionarioCodigoLetra(dicionario)
    texto = limparTexto(textocifrado)
    comprimentoTexto = len(texto)
    codCifrados = ''
    textoOriginal = ''
    listCodDecifrados = []
    for caracter in texto:
        codCifrados += dicionario[caracter]
    for posicaoLetra in range(comprimentoTexto):
        listCodDecifrados.append(codCifrados[posicaoLetra] + codCifrados[posicaoLetra + comprimentoTexto] + codCifrados[posicaoLetra + 2*comprimentoTexto])
    for codDecifrado in listCodDecifrados:
        textoOriginal += dicionarioCodigoLetra[codDecifrado]         
    return textoOriginal

textoCifrado = input('Digite o texto cifrado: ')
chave = input('Digite a chave (Alfabeto misturado com 26 letras mais o ponto "."): ')

print('')
print('############### Resposta ##################')
print('')
textoDecifrado = decifrarTrifid(textoCifrado, chave)
print('Texto Original (decifrado) = ',textoDecifrado)

