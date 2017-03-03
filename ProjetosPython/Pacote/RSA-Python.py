import random

def euclides_mdc(dividendo, divisor): #maximo divisor comum pelo metodo de euclides
    while divisor != 0:
        temp = divisor
        divisor = dividendo % divisor
        dividendo = temp
    return dividendo

def inverso_multiplicativo(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

def verificar_primo(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def gerador_chaves(p, q):
    if not (verificar_primo(p) and verificar_primo(q)):
        raise ValueError('Os dois Numeros Precisam ser Primos.')
    elif p == q:
        raise ValueError('"p" e "q" nao podem ser iguais')
    # n = pq
    n = p * q

    # Phi é o totético de n
    phi = (p - 1) * (q - 1)

    # Escolha um inteiro "e" tal que "e" e phi(n) são coprimos
    e = random.randrange(1, phi)

    # Usa o algoritmo de euclides para verificar se "e" e "phi(n)" são coprimos
    g = euclides_mdc(e, phi)
    while g > 1:
        e = random.randrange(1, phi)
        g = euclides_mdc(e, phi)

    # Usa o algoritmo extendido de Euclides para gerar a chave privada
    d = inverso_multiplicativo(e, phi)

    # Retorna a chave pública e privada
    # Chave publica é (e, n) e a chave privada é (d, n)
    return ((e, n), (d, n))


def encriptar(pk, texto):
    # Unpack the key into it's components
    key, n = pk
    # Converte cada letra no texto para numeros baseado no caractere usando a^b mod m
    cifra = [(ord(char) ** key) % n for char in texto]
    # Retorna o array de bytes
    return cifra


def decriptar(pk, textoCifrado):
    # Unpack the key into its components
    key, n = pk
    # Gera o texto decriptado baseado no texto cifrado e chave usando a^b mod m
    texto = [chr((char ** key) % n) for char in textoCifrado]
    # Retorna o array de bytes como string
    return ''.join(texto)


if __name__ == '__main__':
    '''
    Detecta se o script está sendo rodado pelo usuário
    '''
    print("RSA Encriptador/ Decriptador")
    p = int(input("Digite um numero primo (17, 19, 23, etc): "))
    q = int(input("Digite outro numero primo (Nao o mesmo que digitou anteriormente): "))
    print("Gerando seus publico/privado par de chaves agora . . .")
    publica, privada = gerador_chaves(p, q)
    print("Sua chave publica é ", publica, " e sua chave privada é ", privada)
    message = input("Digite uma mensagem para encriptar com sua chave privada: ")
    encrypted_msg = encriptar(privada, message)
    print("Sua mensagem encriptada é: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decriptando mensagem com a chave publica ", publica, " . . .")
    print("Sua mensagem é:")
    print(decriptar(publica, encrypted_msg))
    
    