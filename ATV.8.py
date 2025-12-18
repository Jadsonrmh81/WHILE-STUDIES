while True:
    for i in range(1,6):
        l = input('Type the vogels: ')       
        
    ask = input('Insert the word: ').lower()
    
    if not all(part.isalpha() for part in ask.split()):

        print('Just strings, please.')
    else:
        
        print(f'You typed {ask}')
        break
if l in ask:
    print(f'Number of vowels: {l}')
else:
    print('Any vowel.')






        
        
