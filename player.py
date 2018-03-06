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

from Stack import Stack
from MyQueue import Queue

class Player:

    """Used to make instances of players"""

    def __init__(self):
        
        """assigning initial values of players"""

        self.PlayingPile = Stack()          # stack 
        self.StoragePile = Queue()           # queue 

    def remove_card(self):

        """Removes card from the playing piles of players"""

        if self.PlayingPile.size() > 0:           # if not empty, return the card on top     
            pop_card = self.PlayingPile.pop()
            return pop_card
        else:   
            self.move_storage()                 # if empty, refill it with cards from the storage pile
            pop_card = self.remove_card()       # then call the remove function again
            return pop_card                     # and return the card on top

    def display_card(self, card, player):

        """displays the player's removed card"""

        if player == "human":                   # if a human player, display his/her removed card
            print("Your have displayed a card " + str(card))
        elif player == "comp":                  # if a computer player, display its removed card
            print("Computer has displayed a card " + str(card))

    def move_loot(self, loot_pile):

        """moves the cards in the loot pile to the storage pile of
        the player, if the player wins"""
        
        for i in loot_pile:
            self.StoragePile.enqueue(i)

    def move_storage(self):

        """moves everything from storage pile to a playing pile"""
        
        print("Playing pile became empty. Now refilling it with cards from storage pile.")
        print()
        for i in self.StoragePile.q:
            self.PlayingPile.push(i)

        self.StoragePile = Queue()                   # after finishing the move, empty the storage pile


        