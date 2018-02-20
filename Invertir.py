def numDigitos(n):
    if n<10:
        return 1
    return 1 + numDigitos(int(n/10))

def pot(n,m):
    if m==0:
        return 1
    if m==1:
        return n
    return n*(pot(n,m-1))

def invertir(n):
    if numDigitos(n)==1:
        return n
    return (n%10)*pot(10,(numDigitos(n)-1))+invertir(int(n/10))

print(invertir(59846))
print numDigitos(59846)
print pot(2,4)
