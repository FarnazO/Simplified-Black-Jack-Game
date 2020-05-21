'''
This module contains the Game class
'''
class Game():
    '''
    This class contains the actions required for playing the game
    '''
    def __init__(self):
        '''
        This method initialises the game object
        '''
        self.player_bet = 0
        self.playing = True
    def take_bet(self, chip):
        '''
        This method asks the user how much the player wants to place a bet.
        Input : a chip object
        Output: the value of the bet taken 



        by the player
        '''
        available_chips = chip.total
        print(f"You have {available_chips} chips available for betting.")
        while True:
            try:
                self.player_bet = int(input("Place your bet in integer: "))
                if self.player_bet > available_chips:
                    raise Exception("Whoops! Not enuogh chips!")
            except ValueError as ve:
                print("Incorrect input! Try again!")
                continue
            except:
                print(f"Your bet is more than your available chips which is {available_chips}.")
                another_bet = input("Would you like to place another bet (type Y)? or end the game (type N)?")
                if another_bet.upper() == "Y":
                    continue
                elif another_bet.upper() == "N":
                    "Your game ended!"
                    break
                else:
                    raise Exception("Wrong input!")
            else:
                print(f"The bet you placed is {self.player_bet}!")
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
                break
            elif result.lower() == "s" or result.lower() == "stand":
                self.playing = False
                break
            else:
                print("Wrong choice!")
                continue 
    def show_some(self, player_hand, dealer_hand):
        '''
        This method shows all the players cards plus all the dealer's hand\
        apart from one of dealer's card.
        '''
        print("\nDealer's hand: ")
        for i in range(1, len(dealer_hand.cards)):
            print(f"{dealer_hand.cards[i].rank} of {dealer_hand.cards[i].suit}")
