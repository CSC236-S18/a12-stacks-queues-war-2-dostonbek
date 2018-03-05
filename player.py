##########################################################################
# Author: Dostonbek Toirov
# Username: toirovd 
# 
##########################################################################
# Acknowledgement: 
#
#
##########################################################################



class Player:

    def __init__(self):
        # possibly useful instance variables
        self.Current = None             # my currently displayed card
        self.currentState = None        # keeps track of the state of play
        self.PlayingPile = []            # stack 
        self.StoragePile = []           # queue 

    def make_move():
        # initiates a round of play and communicates play-by-play during the round
        # returns true when the game is still in play
        # returns false when the game is over
        # Communicates an appropriate message about whether the user beat the computer
        pass

    def remove_card(self):
        # Precondition: myPlayingPile is not empty 
        # If it is not empty, the function removes a card from myPlayingPile, 
        # returning the stored value
        if len(self.PlayingPile) > 0:
            pop_card = self.PlayingPile.pop(-1)
            return pop_card
        else:
            self.move_storage()
            pop_card = self.remove_card()
            return pop_card

    def display_card(self, card, player):
        # displays a card on the screen and returns the value
        if player == "human":
            print("Your have displayed a card " + str(card))
        elif player == "comp":
            print("Computer has displayed a card " + str(card))

    def move_loot(self, loot_pile):
        # moves everything from lootPile to myStoragePile    
        for i in loot_pile:
            self.StoragePile.append(i)

    def move_storage(self):
        # moves everything from myStoragePile to myPlayingPile
        print("Your playing pile became empty. Now refilling it with cards from your storage pile.")
        for i in self.StoragePile:
            self.PlayingPile.append(i)
        print("moved the storage to playing")
        self.StoragePile = []


        