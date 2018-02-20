def sumDigitos(n):
    if n==0:
        return n
    return n % 10 + int(sumDigitos(n/10))

print(sumDigitos(123456789))
