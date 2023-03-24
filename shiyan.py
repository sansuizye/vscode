import math
def s(*args):
    m = 0
    sums = sum(args)/len(args)
    print(sums)
    for i in args:
        m =+ math.pow(i-sums,2)
        m = math.sqrt(m)
    s1 = m/len(args)
    return(s1)
print(s(15.40,15.44,15.34,15.41,15.38))
print(15.39+(0.0028*2.78)/math.sqrt(5))


        


    



