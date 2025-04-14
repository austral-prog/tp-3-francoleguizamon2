def check_vowels():
    name = str(input('Enter name: ')).lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in vowels:
        if letter in name:
            print('Contiene', letter + ':', True)
        else:
            print('Contiene', letter + ':', False)
check_vowels()
