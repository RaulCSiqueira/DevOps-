# Imports the built-in os module to clear the screnn
import os
# Imports the card and Desk from the cards module
from cards import Card, Deck

class GameOver(Exception):
    ''' An exception raised when the player is out of money.
        Exemple:
        
        >>> raise GameOver('Better Luck next time!')
        Traceback (most recent call last):
        ...
        GameOver: Better Luck next time!
    '''

class Player:
    ''' Represents a blackhacj player - which includes a dealer.
        
        Ensure that the player class includes sttrs for cads and money.
        And that they are the expected default values.
        >>> player = Player()
        
        A new player shouldn't have any cards.
        >>> len(player.cards)
        0
        
        A new player should have $1000
        >>> player.money
        1000
    '''
    def __init__(self):
        self.money= 1_000
        self.cards = []

def prompt_for_bet(money: int) -> int:
    ''' Continuously prompt for a numeric bet until provided.'''
    try:
        #positive bets only. Don't allow a player to bet -1_000_000 and then intentionally lose.
        # that would be an expensive mistake. :)
        # If the user supplied bet balue cannot be converted into an int hte built-in ValuError is raised.
        return abs(int(input(f'How much of Your ${money} would you like to wager?')))
    except ValueError:
        print('Your bet must be an integer. Example: 42')
        # try it again after informing the user to enter an integer
        return prompt_for_bet(money)
    except:
        # Any other exceptions should be re-raised to allow
        # the calling code a chance to resolve the problm.
        raise

def score(cards: list[Card]) -> int:
    ''' Calculate the score for the set of cards.

        Create some cards to use for testing the score.
        >>> _k = Card('♠', 'K') 
        >>> _a = Card('♠', 'A')
        >>> _2 = Card('♠', '2')
        >>> _3 = Card('♠', '3')
        >>> _5 = Card('♠', '5')

        >>> assert score([_k, _a]) == 21
        >>> assert score([_k, _a, _a]) == 12
        >>> assert score([_2, _3, _5]) == 10
    '''
    # Create a point value lookup using a dictionary.
    # Aces can be used as either a 1 or an 11. 
    # This lookup sets the default as 11.
    scores = {
        'A': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
    }
    # Calculate the score assuming the ace is 11.
    score = sum([scores[card.rank] for card in cards]) or 0
    # Adjust the score if needed to allow aces to be used as 1.
    for card in cards:
        # If the score is greater than 21 and at least one of the
        # cards is an ace then we can turn the ace into a 
        # 1 by subtracting 10 from the score
        if  score > 21 and card.rank == 'A':
            score -= 10
    return score

def format_winner(winner: str) -> str:
    ''' Format the message displayer to the winner and return the str.
        
        >>> assert 'A Robot wins!' in format_winner('a robot')
        >>> assert 'A Human wins!' in format_winner('a human')
    '''
    winner = f'{winner.title()} wins!'
    winner = f'{winner:@^80}' # Center test inside an 80 chacacter sapce.
    return winner

def format_cards(player: Player, dealer: Player) -> str:
    ''' Displays the cards for the player and dealer. '''
    cards = f'{"dealer":-^80}\n'
    cards += f'{" ".join([str(card) for card in dealer.cards])}\n'
    cards += f'{"player":-^80}\n'
    cards += f'{" ".join([str(card) for card in player.cards])}\n'
    cards += f'{"total: {}".format(score(player.cards)): ^80}'
    return cards

def clear_screen():
    ''' Clear the terminal screen using either cls on Windows otherwise clear. 

        The double pipe operator || on Linux and Windows is used to 
        attempt the first command and fallback to the second.

        So cls||clear attempts cls and if a non-zero status code is returned clear is attempted.
    '''
    os.system('cls||clear')


def play_round(player: Player, dealer: Player, deck: Deck, action_callable: callable = input, bet_callable: callable = prompt_for_bet):
    ''' Play a single round of blackjack. 

        Args:
            player          | The player
            dealer          | The dealer
            deck            | The deck of cards to use
            action_callable | Callable used to prompt a user for an action.
                            |> The callable must accept 1 positional str argument representing the prompt to display to a player.
                            |> The callable must return a str representing the symbol for the desired action.
                            |>  -----------------
                            |> | action | symbol |
                            |>  -----------------
                            |> |   hit  |    h   |
                            |> |  stand |    s   |
                            |>  -----------------
            bet_callable    | Callable used to prompt a user for their bet.
                            |> The callable must accept 1 positional int argument representing a player's available money.
                            |> The callable must return a positive int representing the bet.


        ------------------- Warning -------------------
        This function mutates the provided arguments 
        and will leave them in a non-deterministic state.
        -----------------------------------------------
        
        Calling this function when a player is out of money should raise a GameOver exception.
        >>> player = Player()
        >>> player.money = 0
        >>> play_round(player, Player(), Deck())
        Traceback (most recent call last):
            ...
        GameOver: Game over! You're bankrupt!

        Calling this function when a player has sufficient funds and a winning hand.
        >>> test_bet_callable = lambda n: 100
        >>> test_act_callable = lambda s: 's'
        >>> player = Player()
        >>> dealer = Player()
        >>> deck = Deck()
        >>> deck.cards = [Card('♠', 'K'), Card('♠', 'A'), Card('♥', 'K'), Card('♥', 'Q')]
        >>> play_round(player, dealer, deck, test_act_callable, test_bet_callable)
        -------------------------------------dealer-------------------------------------
        Q♥ ??
        -------------------------------------player-------------------------------------
        A♠ K♠
                                           total: 21                                    
        -------------------------------------dealer-------------------------------------
        Q♥ K♥
        -------------------------------------player-------------------------------------
        A♠ K♠
                                           total: 21                                    
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Player wins!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        >>> assert player.money == 1200

        Calling this function when a player has sufficient funds and a losing hand.
        >>> deck.cards = [Card('♠', '2'), Card('♠', 'A'), Card('♥', 'K'), Card('♥', 'Q') ]
        >>> play_round(player, dealer, deck, test_act_callable, test_bet_callable)
        -------------------------------------dealer-------------------------------------
        Q♥ ??
        -------------------------------------player-------------------------------------
        A♠ 2♠
                                           total: 13                                    
        -------------------------------------dealer-------------------------------------
        Q♥ K♥
        -------------------------------------player-------------------------------------
        A♠ 2♠
                                           total: 13                                    
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Dealer wins!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        >>> assert player.money == 1100

        Ensure that we're not losing cards that aren't being put back in the deck after a round.
        >>> assert len(deck.cards) == 4

    '''
    # Step 1 
    # Ensure the player has enough money to play. If not, game over!
    if player.money == 0:
        raise GameOver("Game over! You're bankrupt!")

    # Begin the round by resetting the clearing the player and dealer's cards.
    dealer.cards = []
    player.cards = []

    # Step 2
    # The round opens by prompting the player for a bet. 
    # Until we have a bet we can't do anything else. 
    # Ensure that the player has enough money to place the bet.
    while (rounds_wager := bet_callable(player.money)) > player.money:
        print(f'please change your bet. you bet ${rounds_wager}. you only have ${player.money}.')
    
    # Step 3
    # Deal two cards for the delaer. One needs to be face up
    dealer.cards = [deck.deal(), deck.deal(faceup=False)]
    # Deal two cards for the player
    player.cards = [deck.deal() for _ in range(2)]
    # Rendedr the cards to the console.
    clear_screen()
    print(format_cards(player, dealer))

    # Step 4
    # The player needs to determine their next action. 
    # Will they hit or stand? 
    # By typing an s they'll stand.
    # By typing an h they'll hit.
    # Anything else will be ignored.
    while (action := action_callable('pick your action: (h)it (s)tand > ')) != 's':
        if action == 'h':
            # take another card for the player
            player.cards.append(deck.deal())
            # Everytime a player's cards change we need to render the cards.
            clear_screen
            print(format_cards(player, dealer))
    # Step 5
    # The dealer in a real game would determine for themself if they want to hit or stand.
    # We're going to create some basic rules to simulate a real person as the dealer.
    # While the score of the dealer's hand is less than 17 keep taking cards.
    while score(dealer.cards) < 17:
        dealer.cards.append(deck.deal())
    # STEP 6
    # Determine who won by comparing scores. 
    # if the player scored 21 then they win. 
    # if the dealer scored more than 21 the player wins.
    # if the player scores higher than the dealer and they didn't go over 21 then the player wins.
    dealers_score = score(dealer.cards)
    players_score = score(player.cards)

    # Who won ...
    # This logic does not fully align with the actual rules of blackjack.
    if (players_score == 21 or dealers_score > 21 or (players_score >= dealers_score and players_score <= 21)):
        player.money += rounds_wager * 2
        winner = 'player'
    else:
        player.money -= rounds_wager
        winner = 'dealer'
    # STEP 7 
    # Display all the cards, including the dealer's previously hidden cards.
    # First need to make them faceup.
    # Then the next time display is called it'll show all cards.
    for card in dealer.cards:
        card.faceup = True

    clear_screen()
    print(format_cards(player, dealer))
    # Inform the player who won.
    print(format_winner(winner))

    # STEP 8 
    # Return the cards to the deck to prevent card-loss
    # Having played a round re-add the cards to the deck.
    # This likely breaks official game play rules or something.
    # However, it's how this functions. :P
    deck.cards += player.cards
    deck.cards += dealer.cards

def play():
    ''' Continuously play until the player stop the code.'''
    player = Player()
    dealer = Player()
    deck = Deck()

    # Loop forever unsless the code is insterrupteds by CTRL+C
    while True:
        deck.shuffle()
        play_round(player, dealer, deck)

# If This code is being run as a script, play the game.


# Add class and function definitions above this line.
if __name__ == '__main__':
    # Typically imports are added to the top of the file.
    # However, sometimes adding an import near where the imported
    # objects are used has value.
    #
    # In this case these two modules are only used if this is run as a script.
    import argparse
    import doctest
    parser = argparse.ArgumentParser(description='Play a game of blackjack.')
    parser.add_argument('--test', action='store_true')

    if parser.parse_args().test:
        doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL, verbose=True)
    else:
        try:
            play()
        except GameOver as go:
            print(go)