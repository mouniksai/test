l = list(map(str, input().split()))
print(l)
count = 0
for i  in l:
    for j in l:
        if i == j:
            count +=1
            if count>2:
                l.remove(j)
                count=0
        else: pass
print(l)