def div(n,m):
    if m==0:
        return "indeterminado"
    if n==0:
        return 0
    return 1+div(n-m,m)
print div(40,4)
