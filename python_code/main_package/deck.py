'''
This is the deck module containing the Deck() class
'''
import random
from .card import Card

class Deck():
    '''
    This class creates a deck of 52 cards when called.
    It has the following properties:
        "cards" which is the list containing all the cards present in the deck
        "suits" which is a list of all possible suits for a complete deck
        "ranks" which is a list of all possible ranks for a complete deck
    It has the following methods:
        "shuffle" method which shuffles the cards inside the deck when called.
        "deal" method which deals two cards to the player and two cards to the player of black jack
        "get_top_card" method which returns the top card on the deck
        "__str__" which returns the cards present in the deck
        "__len__" which returns the total number of cards left in the deck
    '''
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',\
             'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    def __init__(self):
        '''
        Initialises the deck object by creating 52 cards of a playing card deck
        '''
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(rank, suit))

    def __str__(self):
        '''
        This method returns the existing cards in the deck object
        '''
        cards_text = []
        for deck_card in self.cards:
            cards_text.append(deck_card.__str__())
        return cards_text

    def __len__(self):
        '''
        This method returns the number of existing cards in the deck
        '''
        return len(self.cards)

    def shuffle(self):
        '''
        Uses the random library to shuffle the cards in the deck
        '''
        random.shuffle(self.cards)

    def deal(self):
        '''
        This method deals two cards (first two cards of the deck) to the player and \
        two cards (second two cards of the deck) to the dealer.
        Output: a tuple containing two lists; first list has the cards for the player \
        and the second list has the cards for the dealer
        '''
        player_cards = self.cards[0:2]
        dealer_cards = self.cards[2:4]
        for _ in range(0, 4):
            self.cards.pop(0)
        return player_cards, dealer_cards

    def get_next_card(self):
        '''
        This method returns the next card in the deck.
        Output: a card object
        '''
        next_card = self.cards[0]
        self.cards.pop(0)
        return next_card
