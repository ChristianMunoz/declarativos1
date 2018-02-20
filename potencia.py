def pot(n,m):
    if m==0:
        return 1
    if m==1:
        return n
    return n*(pot(n,m-1))
print(pot(10,3))
