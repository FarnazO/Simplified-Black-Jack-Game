'''
This module contains the unit tests for the Deck() class and its methods.
'''

import unittest
from mock import patch
from main_package import deck
from main_package.card import Card

class TestDeck(unittest.TestCase):

    '''
    This class contains the unit tests for the methods in the Deck() class
    '''
    def setUp(self):
        '''
        Sets up the common variables and objects used for all the unit tests
        '''
        self.suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        self.ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
        self.test_deck = deck.Deck()

    def test_given_suits_and_ranks_build_the_card_deck(self):
        '''
        Tests that when a deck object is created a deck of 52 cards has been generated
        '''
        expected_result = []
        for suit in self.suits:
            for rank in self.ranks:
                expected_result.append(Card(rank, suit))
        self.test_deck.__init__()
        self.assertEqual(expected_result[0].__str__(), \
                        self.test_deck.cards[0].__str__())

        self.assertEqual(expected_result[34].__str__(), \
                        self.test_deck.cards[34].__str__())

    def test_given_a_deck_print_the_cards_in_the_deck(self):
        '''
        This method tests the __str__ method for Deck class.
        For a given deck it should return all the cards in it.
        '''
        expected_result = []

        for deck_card in self.test_deck.cards:
            expected_result.append(deck_card.__str__())

        actual_result = self.test_deck.__str__()
        self.assertEqual(expected_result, actual_result)

    def test_given_a_deck_return_the_number_of_cards_existing_in_deck(self):
        '''
        This method tests the __len__ method in the Deck class
        '''
        expected_result = 48
        self.test_deck.deal()
        self.assertEqual(expected_result, len(self.test_deck))

    def test_when_shuffle_called_shuffle_the_deck_method2(self):
        '''
        This is the second way of testing the shuffle method of the deck object
        '''
        with patch.object(deck.random, 'shuffle') as random_mock:
            self.test_deck.shuffle()

        random_mock.assert_called_with(self.test_deck.cards)

    '''
    This way of testing seems to fail when working with relative imports
    '''
    # @patch('deck.random')
    # def test_when_shuffle_called_shuffle_the_deck(self, mock_random):
    #     '''
    #     This method tests the shuffle method of the deck object
    #     '''
    #     self.test_deck.shuffle()
    #     mock_random.shuffle.assert_called_with(self.test_deck.cards)

    def test_when_deal_is_called_two_cards_are_given_to_player_and_dealer(self):
        '''
        This unit tests check that four cards are dealth between the dealer \
        and player (two cards each)
        '''
        expected_result = (self.test_deck.cards[0:2], self.test_deck.cards[2:4])
        actual_result = self.test_deck.deal()
        for i in range(0, 2):
            self.assertEqual(expected_result[0][i].__str__(), actual_result[0][i].__str__())
            self.assertEqual(expected_result[1][i].__str__(), actual_result[1][i].__str__())

        self.assertEqual(self.test_deck.__len__(), 48)

    def test_get_next_card_return_the_next_card_in_the_deck(self):
        '''
        This method tests get_next_card and whether it returns the correct card.
        '''
        initial_deck_size = len(self.test_deck.cards)
        expected_result = self.test_deck.cards[0]
        actual_result = self.test_deck.get_next_card()
        self.assertEqual(expected_result.__str__(), actual_result.__str__())
        self.assertEqual(initial_deck_size - 1, len(self.test_deck.cards))

    def test_print_all_cards_method_given_two_cards(self):
        '''
        This method tests the print_all_cards method when given two cards to print
        '''
        player_cards, dealer_cards  = self.test_deck.deal()
        expected_print_arg = "|{:>2}     |  |{:>2}     |".format(player_cards[0].rank,\
                                                                 player_cards[1].rank)
        with patch.object(__builtins__, 'print') as mock_print:
            self.test_deck.print_all_cards(player_cards)
            mock_print.assert_called_with("└───────┘  └───────┘")

        actual_result = mock_print.call_args_list[1].args[0]
        self.assertEqual(expected_print_arg, actual_result)
        self.assertEqual(7, len(mock_print.call_args_list))


    def test_print_some_cards_method_given_two_cards(self):
        '''
        This method tests the print_some_cards method when given two cards to print
        '''
        player_cards, dealer_cards  = self.test_deck.deal()
        back_emoji = "\U0001F9A0"
        expected_print_arg = "|{0}{1}{2} |  | {3}     |".format(\
                                                        back_emoji,\
                                                        back_emoji,\
                                                        back_emoji,\
                                                        dealer_cards[1].rank)
        with patch.object(__builtins__, 'print') as mock_print:
            self.test_deck.print_some_cards(dealer_cards)
            mock_print.assert_called_with("└───────┘  └───────┘")
            
        actual_result = mock_print.call_args_list[1].args[0]
        self.assertEqual(expected_print_arg, actual_result)
        self.assertEqual(7, len(mock_print.call_args_list))

if __name__ == '__main__':
    unittest.main()
