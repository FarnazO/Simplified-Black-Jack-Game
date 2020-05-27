'''
This module contains the Chips class
'''
class Chips():
    '''
    This class sets the chips with an initial chip of 100 for each chip object
    It contains the following properties:
        - "total" wich is the total number of chips, initially it is set to 100
    It also contains the following methods:
        - "win_bet" which adds the won chips to the total existing chips
        - "lose_bet" which removes the lost chips from the total existing chips
    '''

    def __init__(self):
        '''
        Inititalises the chip object
        '''
        self.total = 100

    def win_bet(self, bet):
        '''
        Adds the beted chips to the total chips
        '''
        self.total += bet
        return self.total

    def lose_bet(self, bet):
        '''
        Takes away the beted chips from the total chips
        '''
        self.total -= bet
        return self.total
