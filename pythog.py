for i in range(1,500):
    for j in range(i,500):
        for k in range(j,500):
            if i**2+j**2==k**2:
                print (f'{i},{j},{k}')
