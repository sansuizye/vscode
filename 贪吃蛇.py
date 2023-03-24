def getscore():
    import random
    global x
    x = [random.randint(0,100) for i in range(100)]
    return x
def chargescore(y):
    if y < 60:
        return("不及格")
    elif y >= 60 and y < 70:
        return("及格")
    elif y >= 70 and y < 80:
        return("中等")
    elif y >= 80 and y < 90:
        return("良好")
    else:
        return("优秀")
def grade_count():
    b = list(map(chargescore,x))
    lis = ["优秀","良好","中等","及格","不及格"]
    lis2 = [b.count(j) for j in lis]
    out = {k:v for k,v in zip(lis,lis2)}
    print(out)
def display():
    getscore()
    grade_count()
    return




