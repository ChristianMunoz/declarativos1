def prod(n,m):
    if m==0:
        return 0
    if m==1:
        return n
    return n+prod(n,m-1)


print(prod(5,5))
