import re  #Regex (regular expressions)
import numpy as np


class FeatureEngineering(object):
    """
    FeatureEngineering class offers various classes that implement the transformations
    """
    class DateTransformer(object):
        """
        DateTransformer
        """

        def __init__(self):
            pass

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

        def apply(self, df):
            """
            Applies the transformation and returns the dataframe
            :param df:
            :return:
            """
            df["is_date"] = df.Word_text.apply(self.is_date)
            return df

    class NumberTransformer(object):
        """
        NumberTransformer
        """

        def __init__(self):
            pass

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

        def apply(self, df):
            """
            Applies the transformation and returns the dataframe
            :param df:
            :return:
            """
            df["is_number"] = df.Word_text.apply(self.is_number)
            return df

    class Number_with_percentTransformer(object):
        """
        Number with percent Transformer
        """

        def __init__(self):
            pass

        def is_number_with_percent(self, string):
            """
            Returns 1 if number with percentage is present
            :param string:
            :return:
            """
            return 1 if re.match(r"\d+%", string) is not None else 0

        def apply(self, df):
            """
            Applies the transformation and returns the dataframe
            :param df:
            :return:
            """
            df["is_number_with_percent"] = df.Word_text.apply(self.is_number_with_percent).astype("boolean")
            return df

    class UN_Transformer(object):
        """
        UN_Transformer
        """

        def __init__(self):
            pass

        def is_UN(self, string):
            """
            Returns 1 if UN value is present
            :param string:
            :return:
            """
            UN_REGEX = r"UN([a-zA-Z0-9.]+/)+[a-zA-Z0-9]+"
            return 1 if re.match(UN_REGEX, string.strip()) is not None else 0

        def apply(self, df):
            """
            Applies the transformation and returns the dataframe
            :param df:
            :return:
            """

            df["is_UN"] = df.Word_text.apply(self.is_UN).astype("boolean")
            return df

    class UnitsTransformer(object):
        """
        UnitsTransformer
        """

        unit_to_category = {
            'm': 1,
            'mm': 1,
            'cm': 1,
            'µm': 1,
            'l':2,
            'ml':2,
            'm3':2,
            'g':3,
            'gr':3,
            'kg':3
        }

        def __init__(self):
            pass

        def get_unit_type(self, string):
            """
            returns the unit_type
            :param string:
            :return:
            """
            if string.lower() in FeatureEngineering.UnitsTransformer.unit_to_category.keys():
                return FeatureEngineering.UnitsTransformer.unit_to_category[string.lower()]
            return 0

        def is_unit(self, string):
            """
            returns if unit is present
            :param string:
            :return:
            """
            return string.lower() in FeatureEngineering.UnitsTransformer.unit_to_category.keys()

        def apply(self, df):
            """
            Applies the transformation and returns the dataframe
            :param df:
            :return:
            """
            df["is_unit"] = df.Word_text.apply(self.is_unit)
            df["unit_type"] = df.Word_text.apply(self.get_unit_type)
            return df

    class MeanTransformer(object):
        """
        MeanTransformer
        """

        def __init__(self):
            pass

        def y_mean(self, string):
            """
            Returns mean value
            :param string:
            :return:
            """

            pass

        def apply(self, df):
            """
            Applies the transformation and returns the dataframe
            :param df:
            :return:
            """
            df["y_mean"] = (df.top+df.bottom)/2
            return df

    class One_lTransformer(object):

        def __init__(self):
            pass

        def one_replace_l(string):
            pass

        def apply(self,df):
            for item in df["Word_text"]:
                if "1" in item:
                    if sum(c.isdigit() for c in item) == 1:
                        item = item.replace("1", "l")
            return df