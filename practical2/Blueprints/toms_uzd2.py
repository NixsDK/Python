for i in range(0, 21):
    if i==0 or i==1 or i==2 or i==20 or i==19 or i==18:
        print(' '*11, '*')
    elif i == 3 or i ==17:
        print(' '*8, '*'*7)
    elif i==4 or i==16:
        print(' '*6, '*', ' '*8, '*')
    elif i==5 or i==15:
        print(' '*4, '*', ' ', '*'*8, ' ', '*' )
    elif i==6 or i==14 or i==9 or i==11:
        print(' '*3, '*', ' ', '*'*10, ' ', '*')
    elif i==10:
        print('*'*3, ' *  ','*'*8,' * ', '*'*3 )
    else:
        print(' '*2, '*', ' ', '*'*4, ' '*2, '*'*4, ' ', '*')