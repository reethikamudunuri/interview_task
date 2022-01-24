import pandas as pd
import glob


class DataLoader(object):
    """
    DataLoader provides functionality to load many csv files using glob path expression
    and return the result as dataframe
    """

    def __init__(self, glob_path):
        self.path = glob_path

    def __cleanse(self, df):
        """
        Put all the cleanup logic here
        :param df:
        :return:
        """
        # removing first column, Unnamed: 0
        df.drop(df.columns[0], axis=1, inplace=True)
        return df

    def load(self):
        """
        loads multiple csv files and return the result as a pandas dataframe
        """
        files = glob.glob(self.path)
        li = []
        for filename in files:
            df = pd.read_csv(filename, index_col=None, header=0)
            li.append(df)

        # appends each dataframe under the previous one
        df_test = pd.concat(li, axis=0, ignore_index=True)

        # performs any cleansing operations on the data frame.
        df_test = self.__cleanse(df=df_test)
        return df_test
