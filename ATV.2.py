while True:
    ask = int(input('Insert the right password: '))
    if ask == 2026:
        print(f'You typed {ask}. Program finished.')
        break
    else:
        print('Wrong password. Try again.')