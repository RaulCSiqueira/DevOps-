answer = 9

while True:
    guess = int(input('Guess a number between 1 and 10: '))
    
    if guess == answer:
        print('You got it correct! yay!')
        break
    else:
        print('Sorry, try again')