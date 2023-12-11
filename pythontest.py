str ="hi friends how are you i am in goa"
l = list(str)
str2 = " "

for x in range(0,len(l)):
    if(l[x] in ['a','e','i','o','u']):
     str2 = str2 + l[x].upper()
    else: 
     str2 = str2 +l[x]
print(str2) 
 