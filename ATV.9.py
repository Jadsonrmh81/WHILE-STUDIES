while True:
    ask = input('Write a phrase: ').lower()
    
    if ask == 'exit': # If you want to fisish the loop without show 'exit', this is the sintax
        print('Program finished.')
        break
    else:
        print(f'You typed {ask}')
        print(f'Number of letters: {len(ask)}')   
 


