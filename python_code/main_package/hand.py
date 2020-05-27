'''
This is the deck module containing the Deck Class
'''
class Hand():
    '''
    This class describes the cards in each of the player's hands
    It contains three properties:
        - "cards" which is a list of card objects that are in that hand object
        - "value" which is the total value of the cards in the hand object
        - "aces" which is the total number of aces in the hand object
    It also contains two public methods:
        - "add_card" which adds the given card to the hand and checks for the aces in the hand
        - "adjust_for_ace" which depending on the total value of the hand chooses \
        whether ace should count as 1 or 11
    '''
    values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, \
                '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

    def __init__(self):
        '''
        Initialises the objects of this class (Hand) with the following default parameters
        '''
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        '''
        This method returns the cards in the hand and the total score of the hand
        '''
        cards_text = []
        for card in self.cards:
            cards_text.append(card.__str__())

        return cards_text, f"Total score: {self.value}."

    def __len__(self):
        '''
        This method returns the number of cards in the hand object
        '''
        return len(self.cards)

    def add_card(self, card):
        '''
        This method gets a card and adds it to the hand object. \
        It also updates the value of the hand and the number of aces in it.
        Input: a card object.
        '''
        self.cards.append(card)
        if card.rank == "Ace":
            self.aces += 1
            if self.aces == 2 and self.__len__() == 2:
                self.value = 21
            else:
                self.adjust_for_ace(card)
        else:
            self.value += self.values[card.rank]

    def adjust_for_ace(self, card):
        '''
        This method takes in a card object which is an ace and adjusts its value \
        based on the total value of the hand.

        Input: a card object which is ace
        '''
        if card.rank != "Ace":
            raise Exception("It is not an ace.")

        if self.value > 10:
            self.value += 1
        else:
            self.value += self.values[card.rank]
