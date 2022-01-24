import re
import numpy as np
from units import Units


class FeatureEngineering(object):
    """
    FeatureEngineering class offers various various utility methods that can be used
    to evaluate certain colummns
    """

    def is_date(self, string):
        """
        Return 1 if string matches date regex expression, or returns 0
        :param string:
        :return:
        """
        try:
            return 1 if re.match(r"\d{4}-\d{2}-\d{2}", string) is not None else 0
        except TypeError:
            print(string)

    def is_number(self, string):
        """
        Returns 1 if number, otherwise returns 0
        :param string:
        :return:
        """
        try:
            # try to convert to numpy float
            np.array(string, dtype="float")
            return 1
        except ValueError:
            return 0

    def is_percent(self,string):
        """
        Returns boolean if percentage
        :param string:
        :return:
        """
        return 1 if re.match(r"%", string) is not None else 0

    def is_number_with_percent(self,string):
        """
        Returns 1 if number with percentage is present
        :param string:
        :return:
        """
        return 1 if re.match(r"\d+%", string) is not None else 0

    def is_UN(self,string):
        """
        Returns 1 if UN value is present
        :param string:
        :return:
        """
        UN_REGEX = r"UN([a-zA-Z0-9.]+/)+[a-zA-Z0-9]+"
        return 1 if re.match(UN_REGEX, string.strip()) is not None else 0


    def is_a_unit(self,string):  # if unit type != 0 then it is already a unit
        # define own units because we can be sure they exists + we can define categories
        # Pre processing needed for the unit_type
        units = ["m", "mm", "cm", "µm"]
        units.extend(["l", "ml", "m3"])
        units.extend(["g", "gr", "kg"])
        units

        unit_to_category = dict()  # to check what units belongs to what category
        # 0 would be none
        unit_to_category["m"] = 1  # 1 would be length
        unit_to_category["mm"] = 1
        unit_to_category["cm"] = 1
        unit_to_category["µm"] = 1
        # inches
        unit_to_category["l"] = 2  # 2 would be volume
        unit_to_category["ml"] = 2
        unit_to_category["m3"] = 2
        # gallons
        unit_to_category["g"] = 3  # 3 would be weight
        unit_to_category["gr"] = 3
        unit_to_category["kg"] = 3


        unit_to_cat = dict()
        unit_to_cat["volume"] = 1
        unit_to_cat["mass"] = 2
        unit_to_cat["length"] = 3

        return 1 if string.lower() in Units.units_extend else 0


    def unit_type(string):
        # define own units because we can be sure they exists + we can define categories
        # Pre processing needed for the unit_type
        units = ["m", "mm", "cm", "µm"]
        units.extend(["l", "ml", "m3"])
        units.extend(["g", "gr", "kg"])
        units

        unit_to_category = dict()  # to check what units belongs to what category
        # 0 would be none
        unit_to_category["m"] = 1  # 1 would be length
        unit_to_category["mm"] = 1
        unit_to_category["cm"] = 1
        unit_to_category["µm"] = 1
        # inches
        unit_to_category["l"] = 2  # 2 would be volume
        unit_to_category["ml"] = 2
        unit_to_category["m3"] = 2
        # gallons
        unit_to_category["g"] = 3  # 3 would be weight
        unit_to_category["gr"] = 3
        unit_to_category["kg"] = 3

        import re
        unit_to_cat = dict()
        unit_to_cat["volume"] = 1
        unit_to_cat["mass"] = 2
        unit_to_cat["length"] = 3

        if string.lower() in Units.units_extend():
            return Units.unit_to_category[string.lower()]
        return 0





