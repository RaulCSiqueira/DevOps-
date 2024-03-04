def remover_espacos_especiais(frase):
    caracteres_especiais = "!@#$%^&*()-+?_=,<>/."
    frase_sem_especiais = frase.replace(" ", "")
    for char in caracteres_especiais:
        frase_sem_especiais = frase_sem_especiais.replace(char, "")
    return frase_sem_especiais

def is_palindrome_word(word: str) -> bool:
    if word == word[::-1]:
        print('é um polindrome')
        return 
    else:
        return

def is_palindrome_phrase(phrase: str) -> bool:
    if phrase == phrase[::-1]:
        print('a frase é um palindrome')
        return 
    else:
        print('Frase não é um polindrome')
        return 


for tentativa in range(4):
    word1 = input(str('vai ser uma palavra escreve word e se caso for frase escreva phrase: '))
    if word1 == 'word':
        word2 = input('escreva a uma palavra para ver se é um palindrome: ')
        word = word2.lower()
        is_palindrome_word(word)
            
    elif word1 == 'phrase':
        phrase2 = input('Escreva a frase que possa ser um palindrome: ')
        phrase1 = phrase2.lower()
        phrase = remover_espacos_especiais(phrase1) 
        is_palindrome_phrase(phrase)       