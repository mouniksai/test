l = list(map(str, input().split()))
leng = []

for i in l:
    leng.append(len(i))

x = leng
for j in range(0,len(x)-1):
    
        if x[j]>x[j+1]:
            x[j+1]=x[j]
        else:
           pass
y = leng.index(x[len(x)-1])
print(l[y])
