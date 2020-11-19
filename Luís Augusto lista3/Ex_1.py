from unicodedata import normalize
def main():
    original = input('insira uma palavra: ')
    
    palavra = original.lower().replace(' ', '')
    palavra = normalize('NFKD', palavra).encode('ASCII','ignore').decode('ASCII')
    palavra = ''.join([char for char in palavra if char.isalpha()])
    
    e_palindrome = palavra == palavra[::-1]
    print('{}{} é um palindrome'.format(original,
                                        (' não' * (not e_palindrome))))


if __name__ == '__main__':
    main()

        
