#Fatoracao Fermat - Criptografia

from math import ceil,sqrt

def isPrimo(n):
    if(n==1): return 1;
    elif( n< 4): return 1;
    elif( n%2 ==0): return 0;
    elif( n< 9): return 1;
    elif( n%3 ==0): return 0;
    else:
        r = int(sqrt(n))
        f = 5;
        while( f<=r):
            if(n%f==0): return 0;
            if(n%(f+2)==0): return 0;
            f=f+6
    return 1;

def isSquare(num):
    if ( sqrt(num) % 1 == 0):
        return True
    return False
    
def fermatFactor(N):
    if (N%2==0): return [2,N/2]
    raiz = sqrt(N)
    a = ceil(raiz)
    while not isSquare(a**2-N):
        a = a + 1
    b = sqrt(a**2-N)
    return [a - b,a + b]
   
numeroParaFatorar = 101561
if numeroParaFatorar <= 0:
    print('Número digitado foi: "',numeroParaFatorar,'". Nao pode ser calculado, pois é <= 0.')
else:
    result = fermatFactor(numeroParaFatorar)
    print('parcelas = ',result)
    prova = int(result[0])*int(result[1])
    print('prova = ',prova)

    if (numeroParaFatorar == prova):
        print('Prova OK!!')
    else:
        print('Erro!')

print(isPrimo(numeroParaFatorar))

