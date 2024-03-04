# use Python's built-in random module to shuffle the deck of cards.
import random

# Card models a physical playing card.
class Card:
    ''' An individual card with a suit and rank. Defaults to faceup.
    
        Usage examples:
        
        >>> card = Card('♠', 'A')
        >>> str(card)
        'A♠'

        Cards can use any suite amd rank to accommodate different card games.

        >>> card = Card('@', 'c')
        >>> str(card)
        'c@'
    '''
    #Constructor method requires the suit and rank.
    # Faceup is an optional keyword parameter defaulting to: True
    def __init__(self, suit, rank, faceup=True):
        ''' The Card Constructor.
            Args:
                Suit    |   US card decks include spades, diamonds, hearts, and clubs. ♠ ♦ ♥ ♣
                rank    |   Us card decks include A 2 3 4 5 6 7 8 9 10 J Q K
                faceup  |   (optional) Cards facing up are displayed in the console.
        '''
        # Defining attributes for suit and rank.
        # For example.
        # ♠ 2
        self.suit = suit
        self.rank = rank
        # Cards can be either face up or face down in enough card games that a faceup attribute is included.
        self.faceup = faceup

    # Defining a __str__ is quite useful for console based apps
    def __str__(self):
        ''' The magic metho __str__ determines how this object is represented when converted to a str object.
            The str representation for this object is going to be different if the card is face up or facee down.
            Question marks are used if the card is face down
            Example:
            >>> str(Card('♠', '2', faceup=False))
            '??'
            >>> str(Card('♠', '2', faceup=True))
            '2♠'
        '''
        # Python supports coditional assignment using an inline if statemnt.
        rank = self.rank if self.faceup else '?'
        suit = self.suit if self.faceup else '?'
        # Python includes multiple ways to format strings.
        # the f in front of the below string literal makes the string into an f-string
        # F-strings are able to embed expressions insede curly brackets.
        # the result of the expression is renderd as a string.
        return f'{rank}{suit}'
    
    # Defining how this object will be represented when printed.
    def __repr__(self):
        ''' the magic method __repr__ determines how this object is represented when printed.
            example:
            >>> print(Card('♠', '2'))
            2♠
        '''
        # str(self) calls the above __str__ method and returns the response.
        # the __str__ magic method could also be called directly.
        # A common argument for useng self.__str__() instead of str(self) is the slight performance hit
        # which results from str(self) adding an extra Function Call.
        #
        # The intent of the __str__ magic method is to make it easy to convert object to a str.
        # the added readability of str(self) over self.__str__() is worth the likely unnoticed performce hit.
        # 
        # code is read more often than it's written.
        # Prioriteze readability over premature optimization.
        return str(self)
    
class Deck:
    ''' A deck based on a standard US card deck.

        Consistes of 13 possible card ranks from Ace to King.
        Consistes of  4 possible card suits: spade, diamond, heart, club.

        Create calss attributes containing suit and rank.
        Calling slit will creak these into a list
        the split function can be used to produce simple lists without the added visual clutter of the list syntax

        Example:        
        >>> assert ['♠', '♦', '♥', '♣'] == '♠ ♦ ♥ ♣'.split()

        either is fine. However, split can make some code easier to read.
    '''

    suits = '♠ ♦ ♥ ♣'.split()
    ranks = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

    def __init__(self):
        ''' Create a new deck consisting of one rank for each suit.
            Produces a new list using a list comprehension to loop over all of the ranks for each suit.

            Nested list comprehensions can be difficult to read at times. Epecially for new Python developers.

            The same result using a for loops:
            >>> suits = '♠ ♦ ♥ ♣'.split()
            >>> ranks = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
            >>> cards = []
            >>> for suit in suits:
            ...    for rank in ranks:
            ...        cards.append(Card(suit, rank))

            Verify that both approaches produce the same results.
            >>> cards 
            [A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♦, 2♦, 3♦, 4♦, 5♦, 6♦, 7♦, 8♦, 9♦, 10♦, J♦, Q♦, K♦, A♥, 2♥, 3♥, 4♥, 5♥, 6♥, 7♥, 8♥, 9♥, 10♥, J♥, Q♥, K♥, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣]
            
            >>> [Card(s,r) for s in Deck.suits for r in Deck.ranks]
            [A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♦, 2♦, 3♦, 4♦, 5♦, 6♦, 7♦, 8♦, 9♦, 10♦, J♦, Q♦, K♦, A♥, 2♥, 3♥, 4♥, 5♥, 6♥, 7♥, 8♥, 9♥, 10♥, J♥, Q♥, K♥, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣]
        '''
        self.cards = [Card(s,r) for s in self.suits for r in self.ranks]

    def shuffle(self):
        ''' Models the ability to shuffle a deck of cards.
            Uses the shuffle function from the random module.
        '''
        random.shuffle(self.cards)

    def deal(self, faceup=True):
        ''' Models the ability to deal a card.

            Example:
            
            >>> deck = Deck()

            the last card in the list is the "top" of the deck.
            >>> deck.cards[-1]
            K♣
            
            >>> card = deck.deal()
            >>> card
            K♣
            
            the dealt card is no longer in the list of cards.
            
            >>> deck.cards[-1]
            Q♣
            
            Deal a card facedown to test the display
            >>> card = deck.deal(faceup=False)
            >>> card
            ??
            
            Although the car is masked when displayed, its suit and rank are still accessible.
            >>> card.rank, card.suit
            ('Q', '♣')

        '''
        # pop removes a card from the deck
        card = self.cards.pop()
        # Ensure the card is correctly placed face up or down.
        card.faceup = faceup
        # Return the card.
        # Which is now removed from the deck and subject to being
        # Lost if now re-added before discarding.
        return card
    
    def __str__(self):
        ''' the magic metod __str__ determines how this object is represented when coverted to a str object.'''
        return ' '.join([f'{c.rank}{c.suit},' for c in self.cards])
    def __repr__(self):
        ''' the magic method __repr__ determines how this object is represeted when  printed.
            Example: 

            >>> print (Deck())
            A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♦, 2♦, 3♦, 4♦, 5♦, 6♦, 7♦, 8♦, 9♦, 10♦, J♦, Q♦, K♦, A♥, 2♥, 3♥, 4♥, 5♥, 6♥, 7♥, 8♥, 9♥, 10♥, J♥, Q♥, K♥, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣,
        '''
        return str(self)
    
    def __len__(self):
        ''' the Magic method __len__ determines how this object reponds to the built0in len fucniton.
            example:
            
            >>> len(Deck())
            52
        '''
        return len(self.cards)


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)