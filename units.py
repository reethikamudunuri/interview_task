
class Units(object):

    def units_extend(self):

        self.units = ["m","mm","cm","µm"]
        self.units.extend(["l","ml","m3"])
        self.units.extend(["g","gr", "kg"])
        self.units

    def unit_to_category(self):

        self.unit_to_category = dict() #to check what units belongs to what category
                                  #0 would be none
        self.unit_to_category["m"] = 1 #1 would be length
        self.unit_to_category["mm"] = 1
        self.unit_to_category["cm"] = 1
        self.unit_to_category["µm"] = 1
        #inches
        self.unit_to_category["l"] = 2 #2 would be volume
        self.unit_to_category["ml"] = 2
        self.unit_to_category["m3"] = 2
        #gallons
        self.unit_to_category["g"] = 3 #3 would be weight
        self.unit_to_category["gr"] = 3
        self.unit_to_category["kg"] = 3

    def units_to_cat(self):
        self.unit_to_cat=dict()
        self.unit_to_cat["volume"] = 1
        self.unit_to_cat["mass"] = 2
        self.unit_to_cat["length"] = 3
