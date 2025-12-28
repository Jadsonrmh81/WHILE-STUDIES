while True:
    n = input('Insert a number (or "exit" to finish): ').lower()

    if n == 'exit':
        print('Program finished.')
        break
    elif not n.isdigit():
        print('Just numbers, please.')
    else:
        n = int(n)
        print(f'You typed {int(n)}')

    if n % 2 == 0:
        print(f'{n} is even.')
    else:
        print(f'{n} is odd.')