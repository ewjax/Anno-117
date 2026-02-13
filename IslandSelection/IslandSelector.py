from enum import IntFlag, auto


class LatiumFertility(IntFlag):
    """
    bitmapped enum for latium island fertilities
    """
    NONE = auto(0),
    MACKEREL = auto(),
    LAVENDAR = auto(),
    RESIN = auto(),
    OLIVE = auto(),
    GRAPES = auto(),
    FLAX = auto(),
    MUREX_SNAILS = auto(),
    SANDARAC = auto(),
    OYSTER = auto(),
    STURGEON = auto(),
    MARBLE = auto(),
    IRON = auto(),
    MINERAL = auto(),
    GOLD_ORE = auto()


class LatiumIsland:

    def __init__(self,
                 island_name: str,
                 fert_values: LatiumFertility = LatiumFertility.NONE,
                 river_slots: int = 0,
                 mountain_slots: int = 0):
        self.island_name = island_name,
        self.fertilities = fert_values
        self.river_slots = river_slots
        self.mountain_slots = mountain_slots
        # todo - add something for size

        # dictionary of fertility types and their weights
        self.fertility_weight = {}
        self.define_weights()


    def define_weights(self):
        """
        Weighting Scheme
        Tier2 - 5 points per production chain
        Tier3 - 3 points
        Tier4 - 1 point per production chain
        Construction material - use tier scores, but divide by 2
        River slots - 1 point per slot, multiplied by gold ore score?
        Mountain slots - 1 point per slot, multiplied by mineral score?
        """
        # tier2 chains - garum, soap
        self.fertility_weight[LatiumFertility.MACKEREL] = 5
        self.fertility_weight[LatiumFertility.LAVENDAR] = 5

        # tier3 chains - amphorae, olives
        self.fertility_weight[LatiumFertility.RESIN] = 3
        self.fertility_weight[LatiumFertility.OLIVE] = 3

        # tier4 chains - wine, togas, loungers, writing tablets, lyres, oysters w caviar, necklaces
        self.fertility_weight[LatiumFertility.GRAPES] = 1           # wine
        self.fertility_weight[LatiumFertility.FLAX] = 2             # togas, loungers
        self.fertility_weight[LatiumFertility.MUREX_SNAILS] = 2     # togas, loungers
        self.fertility_weight[LatiumFertility.SANDARAC] = 3         # writing tablets, loungers, lyres
        self.fertility_weight[LatiumFertility.OYSTER] = 1           # oysters with caviar
        self.fertility_weight[LatiumFertility.STURGEON] = 1         # oysters with caviar

        # construction material for tier3 and tier4 buildings
        # tier3 buildings - forum, baths
        # tier4 buildings - temple, libarary, amphitheatre
        # (3 + 3 + 1 + 1 + 1)/2
        self.fertility_weight[LatiumFertility.MARBLE] = 4.5

        # construction material for tier2 weapons and armor
        # (5 + 5)/2
        self.fertility_weight[LatiumFertility.IRON] = 5

        # tier4 production chains - fine glass, necklaces
        # tier4 mosaics used in buildings temple, library, amphitheatre
        # (1 + 1 + (1+1+1)/2)
        self.fertility_weight[LatiumFertility.MINERAL] = 3.5

        # tier4 - necklaces, lyres
        self.fertility_weight[LatiumFertility.GOLD_ORE] = 2

    def calculate_score(self) -> float:
        """
        determine score based purely on this island's fertilities
        and the associated weighting values for each fertility
        :return:
        score
        """
        rv = 0.0
        fert: LatiumFertility
        for fert in LatiumFertility:
            if self.has_fertility(fert.value):
                rv += self.fertility_weight[fert.value]

        # todo
        # do something cleverer with rivers and mountain slots
        rv += self.river_slots
        rv += self.mountain_slots

        # todo - need to differentiate if this fertility is already accounted for in the trial island set, i.e. don't double count
        # todo - need to provide a scoring weight depending on island order

        return rv

    def add_fertility(self, fert_value: LatiumFertility):
        """
        Add a fertility to this island
        :param fert_value:
        LatiumFertility value to be added
        :return:
        None
        """
        self.fertilities |= fert_value

    def has_fertility(self, fert_value: LatiumFertility) -> bool:
        """
        Does this island have this fertility?
        :param fert_value: LatiumFertility to be checked
        :return:
        True | False
        """
        return self.fertilities & fert_value == fert_value

    def set_river_slots(self, slots: int):
        self.river_slots = slots

    def set_mountain_slots(self, slots: int):
        self.mountain_slots = slots


    def dump(self):
        """
        utility function to dump all class data to stdout
        :return:
        """
        print(f"{vars(self)}")



def main():

    # print(LatiumFertility.NONE)
    # print(LatiumFertility)

    print(f"{LatiumFertility._member_names_}")
    print(f"{LatiumFertility._member_map_}")
    print(f"{LatiumFertility.__members__}")

    name = 'sample island'
    print(f"name = [{name}]")
    li2 = LatiumIsland(name);

    # todo - why did the name string get changed into an array of strings
    print(f"name = [{li2.island_name}]")
    print(f"name = [{li2.island_name[0]}]")

    li2.add_fertility(LatiumFertility.MACKEREL)
    li2.add_fertility(LatiumFertility.LAVENDAR | LatiumFertility.RESIN)
    print(f"Island has resin?   [{li2.has_fertility(LatiumFertility.RESIN)}]")
    print(f"Island has gold?    [{li2.has_fertility(LatiumFertility.GOLD_ORE)}]")
    print(f"Island score: [{li2.island_name[0]}], [{li2.calculate_score()}]")
    # li2.dump()

    li3 = LatiumIsland("island two", LatiumFertility.MACKEREL | LatiumFertility.OLIVE | LatiumFertility.MARBLE, 12, 8)
    print(f"Island score: [{li3.island_name}], [{li3.calculate_score()}]")
    # li3.dump()

    li_max = LatiumIsland('all fertilities')
    for fert in LatiumFertility:
        li_max.add_fertility(fert.value)
    li_max.set_river_slots(12)
    li_max.set_mountain_slots(8)
    li_max.dump()
    print(f"Island score: [{li_max.island_name}], [{li_max.calculate_score()}]")


if __name__ == '__main__':
    main()
