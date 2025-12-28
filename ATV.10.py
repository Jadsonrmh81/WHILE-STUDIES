s = ""
while True:
    word = input('Enter a phrase: ').lower()

    if not all(part.isalpha() for part in word.split()):
        print('Just type strings.')
    elif word == s:
        print('Please, type something.')
    elif word == 'exit':
        print('Program finished.')
        break
    else:
        print(f'You typed {word}')
        print(f'Number of letters: {len(word)}')
