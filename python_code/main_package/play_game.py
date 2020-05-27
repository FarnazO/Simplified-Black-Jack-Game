'''
This module contains the PlayGame class which contains the steps of the game.
And when the file is run on the command line, you can play the black jack game.
'''
from main_package.game import Game
from main_package.chips import Chips
from main_package.deck import Deck
from main_package.hand import Hand

class PlayGame():
    '''
    This class contains all the steps required for running the game as methods.
    It contains the following properties:
        - an game object
        - player_chips which is a chips object
        - dealer_chips which is a chips object
        - player_hand and dealer_hand which at the start are empty but will be Hand objects
        - deck is empty at the inital step but then will be a Deck object
        - game_status which defines different statuses of the game and at start is "started"

    It contains the following methods:
        - "start_the_game" which prints the word "START" and welcomes the user to the game
        - "start_a_new_round" which resets the deck, hands and all the relevant properties for
            a new round of play for the same game.
        - "ask_player_for_bet" which asks the player for their bet and if they choose to end
           the game the game_status changes to "ended".
        - "show_all_player_cards_and_some_dealer_cards" which prints all the players cardss and
            some of the dealer's cards.
        - "show_all_cards" which prints all the cards for both the player and the dealer's hand.
        - "hit_or_stand_player" which asks the player if they want another card or they want to
            stand.
            It also checks if the player has reached 21 or above it.
        - "dealer_plays_hand" which adds cards to dealer's hand if their score is less than 17.
            It also checks if the dealers has exeeded 21.
        - "who_won" which checks who has won the game with a higher score and adjusts the chips
            based on who has won and lost the round.
        - "end_the_game" which prints the word "END" marking the end of the game.
        - "play_again" which prints the word "PLAY AGAIN" marking the start of a new round.
        - "__shuffle_deck_and_deal_cards__" which shuffles the deck and deals cards to both
            player and dealer's hands.
        - "__place_cards_in_hand__" which places the given cards in a hand object

    '''
    def __init__(self):
        '''
        This method initalises the properites needed for the object of this class
        '''
        self.game = Game()
        self.player_chips = Chips()
        self.dealer_chips = Chips()
        self.player_hand = ""
        self.dealer_hand = ""
        self.deck = ""
        self.game_status = "started"

    def start_the_game(self):
        '''
        This method prints the word "START" in *s to mark the start of the game.
        '''
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
        '''
        This method resets the hands, the deck, game.h_or_s and game_status for another round
        of the same game. Resetting the hands and deck includes shuffling the deck and dealing
        the cards to the players
        '''
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.deck = Deck()
        self.game_status = "started"
        self.game.h_or_s = "h"
        self.__shuffle_deck_and_deal_cards__()

    def ask_player_for_bet(self):
        '''
        This method uses the take_bet from the game object to ask the player
        for the bet they want to place and if they don't want to play anymore or don't have
        chips left, the game_status becomes ended.
        '''
        bet_or_not = self.game.take_bet(self.player_chips)
        if bet_or_not == "ended":
            self.game_status = "ended"

    def show_all_player_cards_and_some_dealer_cards(self):
        '''
        This method prints all the players cards and some
            of the dealer's cards (hides one of dealer's cards).
        '''
        self.game.show_hands(self.player_hand, self.dealer_hand, "some")

    def show_all_cards(self):
        '''
        This method prints all the cards for both the player and the dealer's hand.
        '''
        self.game.show_hands(self.player_hand, self.dealer_hand, "all")

    def hit_or_stand_player(self):
        '''
        This method asks the player if they want another card (hit) or they don't want any
        more cards (Stand). While the player asks for a hit, if they score becomes 21, they
        have won the round and game_status becomes "ended". If their score goes above 21 they
        lose the round and game_status becomes "ended".
        '''
        while self.game.h_or_s == "h":
            self.game.h_or_s = self.game.hit_or_stand(self.deck, self.player_hand)
            self.show_all_player_cards_and_some_dealer_cards()
            if self.player_hand.value == 21:
                self.show_all_cards()
                print(f"You won! \U0001f600 \U0001F38A")
                self.player_chips.win_bet(self.game.player_bet)
                self.dealer_chips.lose_bet(self.game.player_bet)
                self.game_status = "ended"
                break

            if self.player_hand.value > 21:
                self.show_all_cards()
                print(f"You lost! \U0001F97A")
                self.player_chips.lose_bet(self.game.player_bet)
                self.dealer_chips.win_bet(self.game.player_bet)
                self.game_status = "ended"
                break
                
            self.game_status = "dealer's turn"

    def dealer_plays_hand(self):
        '''
        This method is called once the player has chosen to stand. In this case, as long as
        dealer's score is less than 17, a card is added to their hand. As they add a card if they
        go above 17 and below 21 the dealer stops drawing a card and if their score goes above 21
        they lose the round and the game_status changes to "ended"
        '''
        hand_value = self.dealer_hand.value
        while self.game_status == "dealer's turn":
            if hand_value < 17:
                hand_value = self.game.hit(self.deck, self.dealer_hand)
            elif hand_value > 21:
                self.show_all_cards()
                print(f"You won! \U0001f600 \U0001F38A")
                self.player_chips.win_bet(self.game.player_bet)
                self.dealer_chips.lose_bet(self.game.player_bet)
                self.game_status = "ended"
            else:
                self.game_status = "continue"

    def who_won(self):
        '''
        This method checks who has the higher score which wins the round and it
        adjusts the chips based on who won and lost the game. Winner gets the chips
        that were beted and losers looses the same amount.
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
        '''
        This method prints the word "END" in *s to mark the end of the game.
        '''
        print("="*44)
        print("||\U0001F44B    * * * *    *      *   * * *     \U0001F44B||")
        print("||\U0001F44B    *          * *    *   *    *    \U0001F44B||")
        print("||\U0001F44B    * * * *    *   *  *   *     *   \U0001F44B||")
        print("||\U0001F44B    *          *     **   *    *    \U0001F44B||")
        print("||\U0001F44B    * * * *    *      *   * * *     \U0001F44B||")
        print("="*44)

    def play_again(self):
        '''
        This method prints the word "PLAY AGAIN" in *s to mark the start of a new round.
        '''
        print("="*95)
        print("||    * * *  *          *      *     *            *       * * * *       *      *  *      *  ||")
        print("||    *    * *         * *      *   *            * *      *            * *     *  * *    *  ||")
        print("||    * * *  *        *   *       *             *   *     *   * *     *   *    *  *   *  *  ||")
        print("||    *      *       * * * *      *            * * * *    *     *    * * * *   *  *     **  ||")
        print("||    *      * * *  *       *     *           *       *   * * * *   *       *  *  *      *  ||")
        print("="*95)

    def __shuffle_deck_and_deal_cards__(self):
        '''
        This is a private method which shuffles the deck, deals the cards and places them
        in the player and dealer's hands.
        '''
        self.deck.shuffle()
        dealth_cards = self.deck.deal()
        self.__place_cards_in_hand__(self.player_hand, dealth_cards[0])
        self.__place_cards_in_hand__(self.dealer_hand, dealth_cards[1])

    def __place_cards_in_hand__(self, hand, cards):
        '''
        This method places the given cards in the given hand.
        '''
        for card in cards:
            hand.add_card(card)
        return hand

if __name__ == '__main__':
    PLAY = PlayGame()
    PLAY.start_the_game()
    PLAYING = True
    while PLAYING:
        PLAY.start_a_new_round()
        PLAY.ask_player_for_bet()
        if PLAY.game_status == "ended":
            break
        PLAY.show_all_player_cards_and_some_dealer_cards()
        PLAY.hit_or_stand_player()
        if PLAY.game_status == "dealer's turn":
            PLAY.dealer_plays_hand()
            if PLAY.game_status == "continue":
                PLAY.who_won()
        while True:
            PLAY_AGAIN = input("Would you like to play again? y/n?")
            if PLAY_AGAIN.lower() == "y" or PLAY_AGAIN.lower() == "yes":
                print("="*40)
                PLAYING = True
                PLAY.game_status = "started"
                PLAY.play_again()
                break
            if PLAY_AGAIN.lower() == "n" or PLAY_AGAIN.lower() == "no":
                PLAYING = False
                PLAY.game_status = "ended"
                break
            print("Wrong choice!")

    PLAY.end_the_game()
