import random 

class Deal:

    def __init__(self, player, comp):
        self.player = player    
        self.comp = comp
        self.deck = range(0, 10)
        self.cards = self.deck * 5
        self.dealingPile = []

    def shuffle(self):
        random.shuffle(self.cards)

    def add_to_deal_pile(self):
        for i in self.cards:
            self.dealingPile.append(i)

    def distribute_to_players(self):
        x = len(self.dealingPile) - 1
        for i in range(25):
            self.player.PlayingPile.append(self.dealingPile[x])
            self.comp.PlayingPile.append(self.dealingPile[x-1])
            x -= 2
