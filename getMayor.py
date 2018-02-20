def getMayor(n):
    if n<10:
        return n
    if n%10>getMayor(int(n/10)):
        return n%10
    return getMayor(int(n/10))
print(getMayor(246897531))
