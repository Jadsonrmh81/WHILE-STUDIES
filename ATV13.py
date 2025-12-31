l = []

while True:
    user = input('Enter words (the same word only 3 times): ')
    if user == '':
        print('Empty input.')
    elif not all(part.isalpha() for part in user.split()):
        print('You can just type words.')

    elif user == 'show':
        print(l)
    elif user == 'clear':
        l.clear()
        print('List cleaned.')    

    elif l.count(user) == 2:
        print('Word blocked.')
        print(f'All the words typed: ',l)
        break
    else:
        l.append(user)
        print(l)


