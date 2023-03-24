list = []
x = input()
for i in x:
    list.append(int(x))
s1 = list[1] + list[3] + list[5] + list[7]
list2 = [m*2 for m in list[::2]]
p = 0
s2 = 0
while p < 4:
   
    if len(str(list2[p])) > 1:
        s2 = s2 + int(str(list2[p])[0]) + int(str(list2[p])[1])
    else:
        s2 += list2[p]
    p += 1
sum = s1 + s2
if sum % 10 == 0:
    print("有效的")
else:
    print("无效的")
    

    


    







    
