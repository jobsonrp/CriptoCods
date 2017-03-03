def AEE(valor1, valor2):
    x0,x1,y0,y1 = 1,0,0,1 # Matriz Identidade
    mdc = valor1
    n = valor2
    while n!=0:
        q,mdc,n = mdc//n, n, mdc%n # n1 // n2 => parte inteira da divisão de n1 por n2
        x0,x1 = x1, x0-q*x1
        y0,y1 = y1, y0-q*y1
    return (mdc,x0)

def inversoMultiplicativo(a, P): # Inverso Multiplicativo de "a" mod "P" = x, onde "a*x = 1 mod P"
    mdc,x0 = AEE(a, P)
    if mdc != 1: return False
    return x0 % P

print(inversoMultiplicativo(630,11)) 