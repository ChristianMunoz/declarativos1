def numDigitos(n):
    if n/10==0:
        return 0
    return 1 + numDigitos(int(n/10))

print(numDigitos(123456789123))
