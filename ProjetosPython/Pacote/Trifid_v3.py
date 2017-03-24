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

print("******* Cifra Trifid *********")
print('Opções:')
print('1 - Para gerar uma chave aleatória.')
print('2 - Para entrar com uma chave válida.')
print('')
opcao = input('Digite o número da opção escolhida:')
if (opcao == '1'):
    chave = gerarChave()
elif (opcao == '2'):
    chave = input('Digite uma chave válida (26 letras diferentes + 1 símbolo):')
    chave = limparTexto(chave)
else:
    print('Numero invalido para opção digitada.')

dicionario = criarDicionarioTrifid(chave)
dicionarioInvertido = inverterDicionario(dicionario)
print('Dicionario (Chave) =',dicionario)
print('Dicionario Invertido =',dicionarioInvertido)
print('Chave =',chave)
print('') 
texto = input('Digite o texto a ser Cifrado: ')
texto = limparTexto(texto)

print('Texto Limpo =',texto)
print('')
print('############### Resposta ##################')

textoCifrado = cifrarTrifid(texto)
print('Texto Cifrado = ',textoCifrado);
print('')
textoDecifrado = decifrarTrifid(textoCifrado)
print('Texto Decifrado =',textoDecifrado)

