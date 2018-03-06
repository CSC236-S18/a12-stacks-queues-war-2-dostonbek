###########################################################
# Author: Dostonbek Toirov
# Username: toirovd 
# 
# Purpose: Creating a card war game while building up knowledge
#           on queues and stacks
###########################################################
# Acknowledgement:
# 
###########################################################

from dealing import Deal 
from player import Player
import time


def start(input):

    """starts the game, if the input is equal to 'y'

    pre: uses an input from the user

    post: returns true if the user input is 'y'"""

    if input == 'y':
        return True
    else:
        return False


def loop_again(loot_pile, player, comp):

    '''uses almost the same game loop in the main funtion.
    Called when the war between players is started, and cards need 
    to be displayed

    pre: Takes loot_pile to store the cards displayed by players, and
    Uses player variable and comp (computer variable)

    post: removes and returns first item in the queue'''

    if player.PlayingPile == 0 and player.StoragePile == 0:         # if player's both piles are empty, then loses the game
        print("Too bad! You ran out of cards in your both storage pile and playing pile!")
        print("Looks like you are not a very good player! You LOST!")
    elif comp.PlayingPile == 0 and comp.PlayingPile == 0:           # if computer's both piles are empty, then loses the game
        print("Kudos to you, the Lord of Cards!")
        print("Computer ran out of cards in both storage pile and playing pile!")
        print("Which means you WON!")

    print()
    x = input("Press 'p' to open a card from your playing play: ")  # asks a player for an input
    print()
    if x == 'p':                                                    # if input is equal to 'p' then, start display card
        pl_card = player.remove_card()                              # a card is removed from a player's playing pile
        comp_card = comp.remove_card()                              # a card is removed from a computer's playing pile
        player.display_card(pl_card, "human")                       # player's card is displayed
        time.sleep(1)
        comp.display_card(comp_card, "comp")                        # a computer's card is displayed
        print()
        time.sleep(1)

        loot_pile.append(pl_card)                                   # player's card is added to the loot
        loot_pile.append(comp_card)                                 # computer's card is added to the loot

        if pl_card > comp_card:                                     # of player's card is greater than computer's
            print("Your card is greater than the computer's card. Nice!!! You will collect all the cards!")
            player.move_loot(loot_pile)                             # move the loot to player's storage pile  

        elif pl_card < comp_card:                                   # if player's card is less than computer's
            print("Oh, no! Computer's card is greater than yours! Computer will collect all the cards!")
            comp.move_loot(loot_pile)                               # move the loot to computer's storage pile
            
        elif pl_card == comp_card:
            print("No! Not again! You and computer have removed the same card again! This means WAR will continue!")
            print()
            time.sleep(1)
            print("Now you both need to add another card each to the loot pile without displaying the cards.")
            loot_pile.append(player.remove_card())                  # remove one more card from player's playing pile without displaying
            loot_pile.append(comp.remove_card())                    # remove one more card from computer's playing pile without displaying
            print()
            time.sleep(1)
            print("Now you both added a card each to the loot pile.")
            print("Now you both need to display another card from your playing pile.")
            print()
            loop_again(loot_pile, player, comp)                     # calls this function again (recursion)
    

def main():
    """
    main function where the main body of the game occurs
    """

    inp = input("Do you want to start the game [y/n]: ")            # ask the user if they want to start the game
    
    player = Player()               # make an instance of a Player class for a human player
    comp  = Player()                # make an instance of a Player class for a computer

    dealer = Deal(player, comp)     # make an instance of a Deal class for a dealer
    dealer.shuffle()                # call to a method shuffle of a dealer
    dealer.add_to_deal_pile()       # adding the shuffled cards to dealing pile
    dealer.distribute_to_players()  # distributing cards in the dealing pile to players
    

    while start(inp):               # main loop of the game

        loot_pile = []              # creating a list for a loot pile in the middle

        if player.PlayingPile == 0 and player.StoragePile == 0:             # if player's both piles are empty, then loses the game
            print("Too bad! You ran out of cards in your both storage pile and playing pile!")
            print("Looks like you are not a very good player! You LOST!")
            break

        elif comp.PlayingPile == 0 and comp.PlayingPile == 0:               # if computer's both piles are empty, then loses the game
            print("Kudos to you, the Lord of Cards!")
            time.sleep(1)
            print("Computer ran out of cards in both storage pile and playing pile!")
            time.sleep(1)
            print("Which means you WON!")
            break

        else:                                                               # if players' piles are not empty then continue the game
            print()
            x = input("Press 'p' to open a card from your playing pile: ")  # asks user to display a card from their playing piles
            print()
            if x == 'p':                                                    # if input is equal to 'p' then, start display card
                pl_card = player.remove_card()                              # a card is removed from a player's playing pile
                comp_card = comp.remove_card()                              # a card is removed from a computer's playing pile
                player.display_card(pl_card, "human")                       # player's card is displayed
                time.sleep(1)
                comp.display_card(comp_card, "comp")                        # a computer's card is displayed
                print()
                time.sleep(1)

                loot_pile.append(pl_card)                                   # player's card is added to the loot
                loot_pile.append(comp_card)                                 # computer's card is added to the loot

                if pl_card > comp_card:                                     # of player's card is greater than computer's
                    print("Your card is greater than the computer's card. Nice!!! You will collect all the cards!")
                    player.move_loot(loot_pile)                             # move the loot to player's storage pile  

                elif pl_card < comp_card:                                   # if player's card is less than computer's
                    print("Oh, no! Computer's card is greater than yours! Computer will collect all the cards!")
                    comp.move_loot(loot_pile)                               # move the loot to computer's storage pile
                    
                elif pl_card == comp_card:
                    print("Oh, no! You and computer have removed the same card! This means WAAAAAAAAR !")
                    print()
                    time.sleep(1)
                    print("Now you both need to add another card each to the loot pile without displaying the cards.")
                    loot_pile.append(player.remove_card())                  # remove one more card from player's playing pile without displaying
                    loot_pile.append(comp.remove_card())                    # remove one more card from computer's playing pile without displaying
                    print()
                    time.sleep(1)
                    print("Now you both added a card each to the loot pile.")
                    print("Now you both need to display another card from your playing pile.")
                    print()
                    loop_again(loot_pile, player, comp)                     # calls this function again (recursion)
            
                
if __name__ == '__main__':
    main()