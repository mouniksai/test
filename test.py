a = open("magic_numbers.txt",'w')
a.write('123456 234567 345678 456789 567890 678901 789012 890123 901234 123789')
a.close()
b= open("magic_numbers.txt",'r')
l = b.read().split()
def compute_recursive_sum(a):
    if len(a)==1:
        return int(a[0])
    else:
        return int(a[0])+ compute_recursive_sum(a[1:])
        
rec_sum=compute_recursive_sum(l)
def compute_power_sum(b):
    if len(b)==1:
        return (b[len(b)-1])**(l1.index(b[0]))
    else:
        return int(b[0])**(l1.index(b[0]))+ compute_power_sum(b[1:])
l1=[]
temp =rec_sum
for  i in range(7):
    l1.append(temp%10)
    temp = int(temp/10)
print('The recursive sum of the numbers is ',compute_recursive_sum(l))

print('the power sum of the recursive sum is',compute_power_sum(l1))
    
    


