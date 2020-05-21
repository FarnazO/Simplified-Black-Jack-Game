'''
This module contains the test class for testing the Game() class.
'''
import unittest
from mock import patch
from main_package.game import Game
from main_package.chips import Chips
from main_package.hand import Hand
from main_package.deck import Deck
from main_package.card import Card

class TestGame(unittest.TestCase):
    '''
    This class contains the unit tests for testing the Game class
    '''
    def setUp(self):
        '''
        This method sets up the common variables for all the \
        unit tests in this module
        '''
        self.game = Game()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.card_deck = Deck()
    def test_the_game_object_is_initiated_correctly(self):
        '''
        Test that the game object is initiated correctly
        '''
        self.game.__init__()
        self.assertEqual(True, self.game.playing)
    def test_take_bet_method_when_the_users_bet_is_accepted(self):
        '''
        Test the take_bet method in the game class when the player successfully place their bet.
        '''
        example_chip = Chips()
        placed_bet = 5
        with patch('builtins.input', return_value=placed_bet): \
        # Mocking the return of the built-in input method
            output_bet = self.game.take_bet(example_chip)
            self.assertEqual(placed_bet, output_bet)
    def test_take_bet_method_when_the_users_bet_is_over_their_available_chips(self):
        '''
        Test the take_bet method in the game class when the player place a bet higher than\
        their chips and then fix it.
        '''
        example_chip = Chips()
        placed_bet = 6
        with patch('builtins.input', return_value=500): \
        # Mocking the return of the first built-in input method
            with patch('builtins.input', return_value="N"): \
            # Mocking the return of the second built-in input method
                with patch('builtins.input', return_value=placed_bet): \
                # Mocking the return of the last built-in input method
                    output_bet = self.game.take_bet(example_chip)
                    self.assertEqual(placed_bet, output_bet)    
    def test_that_hit_method_adds_a_new_card_to_the_hand(self):
        '''
        Tests the hit method which adds a new card to the hand
        '''
        self.game.hit(self.card_deck, self.player_hand)
        self.assertEqual(1, self.player_hand.__len__())
    def test_when_user_chooses_to_hit_a_card_is_added(self):
        '''
        Test the hit_or_stand method when the player chooses hit.
        '''
        with patch('builtins.input', return_value="h"):
            with patch.object(self.game, 'hit') as hit_mock:
                self.game.hit_or_stand(self.card_deck, self.player_hand)
            hit_mock.assert_called_with(self.card_deck, self.player_hand)
    def test_when_user_chooses_to_stand(self):
        '''
        Test the hit_or_stand method when the player chooses hit.
        '''
        with patch('builtins.input', return_value="s"):
            self.game.hit_or_stand(self.card_deck, self.player_hand)
            self.assertEqual(False, self.game.playing)
    def test_show_some_method(self):
        '''
        Test the show_some method.
        '''
        with patch.object(__builtins__, 'print') as mock_print:
            self.game.show_some(self.player_hand, self.dealer_hand)         
        mock_print.assert_called_with("\nDealer's hand: ")
       
if __name__ == '__main__':
    unittest.main()
