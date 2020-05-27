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
        with patch.object(self.play_game.game, 'hit_or_stand', return_value="s") as mock_hit_or_stand:
            with patch.object(self.play_game, 'show_all_player_cards_and_some_dealer_cards') as mock_print:
                    self.play_game.hit_or_stand_player()

        mock_hit_or_stand.assert_called_with(self.play_game.deck, self.play_game.player_hand)
        self.assertEqual("dealer's turn", self.play_game.game_status)

    def test_hit_or_stand_player_method_when_player_score_is_21(self):
        '''
        This method test the hit_or_stand_player method of the PlayGame class when
        the player's score is 21.
        '''
        self.play_game.start_a_new_round()
        self.play_game.player_hand.value = 21
        with patch.object(self.play_game.game, 'hit_or_stand') as mock_hit_or_stand:
            with patch.object(self.play_game, 'show_all_player_cards_and_some_dealer_cards') as mock_print:
                with patch.object(self.play_game, 'show_all_cards') as mock_show_cards:
                    with patch.object(self.play_game.player_chips, 'win_bet') as mock_win_bet:
                        with patch.object(self.play_game.dealer_chips, 'lose_bet') as mock_lose_bet:
                            self.play_game.hit_or_stand_player()

        mock_hit_or_stand.assert_called_with(self.play_game.deck, self.play_game.player_hand)
        mock_show_cards.assert_called_with()
        self.assertEqual("ended", self.play_game.game_status)
        mock_win_bet.assert_called_with(self.play_game.game.player_bet)
        mock_lose_bet.assert_called_with(self.play_game.game.player_bet)

    def test_hit_or_stand_player_method_when_player_score_is_more_than_21(self):
        '''
        This method test the hit_or_stand_player method of the PlayGame class when
        the player's score is more than 21.
        '''
        self.play_game.start_a_new_round()
        self.play_game.player_hand.value = 25
        with patch.object(self.play_game.game, 'hit_or_stand') as mock_hit_or_stand:
            with patch.object(self.play_game, 'show_all_player_cards_and_some_dealer_cards') as mock_print:
                with patch.object(self.play_game, 'show_all_cards') as mock_show_cards:
                    with patch.object(self.play_game.dealer_chips, 'win_bet') as mock_win_bet:
                        with patch.object(self.play_game.player_chips, 'lose_bet') as mock_lose_bet:
                            self.play_game.hit_or_stand_player()

        mock_hit_or_stand.assert_called_with(self.play_game.deck, self.play_game.player_hand)
        mock_show_cards.assert_called_with()
        self.assertEqual("ended", self.play_game.game_status)
        mock_win_bet.assert_called_with(self.play_game.game.player_bet)
        mock_lose_bet.assert_called_with(self.play_game.game.player_bet)

    def test_dealer_plays_their_hand(self):
        '''
        This method tests the dealer_plays_hand method of PlayGame class
        '''
        self.play_game.start_a_new_round()
        self.play_game.game_status = "dealer's turn"
        self.play_game.dealer_hand.value = 10
        with patch.object(self.play_game.game, 'hit', return_value=18) as mock_hit:
                
             self.play_game.dealer_plays_hand()

        mock_hit.assert_called_with(self.play_game.deck, self.play_game.dealer_hand)

    def test_dealer_plays_their_hand_when_dealer_hand_is_more_than_17_less_than_21(self):
        '''
        This method tests the dealer_plays_hand method of PlayGame class when dealer's
        hand is more than 17 and less than 21.
        '''
        self.play_game.start_a_new_round()
        self.play_game.game_status = "dealer's turn"
        self.play_game.dealer_hand.value = 18
        self.play_game.dealer_plays_hand()
        self.assertEqual("continue", self.play_game.game_status)

    def test_dealer_plays_their_hand_when_dealer_hand_is_more_than_21(self):
        '''
        This method tests the dealer_plays_hand method of PlayGame class when dealer's
        hand is more than 21.
        '''
        self.play_game.start_a_new_round()
        self.play_game.game_status = "dealer's turn"
        self.play_game.dealer_hand.value = 23
        with patch.object(self.play_game, 'show_all_cards') as mock_show_cards:
            with patch.object(self.play_game.player_chips, 'win_bet') as mock_win_bet:
                with patch.object(self.play_game.dealer_chips, 'lose_bet') as mock_lose_bet:              
                    self.play_game.dealer_plays_hand()

        mock_show_cards.assert_called_with()
        self.assertEqual("ended", self.play_game.game_status)
        mock_win_bet.assert_called_with(self.play_game.game.player_bet)
        mock_lose_bet.assert_called_with(self.play_game.game.player_bet)

    def test_who_won_method_when_player_wins(self):
        '''
        This method test the who_won method when the player has higher score than dealer
        '''
        expected_print = "You won! \U0001f600 \U0001F38A"
        self.play_game.start_a_new_round()
        self.play_game.player_hand.value = 20
        self.play_game.dealer_hand.value = 17
        with patch.object(self.play_game, 'show_all_cards') as mock_show_cards:
            with patch.object(self.play_game.player_chips, 'win_bet') as mock_win_bet:
                with patch.object(self.play_game.dealer_chips, 'lose_bet') as mock_lose_bet: 
                    with patch.object(__builtins__, 'print') as mock_print:
                        self.play_game.who_won()

        mock_show_cards.assert_called_with()
        mock_print.assert_called_with(expected_print)
        mock_win_bet.assert_called_with(self.play_game.game.player_bet)
        mock_lose_bet.assert_called_with(self.play_game.game.player_bet)

    def test_who_won_method_when_dealer_wins(self):
        '''
        This method test the who_won method when the dealer has higher score than player
        '''
        expected_print = "You lose! \U0001F97A"
        self.play_game.start_a_new_round()
        self.play_game.player_hand.value = 15
        self.play_game.dealer_hand.value = 17
        with patch.object(self.play_game, 'show_all_cards') as mock_show_cards:
            with patch.object(self.play_game.dealer_chips, 'win_bet') as mock_win_bet:
                with patch.object(self.play_game.player_chips, 'lose_bet') as mock_lose_bet: 
                    with patch.object(__builtins__, 'print') as mock_print:
                        self.play_game.who_won()

        mock_show_cards.assert_called_with()
        mock_print.assert_called_with(expected_print)
        mock_win_bet.assert_called_with(self.play_game.game.player_bet)
        mock_lose_bet.assert_called_with(self.play_game.game.player_bet)

    def test_end_the_game_method_prints_the_correct_statements(self):
        '''
        This method test that the end_the_game method,\
        which should print the word "END".
        - 
        '''
        expected_number_of_print_calls = 7
        expected_print= "||\U0001F44B    *          * *    *   *    *    \U0001F44B||"
        with patch.object(__builtins__, 'print') as mock_print:
            self.play_game.end_the_game()

        self.assertEqual(expected_number_of_print_calls,\
                        len(mock_print.call_args_list))
        self.assertEqual(expected_print, mock_print.call_args_list[2].args[0])

    def test_play_again_method_prints_the_correct_statements(self):
        '''
        This method test that the play_again method,\
        which should print the word "PLAY AGAIN".
        - 
        '''
        expected_number_of_print_calls = 7
        expected_print= "||    *    * *         * *      *   *            * *      *            * *     *  * *    *  ||"
        with patch.object(__builtins__, 'print') as mock_print:
            self.play_game.play_again()

        self.assertEqual(expected_number_of_print_calls,\
                        len(mock_print.call_args_list))
        self.assertEqual(expected_print, mock_print.call_args_list[2].args[0])

if __name__ == '__main__':
    unittest.main()