void = ''

while True:
    ask = input('Type a word: ')
    if ask == void:
        print('Type a word, please. ')
        
    elif not all(part.isalpha() for part in ask.split()):
        print('Just strings, please.')
    else: 
        print(f'You typed {ask}')
        print(f'The number of words is {len(ask)}')
        break