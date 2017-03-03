#extended euclid's gcd algorithm stolen from:https://e...content-available-to-author-only...s.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def extendedGCD(b, n):
    x0, x1, y0, y1 = 1,0,0,1
    while n!=0:
        q,b,n = b//n, n, b%n
        x0,x1 = x1, x0-q*x1
        y0,y1 = y1, y0-q*y1
    return (b,x0,y0)
 
#https://e...content-available-to-author-only...a.org/wiki/Modular_multiplicative_inverse#Extended_Euclidean_algorithm
#returns a^-1 s.t. a(a^-1) = 1 (mod m), or False if there doesn't exist a^-1
#ax = 1 (mod m)
#implies ax - 1 = mq, q is an integer
#implies ax - mq = 1
#use ext. gcd. to find x (q is not needed)
#returns false if gcd(a, m) == 1
def modInv(a, m):
    extGCD = extendedGCD(a, m)
    if extGCD[0] != 1: return False
    return extGCD[1] % m
 
#assumes all modulos are coprimes
def generalChineseRemainderThrm(remainders, modulos):
    M = 1
    for m in modulos:
        M *= m
    ratios = []
    for m in modulos:
        ratios.append(M//m)
    B = []
    for i in range(len(modulos)):
        B.append(modInv(ratios[i], modulos[i]))
    x = 0
    for i in range(len(modulos)):
        x += remainders[i]*B[i]*ratios[i]
    return x % M
 
#prime factorization: 13082761331670030=2×3×5×7×11×13×17×19×23×29×31×37×41×43
#factors = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]
#smallest possible solution provided by chinese remainder theorem
modulos = [11,10,9,7] #[2,3,5,7,11,13,17,19,23,29,31,37,41,43]
remainders = [6,3,4,0] #[1]*14
startingPt = generalChineseRemainderThrm(remainders, modulos)
print(startingPt)

