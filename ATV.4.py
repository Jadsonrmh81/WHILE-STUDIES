print('1 - Say Hello')
print('2 - Say Bye')
print('0 - Exit')

while True:
    ask = int(input('Choise an option: '))
    if ask == 1:
        print('Hello!')
    elif ask == 2:
        print('Bye!')
    elif ask == 0:
        print(f'You typed {ask}. Program finished.')
        break
    else: # else in the final of all conditionals
        print('Invalid option. Try again.')
        
    