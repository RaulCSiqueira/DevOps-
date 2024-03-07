from random import randint

class GameOver(Exception): ...

def parse_guess() -> int:
    try:
        if (guess := input('guess a number between 1 and 10 > ')).lower() == 'q':
            raise GameOver
        return int(guess)
    except ValueError:
        print('Your guess must be a valid interger. ')
        return parse_guess()
    
def play():
    print('press Q to quit.')

    try:
        while True:
            answer = randint(1,10)

            while parse_guess() != answer:
                print('try again.')
            else:
                print('you win!')

    except GameOver:
        print('tranks for playing!')
    finally:
        print('like and subscribe!')

if __name__ == '__main__':
    play()