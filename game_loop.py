from dealing import Deal 
from player import Player


def intro():
    pass

def start(input):
    if input == 'y':
        return True
    else:
        return False

def loop_again(loot_pile, player, comp):

    if player.PlayingPile == 0 and player.StoragePile == 0:
        print("Too bad! You ran out of cards in your both storage pile and playing pile!")
        print("Looks like you are not a very good player! You LOST!")
    elif comp.PlayingPile == 0 and comp.PlayingPile == 0:
        print("Kudos to you, the Lord of Cards!")
        print("Computer ran out of cards in both storage pile and playing pile!")
        print("Which means you WON!")

    x = input("Press 'p' to open a card from your playing play: ")
    if x == 'p':
        pl_card = player.remove_card()
        comp_card = comp.remove_card()
        player.display_card(pl_card, "human")
        comp.display_card(comp_card, "comp")

        loot_pile.append(pl_card)
        loot_pile.append(comp_card)

        if pl_card > comp_card:
            print("Your card is greater than the computer's card. Nice!!! You will collect all the cards!")
            player.move_loot(loot_pile)
            print(player.StoragePile)
        elif pl_card < comp_card:
            print("Oh, no! Computer's card is greater than yours! Computer will collect all the cards!")
            comp.move_loot(loot_pile)
            print(comp.StoragePile)
        elif pl_card == comp_card:
            print("No! Not again! You and computer have removed the same card again! This means WAR will continue!")
            print(loot_pile)
            print("Now you both need to add another card each to the loot pile without displaying the cards.")
            loot_pile.append(player.remove_card())
            loot_pile.append(comp.remove_card())
            print(loot_pile)
            print("Now you both added a card each to the loot pile.")
            print("Now you both need to display another card from your playing pile.")
            loop_again(loot_pile, player, comp)
    

def main():
    # Introduction
    intro()

    inp = input("Do you want to start the game [y/n]: ")
    
    player = Player()
    comp  = Player()

    dealer = Deal(player, comp)
    dealer.shuffle()
    dealer.add_to_deal_pile()
    dealer.distribute_to_players()
    
    

    while start(inp):
        loot_pile = []

        if player.PlayingPile == 0 and player.StoragePile == 0:
            print("Too bad! You ran out of cards in your both storage pile and playing pile!")
            print("Looks like you are not a very good player! You LOST!")
        elif comp.PlayingPile == 0 and comp.PlayingPile == 0:
            print("Kudos to you, the Lord of Cards!")
            print("Computer ran out of cards in both storage pile and playing pile!")
            print("Which means you WON!")
        else:
            x = input("Press 'p' to open a card from your playing pile: ")
            if x == 'p':
                pl_card = player.remove_card()
                comp_card = comp.remove_card()
                player.display_card(pl_card, "human")
                comp.display_card(comp_card, "comp")

                loot_pile.append(pl_card)
                loot_pile.append(comp_card)

                if pl_card > comp_card:
                    print("Your card is greater than the computer's card. Nice!!! You will collect all the cards!")
                    player.move_loot(loot_pile)
                    print(player.StoragePile)
                elif pl_card < comp_card:
                    print("Oh, no! Computer's card is greater than yours! Computer will collect all the cards!")
                    comp.move_loot(loot_pile)
                    print(comp.StoragePile)
                elif pl_card == comp_card:
                    print("Oh, no! You and computer have removed the same card! This means WAR!")
                    print(loot_pile)
                    print("Now you both need to add another card each to the loot pile without displaying the cards.")
                    loot_pile.append(player.remove_card())
                    loot_pile.append(comp.remove_card())
                    print(loot_pile)
                    print("Now you both added a card each to the loot pile.")
                    print("Now you both need to display another card from your playing pile.")
                    loop_again(loot_pile, player, comp)

                
                

if __name__ == '__main__':
    main()