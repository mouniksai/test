str ="hi friends how are you i am in goa"
str2 = ""

for x in range(0,len(str)):
    if(str[x] in ['a','e','i','o','u']):
     str2 = str2 + str[x].upper()
    else: 
     str2 = str2 +str[x]

print(str2) 
 