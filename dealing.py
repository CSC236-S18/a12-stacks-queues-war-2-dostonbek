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

import random 

class Deal:
    """
    Used to create piles of cards, shuffle them and 
    distribute them to players
    """

    def __init__(self, player, comp):

        """Assigning initial values of the class"""
        
        self.player = player            # player instance of Player class
        self.comp = comp                # computer instance of Player class
        self.deck = range(0, 10)        # creating a deck of cards with values from 0 to 9
        self.cards = self.deck * 5      # creating a pile of five decks of cards
        self.dealingPile = []           # dealing pile

    def shuffle(self):

        """shuffles the cards stored in self.cards list"""
        
        random.shuffle(self.cards)

    def add_to_deal_pile(self):
        
        """adds the shuffled cards to the dealing pile in the same order"""

        for i in self.cards:
            self.dealingPile.append(i)

    def distribute_to_players(self):

        """distributes the cards to players from top of the dealing pile in alternate turns"""

        x = len(self.dealingPile) - 1
        for i in range(25):
            self.player.PlayingPile.push(self.dealingPile[x])
            self.comp.PlayingPile.push(self.dealingPile[x-1])
            x -= 2
