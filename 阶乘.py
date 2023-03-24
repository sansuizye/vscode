def jie(x):
    if x == 1:
        return 1
    else:
        return (2**(x-1)) * jie(x-1)
print(jie(3))