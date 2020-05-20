'''
This module tests the methods of the Chips class
'''
import unittest
from main_package.chips import Chips

class TestChips(unittest.TestCase):
    '''
    This class contains the unit test for the methods in the Chips class
    '''
    def setUp(self):
        '''
        Sets the common variables used across all the unit tests
        '''
        self.chips = Chips()

    def test_the_initiation_of_the_chips_object(self):
        '''
        Test the initiation of the chip object
        '''
        self.chips.__init__()
        self.assertEqual(100, self.chips.total)

    def test_correct_chips_is_added_when_winning_the_bet(self):
        '''
        Test the correct number of chips is added when win_bet is called
        '''
        self.chips.win_bet(10)
        self.assertEqual(110, self.chips.total)

    def test_correct_chips_is_removed_when_winning_the_bet(self):
        '''
        Test the correct number of chips is removed when lose_bet is called
        '''
        self.chips.lose_bet(10)
        self.assertEqual(90, self.chips.total)

if __name__ == '__main__':
    unittest.main()
    