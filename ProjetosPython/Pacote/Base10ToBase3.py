def ternary(n):
    if n == 0:
        return ''
    else:
        e = n//3
        q = n%3
        return ternary(e) + str(q)
    
print(ternary(26))