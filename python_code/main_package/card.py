class Card():
    '''
    This is the Card class which produces a card object for a given rank and suit
    Inputs: 
    - rank:  a string representing the rank of a card. e.g. "Ace" or "Two"
    - suit:  a string representing the suit of a card. e.g. "Hearts" or "Spades"
    '''
    def __init__(self, rank, suit):
        '''
        Instantiates the Card object with the given rank and suit
        Input: rank and suit as string
        Output: card object with the specified rank and suit
        '''
        self.rank = rank
        self.suit = suit

    def __str__(self):
        '''
        Output: a statement showing the rank and suit of the card object
        '''
        return f"{self.rank} of {self.suit}"
