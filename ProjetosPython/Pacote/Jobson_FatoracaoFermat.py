#Fatoracao Fermat - Criptografia

from math import ceil,sqrt

def eh_quadrado(x):
    y = int(sqrt(x+0.5))
    return y*y == x

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

def fermat_factor(N):
    b2 = 3
    a=int(ceil(sqrt(N)))
    while not eh_quadrado(b2):
        b2 = a*a - N
        if( eh_quadrado(b2) ):
            b1 = int(sqrt(b2))
            c = a+b1
            if(c!=1 and c!=N):
                return c

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
   
numeroParaFatorar = 1601
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

print('Novo = ',fermat_factor(numeroParaFatorar))  
