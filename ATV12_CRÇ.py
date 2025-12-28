l = []

while True:
    word = input('Enter words: ').lower()

    if word == '':
        print('Please, type words.')
    
    elif not all(part.isalpha() for part in word.split()):
        print('Just strings, please.')

    elif word == 'exit':
        print('Program finished.')
        break

    elif word == 'show':
        if len(l) == 0:
            print('List is empty.')
        else:
            print(l)
    elif word == 'clear':
        l.clear()
        print('List cleared.')
    
    else:
        l.append(word)
        print(f'"{word}" added to the list.')

# Regra da programação: executar -> validar -> decidir

#Regra mental:

# Não faça: 
#l.append(entrada)
   #if entrada é válida:

# Faça:
#if entrada é válida:
    #l.append(entrada)

# lembrete: a ordem das condições muda tudo.