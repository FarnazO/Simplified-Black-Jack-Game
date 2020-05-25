'''
This module contains the PlayGame class which contains the steps of the game.
And when the file is run on the command line, you can play the black jack game.
'''
from game import Game
from chips import Chips
from deck import Deck
from hand import Hand
import emoji
from card import Card

class PlayGame():
    '''
    This class contains the 
    '''
    def __init__(self):
        self.game = Game()
        self.player_chips = Chips()
        self.dealer_chips = Chips()
    def start_the_game(self):
        print("Welcome to the simplified Black Jack game!")
        print("="*50)
        print("||  * * *   * * * *      *      * * *   * * * * ||")
        print("||  *          *        * *     *    *     *    ||")
        print("||  * * *      *       *   *    * * *      *    ||")
        print("||      *      *      * * * *   *    *     *    ||")
        print("||  * * *      *     *       *  *     *    *    ||")
        print("="*50)
        print("\U000026CF is Spades")
        print("\U0001F48E is Diamonds")
        print("\U0001F497 is Hearts")
        print("\U0001F46F is Clubs")
        print("="*50)
    def start_a_new_round(self):
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.game_status = "started"
        self.game.h_or_s = "h"
    def shuffle_deck_and_deal_cards(self):
        self.deck = Deck()
        self.deck.shuffle()
        player_cards, dealer_cards = self.deck.deal()
        self.__place_cards_in_hand__(self.player_hand, player_cards)
        self.__place_cards_in_hand__(self.dealer_hand, dealer_cards)
    def __place_cards_in_hand__(self, hand, cards):
        for card in cards:
            hand.add_card(card)
        return hand
    def ask_player_for_bet(self):
        bet_or_not = play.game.take_bet(self.player_chips)
        if bet_or_not == "ended":
            self.game_status = "ended"
    def show_all_player_cards_and_some_dealer_cards(self):
        self.game.show_hands(self.player_hand, self.dealer_hand, "some")
    def show_all_cards(self):
        self.game.show_hands(self.player_hand, self.dealer_hand, "all")
    def hit_or_stand_player(self):
        while self.game.h_or_s == "h":
            self.game.hit_or_stand(self.deck, self.player_hand)
            self.show_all_player_cards_and_some_dealer_cards()
            if self.player_hand.value == 21:
                self.show_all_cards()
                print(f"You won! \U0001f600 \U0001F38A")
                self.player_chips.win_bet(self.game.player_bet)
                self.dealer_chips.lose_bet(self.game.player_bet)
                self.game_status = "ended"
                break
            elif self.player_hand.value > 21:
                self.show_all_cards()
                print(f"You lost! \U0001F97A")
                self.player_chips.lose_bet(self.game.player_bet)
                self.dealer_chips.win_bet(self.game.player_bet)
                self.game_status = "ended"
                break
            else:
                self.game_status = "dealer's turn"
    def dealer_plays_hand(self):
        while self.game_status == "dealer's turn":
            if self.dealer_hand.value < 17:
                self.game.hit(self.deck, self.dealer_hand)
            elif self.dealer_hand.value > 21:
                self.show_all_cards()
                print(f"You won! \U0001f600 \U0001F38A")
                self.player_chips.win_bet(self.game.player_bet)
                self.dealer_chips.lose_bet(self.game.player_bet)
                self.game_status = "ended"
            else:
                self.game_status = "continue"
    def who_won(self):
        '''
        This method checks who has won the game and who wins or loses the chips.
        '''
        if self.player_hand.value <= self.dealer_hand.value:
            self.show_all_cards()
            print("You lose! \U0001F97A")
            self.player_chips.lose_bet(self.game.player_bet)
            self.dealer_chips.win_bet(self.game.player_bet)
            
        else:
            self.show_all_cards()
            print("You won! \U0001f600 \U0001F38A")
            self.player_chips.win_bet(self.game.player_bet)
            self.dealer_chips.lose_bet(self.game.player_bet)
    def end_the_game(self):
        print("="*44)
        print("||\U0001F44B    * * * *    *      *   * * *     \U0001F44B||")
        print("||\U0001F44B    *          * *    *   *    *    \U0001F44B||")
        print("||\U0001F44B    * * * *    *   *  *   *     *   \U0001F44B||")
        print("||\U0001F44B    *          *     **   *    *    \U0001F44B||")
        print("||\U0001F44B    * * * *    *      *   * * *     \U0001F44B||")
        print("="*44)
    def play_again(self):
        print("="*95)
        print("||    * * *  *          *      *     *            *       * * * *       *      *  *      *  ||")
        print("||    *    * *         * *      *   *            * *      *            * *     *  * *    *  ||")
        print("||    * * *  *        *   *       *             *   *     *   * *     *   *    *  *   *  *  ||")
        print("||    *      *       * * * *      *            * * * *    *     *    * * * *   *  *     **  ||")
        print("||    *      * * *  *       *     *           *       *   * * * *   *       *  *  *      *  ||")
        print("="*95)

if __name__ == '__main__':
    play = PlayGame()
    play.start_the_game()
    playing = True
    while playing:
        play.start_a_new_round()
        play.shuffle_deck_and_deal_cards()
        play.ask_player_for_bet()
        if play.game_status == "ended":
            break
        play.show_all_player_cards_and_some_dealer_cards()
        play.hit_or_stand_player()
        if play.game_status == "dealer's turn":
            play.dealer_plays_hand()
            if play.game_status == "continue":
                play.who_won()
        while True:
            play_again = input("Would you like to play again? y/n?")
            if play_again.lower() == "y" or play_again.lower() == "yes":
                print("="*40)
                playing = True
                play.game_status = "started"
                play.play_again()
                break
            elif play_again.lower() == "n" or play_again.lower() == "no":
                playing = False
                play.game_status = "ended"
                break
            else:
                print("Wrong choice!")
                continue
    play.end_the_game()