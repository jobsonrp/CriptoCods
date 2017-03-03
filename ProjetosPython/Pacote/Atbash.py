class AtBash:
    def __init__(self):
        self.alfabeto = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+|:"<>-=[];,.?/`'

    def codificar(self, text_original):
        cifra = ""
        for i in text_original:
            index = self.alfabeto.index(i)
            cifra += self.alfabeto[abs(len(self.alfabeto) - index - 1) % len(self.alfabeto)]
        return cifra

    def decodificar(self, text_cifra):
        return self.codificar(text_cifra)


if __name__ == "__main__":
    atbash = AtBash()

    codificar = atbash.codificar("aaaAAAHello World!")
    print(codificar)

    decodificar = atbash.decodificar(codificar)
    print(decodificar)
