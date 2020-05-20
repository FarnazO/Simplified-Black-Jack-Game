'''
This module contains the unit tests needed for the Hand() class
'''
import unittest
from main_package.hand import Hand
from main_package.card import Card

class TestHand(unittest.TestCase):
    '''
    This class contains the unit test methods for the Hand class
    '''

    def setUp(self):
        '''
        Sets up the common variables used across all the unit tests
        '''
        self.test_hand = Hand()

    def test_when_hand_object_is_initalised_it_is_empty(self):
        '''
        Test the initialisation of the hand object
        '''
        self.test_hand.__init__()
        self.assertEqual(0, self.test_hand.value)
        self.assertEqual(0, self.test_hand.aces)
        self.assertEqual([], self.test_hand.cards)

    def test_when_str_is_called_correct_output_is_returned(self):
        '''
        Test the __str__ method of the Hand class
        '''
        expected_result = ([], "You have a total score of 0.")
        actual_result = self.test_hand.__str__()

        self.assertEqual(expected_result, actual_result)

    def test_when_len_is_called_length_of_hand_is_returned(self):
        '''
        Test the __len__ method defined in Hand class
        '''
        expected_result = 0
        actual_result = len(self.test_hand)
        self.assertEqual(expected_result, actual_result)

    def test_the_correct_card_is_added_when_add_card_is_called(self):
        '''
        Test the add_card method in Hand class
        '''
        expected_cards_in_hand = [Card("Ace", "Hearts"), Card("Ace", "Spades")]
        expected_value = 21
        expected_hand_length = 2

        self.test_hand.add_card(expected_cards_in_hand[0])
        self.test_hand.add_card(expected_cards_in_hand[1])

        self.assertEqual(expected_cards_in_hand, self.test_hand.cards)
        self.assertEqual(expected_value, self.test_hand.value)
        self.assertEqual(expected_hand_length, len(self.test_hand))

    def test_the_correct_value_of_ace_is_used_when_total_hand_value_is_9(self):
        '''
        Test the adjust_for_ace method in the Hand class when the total value of hand is 9
        '''
        expected_value = 20
        self.test_hand.value = 9
        self.test_hand.adjust_for_ace(Card("Ace", "Hearts"))

        self.assertEqual(expected_value, self.test_hand.value)

    def test_the_correct_value_of_ace_is_used_when_total_hand_value_is_17(self):
        '''
        Test the adjust_for_ace method in the Hand class when the total value of hand is 17
        '''
        expected_value = 18
        self.test_hand.value = 17
        self.test_hand.adjust_for_ace(Card("Ace", "Hearts"))

        self.assertEqual(expected_value, self.test_hand.value)

    def test_an_error_is_raised_when_a_card_other_than_ace_is_used_with_adjust_for_ace(self):
        '''
        Test the adjust_for_ace method in the Hand class when a card other than an ace is used.
        '''
        with self.assertRaises(Exception) as context:
            self.test_hand.adjust_for_ace(Card("Two", "Hearts"))
            
        self.assertEqual("It is not an ace.", str(context.exception))

if __name__ == '__main__':
    unittest.main()
