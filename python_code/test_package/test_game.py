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
from main_package import game

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
        self.dealer_hand.add_card(Card("Ace", "Hearts"))
        self.dealer_hand.add_card(Card("Ace", "Spades"))
        self.player_hand.add_card(Card("2", "Hearts"))
        self.player_hand.add_card(Card("3", "Hearts"))
        self.player_chips = Chips()
        self.dealer_chips = Chips()

    def test_the_game_object_is_initiated_correctly(self):
        '''
        Test that the game object is initiated correctly
        '''
        self.game.__init__()
        self.assertEqual("h", self.game.h_or_s)

    def test_take_bet_method_when_the_users_bet_is_accepted(self):
        '''
        Test the take_bet method in the game class when the player successfully place their bet.
        '''
        placed_bet = 5
        with patch('builtins.input', return_value=placed_bet): \
        # Mocking the return of the built-in input method
            output_bet = self.game.take_bet(self.player_chips)
            self.assertEqual(placed_bet, output_bet)

    def test_take_bet_method_when_the_users_bet_is_over_their_available_chips(self):
        '''
        Test the take_bet method in the game class when the player place a bet higher than\
        their chips and then fix it.
        '''
        placed_bet = 6
        with patch('builtins.input', return_value=500): \
        # Mocking the return of the first built-in input method
            with patch('builtins.input', return_value="N"): \
            # Mocking the return of the second built-in input method
                with patch('builtins.input', return_value=placed_bet): \
                # Mocking the return of the last built-in input method
                    output_bet = self.game.take_bet(self.player_chips)
                    self.assertEqual(placed_bet, output_bet)

    def test_that_hit_method_adds_a_new_card_to_the_hand(self):
        '''
        Tests the hit method which adds a new card to the hand
        '''
        self.game.hit(self.card_deck, self.player_hand)
        self.assertEqual(3, self.player_hand.__len__())

    def test_when_user_chooses_to_hit_a_card_is_added(self):
        '''
        Test the hit_or_stand method when the player chooses hit.
        '''
        with patch('builtins.input', return_value="h"):
            with patch.object(self.game, 'hit') as hit_mock:
                self.game.hit_or_stand(self.card_deck, self.player_hand)
            hit_mock.assert_called_with(self.card_deck, self.player_hand)
        self.assertEqual("h", self.game.h_or_s)

    def test_when_user_chooses_to_stand(self):
        '''
        Test the hit_or_stand method when the player chooses hit.
        '''
        with patch('builtins.input', return_value="s"):
            self.game.hit_or_stand(self.card_deck, self.player_hand)
            self.assertEqual("s", self.game.h_or_s)

    def test_show_hands_method_when_some_cards_is_shown(self):
        '''
        Test the show_hands method when the option of "some" or none is chosen
        '''
        expected_number_of_print_calls = 10
        with patch.object(__builtins__, 'print') as mock_print:
            with patch.object(game.Deck, 'print_some_cards') as mock_print_cards:
                self.game.show_hands(self.player_hand, self.dealer_hand)

        mock_print_cards.assert_called_with(self.dealer_hand.cards)
        self.assertEqual(expected_number_of_print_calls,\
                        len(mock_print.call_args_list))
        self.assertEqual("Dealer's hand: ", 
                        mock_print.call_args_list[0].args[0])

    def test_show_hands_method_when_all_cards_are_shown(self):
        '''
        Test the show_hands method when the option of "all" is chosen
        '''
        expected_number_of_print_calls = 3
        with patch.object(__builtins__, 'print') as mock_print:
            with patch.object(game.Deck, 'print_all_cards') as mock_print_cards:
                self.game.show_hands(self.player_hand, self.dealer_hand, "all")

        mock_print_cards.assert_called_with(self.player_hand.cards)
        self.assertEqual(expected_number_of_print_calls,\
                        len(mock_print.call_args_list))

        self.assertEqual(f"Dealer's hand with total score: {self.dealer_hand.value}", 
                        mock_print.call_args_list[0].args[0])

    # def test_who_won_when_the_player_wins(self):
    #     '''
    #     Test the who_won method when the player wins the game
    #     '''
    #     player_hand = Hand()
    #     player_hand.add_card(Card("Ace", "Hearts"))
    #     player_hand.add_card(Card("Jack", "Diamonds"))
    #     dealer_hand = Hand()
    #     dealer_hand.add_card(Card("Seven", "Spades"))
    #     dealer_hand.add_card(Card("Ten", "Clubs"))
    #     self.game.player_bet = 10

    #     expected_number_of_player_chips = 110
    #     expected_number_of_dealer_chips = 90
    #     winner = self.game.who_won(\
    #         self.player_chips, self.dealer_chips, player_hand, dealer_hand\
    #         )
    #     self.assertEqual("Player", winner)
    #     self.assertEqual(expected_number_of_player_chips, self.player_chips.total)
    #     self.assertEqual(expected_number_of_dealer_chips, self.dealer_chips.total)

if __name__ == '__main__':
    unittest.main()
