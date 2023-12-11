N = int(input('enter the value of end for the series'))
sum = 0
n1=0
n2=1
while n2<N:
    print(n1)
    print(n2)
    sum = n1 + n2
    n1 = sum
    n2 += sum
    