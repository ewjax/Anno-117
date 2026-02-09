


class LatiumIslandWeights:
    """
    Weighting Scheme
    Tier2 - 5 points per production chain
    Tier3 - 3 points
    Tier4 - 1 point per production chain
    Construction material - use tier scores, but divide by 2
    River slots - 1 point per slot, multiplied by gold ore score?
    Mountain slots - 1 point per slot, multiplied by mineral score?

    """

    def __init__(self):
        self.mackerel = 5           # garum (tier2)
        self.lavender = 5           # soap (tier2)
        self.resin = 3              # amphorae (tier3)
        self.olive = 3              # olives (tier3)
        self.grapes = 1             # wine (tier4)
        self.flax = 2               # togas (tier4), loungers (tier4)
        self.murex_snails = 2       # togas (tier4), loungers (tier4)
        self.sandarac = 3           # writing tablets (tier4), loungers (tier4), lyres (tier4)
        self.oyster = 1             # oysters w caviar (tier4)
        self.sturgeon = 1           # oysters w caviar (tier4)
        self.marble = 4.5           # forum, baths, temple, library, amphitheatre (divide
        self.iron = 5               # weapons (tier2), armor (tier2), divided by 2
        self.mineral = 3.5          # fine glass (tier4), necklaces (tier4), mosaics for tier4 buildings (temple, library, amphitheatre)
                                    # so, 1 + 1 + (1+1+1)/2
        self.gold_ore = 2           # necklaces (tier4), lyres (tier4)



class LatiumIsland:

    def __init__(self, weights: LatiumIslandWeights):
        self.name = 'Not Set'

        self.mackerel = False
        self.lavender = False
        self.resin = False
        self.olive = False
        self.grapes = False
        self.flax = False
        self.murex_snails = False
        self.sandarac = False
        self.oyster = False
        self.sturgeon = False
        self.marble = False
        self.iron = False
        self.mineral = False
        self.gold_ore = False

        self.river_slots = 0
        self.mountain_slots = 0

        self.weights = weights

        # raw score from fertilities
        self.raw_score




def main():
    pass


if __name__ == '__main__':
    main()
