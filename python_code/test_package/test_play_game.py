'''
This module contains the class testing the PlayGame class
'''
import unittest
from mock import patch
from main_package.play_game import PlayGame
from main_package import play_game
from main_package.game import Game
from main_package.chips import Chips
from main_package.deck import Deck
from main_package.hand import Hand
from main_package.card import Card


class TestPlayGame(unittest.TestCase):
    '''
    This class containst the unit tests for the methods in PlayGame class
    '''
    def setUp(self):
        '''
        This method sets up the common variables for all the \
        unit tests in this module
        '''
        self.play_game = PlayGame()

    def test_start_the_game_method_prints_the_correct_statements(self):
        '''
        This method test that the start_the_game method,\
        which should print the word "START" and welcomes the user to the game
        - 
        '''
        expected_number_of_print_calls = 13
        expected_print= "||  * * *   * * * *      *      * * *   * * * * ||"
        with patch.object(__builtins__, 'print') as mock_print:
            self.play_game.start_the_game()

        self.assertEqual(expected_number_of_print_calls,\
                        len(mock_print.call_args_list))
        self.assertEqual(expected_print, mock_print.call_args_list[2].args[0])

    def test_when_a_new_round_starts_correct_properties_are_set(self):
        '''
        This method tests the start_a_new_round method
        '''
        player_cards = [Card("2", "Hearts"), Card("5", "Hearts")]
        dealer_cards = [Card("Ace", "Hearts"), Card("5", "Spades")]
        self.play_game.start_a_new_round()
        with patch.object(play_game, 'Hand') as mock_hand:
            with patch.object(play_game, 'Deck') as mock_deck:
                self.play_game.start_a_new_round()

        mock_hand.assert_called_with()
        mock_deck.assert_called_with()
        self.assertEqual("started", self.play_game.game_status)
        self.assertEqual("h", self.play_game.game.h_or_s)
        
    def test_when_asking_player_for_a_bet_given_they_place_a_bet(self):
        '''
        This method tests the ask_player_for_bet method when the player\
        places a valid bet.
        '''
        with patch.object(self.play_game.game, 'take_bet', return_value=5) as mock_bet:
            self.play_game.ask_player_for_bet()
        mock_bet.assert_called_with(self.play_game.player_chips)
        self.assertEqual("started", self.play_game.game_status)
        
    def test_when_asking_player_for_a_bet_given_they_end_the_game(self):
        '''
        This method tests the ask_player_for_bet method when the player\
        chooses to end the game.
        '''
        with patch.object(self.play_game.game, 'take_bet', return_value="ended") as mock_bet:
            self.play_game.ask_player_for_bet()
        self.assertEqual("ended", self.play_game.game_status)
         
    def test_show_all_player_cards_and_some_dealer_cards_method(self):
        '''
        This method tests show_all_player_cards_and_some_dealer_cards method\
        in the PlayGame class.
        '''
        with patch.object(self.play_game.game, 'show_hands') as mock_show_hands:
            self.play_game.show_all_player_cards_and_some_dealer_cards()

        mock_show_hands.assert_called_with(self.play_game.player_hand, \
                                           self.play_game.dealer_hand,
                                           "some")

    def test_show_all_cards_method(self):
        '''
        This method tests show_all_cards method in the PlayGame class.
        '''
        with patch.object(self.play_game.game, 'show_hands') as mock_show_hands:
            self.play_game.show_all_cards()

        mock_show_hands.assert_called_with(self.play_game.player_hand, \
                                           self.play_game.dealer_hand,
                                           "all")

    def test_hit_or_stand_player_method(self):
        '''
        This method test the hit_or_stand_player method of the PlayGame class
        '''
        self.play_game.start_a_new_round()
        self.play_game.game.h_or_s = "h"
        with patch.object(self.play_game.game, 'hit_or_stand',create=True) as mock_hit_or_stand:
            with patch.object(self.play_game, 'show_all_player_cards_and_some_dealer_cards') as mock_print:
                    self.play_game.hit_or_stand_player()

        mock_hit_or_stand.assert_called_with(self.play_game.deck, self.play_game.player_hand)
        self.assertEqual("dealer's turn", self.play_game.game_status)


if __name__ == '__main__':
    unittest.main()