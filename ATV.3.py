n = 0

while True:
    num = int(input('Insert the number or "0" for exit: '))
    if num == 1: # this number is not included in the sum.
        print(f'You typed {num}. Program finished.')
        break

    n += num # add the values
print(f'The total sum is: {n}')

    
        

      