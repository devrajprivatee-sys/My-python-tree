year = int(input())

if year%100==0:
    if year%400==0:
        print('Leap')
    else:
        print('Non-Leap')
else:
    if year%4==0:
        print('Leap')
    else:
        print('Non-Leap')
#done and dusted
