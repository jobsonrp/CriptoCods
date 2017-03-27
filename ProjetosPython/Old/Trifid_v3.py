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

def dicionarioTrifidDinamica():
    alfabeto = getAlfabeto()
    alfabetoAleatorio = ''.join(sample(alfabeto,len(alfabeto)))
    codigos = geradorCodigos()
    dicionarioLetraCodigo = {}
    for i in range(0, len(alfabetoAleatorio)):   
        dicionarioLetraCodigo[alfabetoAleatorio[i]]=codigos[i]
    return dicionarioLetraCodigo, alfabetoAleatorio

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

def cifrarTrifid(texto):
    texto = limparTexto(texto)
    codigosMisturados = []
    codCifrado = ''
    textoCifrado = ''
    listaCodCifrados = []
    for caracter in texto:
        codigosMisturados.append(dicionario[caracter])
    for linha in range(3):
        for cod in codigosMisturados:
            codCifrado += cod[linha]
    for indice in range(0,len(codCifrado)-1,3):
        listaCodCifrados.append(codCifrado[indice : indice+3])
    for novoCodigo in listaCodCifrados:
        textoCifrado += dicionarioInvertido[novoCodigo]
    return textoCifrado

def decifrarTrifid(textocifrado):
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
        textoOriginal += dicionarioInvertido[codDecifrado]         
    return textoOriginal

dicionario, alfabetoAleatorio = dicionarioTrifidDinamica()
dicionarioInvertido = inverterDicionario(dicionario)
print('Dicionario (Chave)= ',dicionario)
print('Dicionario Invertido = ',dicionarioInvertido)
print('Alfabeto Aleatorio (Chave)= ',alfabetoAleatorio)

print('')
print('############### Resposta ##################')

textoCifrado = cifrarTrifid('T R E A T Y E N D S B O E R W A R .')
print('Texto Original (limpo) = ', limparTexto('T R E A T Y E N D S B O E R W A R .'))    
print('Texto Cifrado = ',textoCifrado);
print('')
textoDecifrado = decifrarTrifid(textoCifrado)
print('Texto Original (decifrado) = ',textoDecifrado)

