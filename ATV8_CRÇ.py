while True:
    word = input('Type a word: ').lower() 

    if word.isalpha():
        break
    else:
        print('Just letters, please.')
        
vowels = 'aeiou'
count = 0

for letter in word:
    if letter in vowels:
        count += 1

print(f'The number of vowels in {word} is {count}.')

