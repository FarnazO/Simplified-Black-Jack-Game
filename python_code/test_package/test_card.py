'''
This it the unit test module for the Card class.
'''
import unittest
from main_package.card import Card

class TestCard(unittest.TestCase):

    '''
    This is the unit test class for Card() class in card.py
    '''
    def test_correct_card_returned_given_a_suit_and_rank(self):
        '''
        This function is testing :
         1. The correct card object is created for a given rank and suit and
         2. the definition of __str__ inside the Card class.
        '''
        rank = "Two"
        suit = "Hearts"
        sample_card = Card(rank, suit)
        actual_result = sample_card.__str__()
        self.assertEqual(actual_result, "Two of Hearts")

if __name__ == '__main__':
    unittest.main()
