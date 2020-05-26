'''
This module contains the Game class
'''
from main_package.deck import Deck

class Game():
    '''
    This class contains the actions required for playing the game
    '''
    def __init__(self):
        '''
        This method initialises the game object
        '''
        self.player_bet = 0
        self.h_or_s = "h"

    def take_bet(self, chip):
        '''
        This method asks the user how much the player wants to place a bet.
        Input : a chip object
        Output: the value of the bet taken by the player
        '''
        available_chips = chip.total
        
        if available_chips == 0:
            print("You have no more chips left for playing! \U0001F62D \U0001F631")
            return "ended"

        print(f"You have {available_chips} chips available for betting.\n")

        while True:
            try:
                self.player_bet = int(input("Place your bet in integer: "))
                print("="*40)
                print("="*40)
                if self.player_bet > available_chips:
                    raise Exception("Whoops! Not enuogh chips!")
            except ValueError:
                print("Incorrect input! Try again!")
                continue
            except:
                print(f"Your bet is more than your available chips which is {available_chips}.")
                another_bet = \
                input("Would you like to place another bet (type Y)? or end the game (type N)?")
                if another_bet.upper() == "Y":
                    continue
                elif another_bet.upper() == "N":
                    return "ended"
                else:
                    raise Exception("Wrong input!")
            else:
                # print(f"The bet you placed is {self.player_bet}!")
                return self.player_bet

    def hit(self, deck, hand):
        '''
        This method takes in a deck object and hand object\
         and adds a new card to the hand from the deck.
        Input: deck object and hand object
        '''
        new_card = deck.get_next_card()
        hand.add_card(new_card)

    def hit_or_stand(self, deck, hand):
        '''
        This method asks the user if they want to hit and get another card or stand.
        Input: a deck object and a hand object
        '''
        while True:
            result = input("hit or stand? h or s?")
            if result.lower() == "h" or result.lower() == "hit":
                self.hit(deck, hand)
                print("="*40)
                self.h_or_s = "h"
                break
            elif result.lower() == "s" or result.lower() == "stand":
                self.playing = False
                print("="*40)
                self.h_or_s = "s"
                break
            else:
                print("Wrong choice!")
                continue 
    
    def show_hands(self, player_hand, dealer_hand, all_or_some = "some"):
        '''
        This method shows all the players cards plus all the dealer's hand\
        apart from one of dealer's card.The all_or_some defines whether all the\
        cards are shown or one of dealer's card is hidden.
        Input: player's hand (hand object),\
               dealer's hand (hand object),\
               a string between "all" or "some"
        '''
        player_cards, player_total_score = player_hand.__str__()
        dealer_cards, dealer_total_score = dealer_hand.__str__()
        deck_of_cards = Deck()

        if all_or_some == "all":
            print(f"Dealer's hand with total score: {dealer_hand.value}")
            deck_of_cards.print_all_cards(dealer_hand.cards)
        else:
            print("Dealer's hand: ")
            deck_of_cards.print_some_cards(dealer_hand.cards)

        print(f"\nPlayer's hand with total score: {player_hand.value}")
        deck_of_cards.print_all_cards(player_hand.cards)
        print("="*40)
