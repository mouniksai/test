yr = int(input('enter the year to test'))
if yr%100!=0:
    if yr%4==0:
        print(f'{yr} is a leap year')
    else:print(f'{yr} is not a leap year')
elif yr%400 == 0:
    print(f'{yr} is a leap year')
else:print(f'{yr} is not a leap year')
