def euclides_mdc(dividendo, divisor): #maximo divisor comum pelo metodo de euclides
    while divisor != 0:
        temp = divisor
        divisor = dividendo % divisor
        dividendo = temp    
    return dividendo

def euclides_recursivo_mdc(dividendo, divisor):
    if divisor == 0:
        return dividendo
    else:
        return euclides_recursivo_mdc(divisor, dividendo % divisor)

def AEE(valor1, valor2):
    x0,x1,y0,y1 = 1,0,0,1 # Matriz Identidade
    mdc = valor1
    n = valor2
    while n!=0:
        q,mdc,n = mdc//n, n, mdc%n # n1 // n2 => parte inteira da divisão de n1 por n2
        x0,x1 = x1, x0-q*x1
        y0,y1 = y1, y0-q*y1
    return (mdc,x0,y0)

def inverso_modular(a,n):
    return (a**(n-2)%n)

def primitiva (a,p):
    restos=[(a**n)%p for n in range (p-1)]
    return (restos)

print('euclides_mdc_extendido = ',AEE(11, 10))
print('euclides_mdc = ',euclides_mdc(348, 156))
print('euclides_recursivo_mdc = ',euclides_recursivo_mdc(348, 156))
print('primitivas = ',primitiva(3,5))
print('inverso_modular(10,3) = ',inverso_modular(10,3))


