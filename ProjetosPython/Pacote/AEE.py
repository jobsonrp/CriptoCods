def AEE(valor1, valor2): # Resulta no MDC entre valor1 e valor2, mais os fatores de Euclides
    x0,x1,y0,y1 = 1,0,0,1 # Matriz Identidade
    mdc = valor1
    n = valor2
    while n!=0:
        q,mdc,n = mdc//n, n, mdc%n # n1 // n2 => parte inteira da divisão de n1 por n2
        x0,x1 = x1, x0-q*x1
        y0,y1 = y1, y0-q*y1
    return (mdc,x0,y0)

print('ALGORITMO DE EUCLIDES ESTENDIDO ')
print('Este código calcula o MDC(a,b) e os fatores de Euclides "x" e "y". ')
print('Onde: MDC(a,b) = d = ax + by ')
print('')
a = int(input('Digite o valor de "a": '))
b = int(input('Digite o valor de "b": '))
print('')
d,x,y = AEE(a,b)
print('Resultado: MDC(%d,%d) = %d = %d*(%d) + %d*(%d) ' % (a,b,d,a,x,b,y))
print('Onde: x = %d e y = %d ' % (x,y))