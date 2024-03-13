def eight(size):
    for y in range(size):
        for x in range(size+1):
            if (y<=size//7-1 or y>=size-size//7) and (x!=size//2+1):
                print(' ', end='')
                
            elif (y==size//7 or y==size-(size//7+1)) and (x<=size//3 or x>=size-(size//3-1)):
                print(' ', end='')

            elif (y==size//7+1 or y==size-(size//7+2)) and (x!=size//7+3 and x!=size-(size//7+2)):
                print(' ', end='')

            elif (y==size//7+2 or y==size-(size//7+3)) and (x<=size//7 or x>=size-size//7+1 or x==size//7+2 or x==size//7+3 or x==size-size//7-1 or x==size-size//7-2):
                print(' ', end='')

            elif (y==size//7+3 or y==size-(size//7+4)) and (x<=size//7-1 or x>=size-size//7+2 or x==size//7+1 or x==size//7+2 or x==size-size//7-1 or x==size-size//7):
                print(' ', end='')

            elif (y==size//2+1 or y==size//2-1) and (x<=size//7-1 or x>=size-size//7+1 or x==size//7+1 or x==size//7+2 or x==size-size//7-1 or x==size-size//7-2):
                print(' ', end='')

            elif (y==size//2) and (x==size//7 or x==size-(size//7) or x==size//7+2 or x==size//7+3 or x==size-(size//7+2) or x==size-(size//7+3)):
                print(' ', end='')

            elif (y>=size//7+4 and y<=size//2-2) and (x<=size//7-2 or x==size//7 or x==size//7+1 or x>=size-size//7+2 or x==size-size//7-1 or x==size-size//7 or (x>=size//7*3 and x<size-size//7*3+1)):
                print(' ', end='')

            elif (y>=size//2+2 and y<=size-size//7-5) and (x<=size//7-2 or x==size//7 or x==size//7+1 or x>=size-size//7+2 or x==size-size//7-1 or x==size-size//7 or (x>=size//7*3 and x<size-size//7*3+1)):
                print(' ', end='')

            else:
                print('*', end='')

        print()

while True:
    try:
        size_input = int(input('Input your perfered size(odd number greater or equal to 3): '))
        if size_input<3 or size_input%2==0:
            print('Please input number that is greater or equal to 3!')
        else:
            break 
    except:
        print('Please input numeris value!')

sumbol_size=size_input*7
eight(sumbol_size)
