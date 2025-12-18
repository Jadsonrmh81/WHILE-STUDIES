while True:
    word = input('Type the secret word: ').lower()
    
    if not all(part.isalpha() for part in word.split()):
        print('Just strings, please. Try again.')

    elif word == 'python':
        print('Correct word!')
        break
    else:
        print(f'Is not {word}. Try again.')
    

   
        
        


