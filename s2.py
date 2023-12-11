a,b= map(str, input().split())
c,d=map(str,input().split())
e,f=map(str,input().split())
input()
c1=0
c2=0
c3=0
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]
for i in a:
    l1.append(i)
for x in b:
    l2.append(x)
for y in c:
    l3.append(y)
for z in d:
    l4.append(z)
for m in e:
    l5.append(m)
for n in f:
    l6.append(n)
for i1 in range(3):
    if int(l1[i1])+int(l2[i1])>9:
        c1+=1
    else:
        pass
print(c1)

for i2 in range(3):
    if int(l3[i2])+int(l4[i2])>9 :
        c2+=1
    else:
        pass
print(c2)

for i3 in range(3):
    if int(l5[i3])+int(l6[i3])>9:
        c3+=1
    else:
        pass
print(c3)



