# The built-in random module includes objects used for generating
# random data in different formats.
import random
# Create a random number for the player to guess.
answer = random.randint(1, 20)

def play():
    # The use of the "walrus" operator allows a name to be bound inside of an expression.
    # The result is more concise code 
    # The walrus operator was introduced in Python 3.8.
    while (guess := int(input('guess a number between 1 and 20 > '))) != answer:
        if guess > answer:
            print('too high')
        elif guess < answer:
            print('too low')
    # while loops run until some condition is True. 
    # This while loop runs until the guess and answer match.
    # while loops can include an else clause which runs when 
    # the condition becomes False.
    else:
        print('correct!')

if __name__ == '__main__':
    play()