while True:
    ask = int(input('Insert a number between 1 and 10: '))
    if ask <1 or ask >10:
        print('Please, insert again.')
    else:
        print(f'Valid number! You typed: {ask}')
        break
        
