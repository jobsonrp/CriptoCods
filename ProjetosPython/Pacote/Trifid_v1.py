#Trifid - Criptografia

from random import sample

def getAlfabeto():
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.'

def getAlfabetoCompleto():
    return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.'

def geradorCodigos():
    listaCodigos = []
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                listaCodigos.append(str(i)+str(j)+str(k))
    return listaCodigos

def misturarLista(lista):
    return sample(lista, len(lista))
    
def dicionarioTabelaTrifidDinamica():
    alfabeto = getAlfabeto()
    listaCodigosMisturados = misturarLista(geradorCodigos())
    dicLetraCodigo = {}
    for i in range(0, len(alfabeto)):   
        dicLetraCodigo[alfabeto[i]]=listaCodigosMisturados[i]
    return dicLetraCodigo

def limparTexto(texto):
    alfabetoCompleto = getAlfabetoCompleto()
    novotexto = texto;
    for caractere in novotexto:
        if not (caractere in alfabetoCompleto):
            novotexto = novotexto.replace(caractere,"")
    return novotexto.upper();

def cifrarTrifid(texto):
    texto = limparTexto(texto)
    print('Texto Original = ',texto)
    listaCodigos = []
    dicTabela = dicionarioTabelaTrifidDinamica()
    print('Tabela = ',dicTabela)
    codCifrado = ''
    textoCifrado = ''
    listaCodCifrados = []
    for caracter in texto:
        listaCodigos.append(dicTabela[caracter])
    for linha in range(3):
        for cod in listaCodigos:
            codCifrado += cod[linha]
    for indice in range(0,len(codCifrado)-1,3):
        listaCodCifrados.append(codCifrado[indice:indice+3])
    dicTabelaInversa = {}
    for item in dicTabela:
        dicTabelaInversa[dicTabela[item]]=item
    print('Tabela Invertida = ',dicTabelaInversa)
    for novoCod in listaCodCifrados:
        textoCifrado += dicTabelaInversa[novoCod]
    return textoCifrado

textoCifrado = cifrarTrifid('T R E A T Y E N D S B O E R W A R .')
print('Texto Cifrado = ',textoCifrado);

#print(dicionarioTabelaTrifidDinamica())

#print(geradorCodigos())

#print(misturarLista(["1", "2", "3", "4"]));

