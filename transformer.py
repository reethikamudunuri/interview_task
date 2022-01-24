from feature_engineering_1 import FeatureEngineering



class Transformer(object):
    """
    Transformer class offers apply method that applies all the transformations
    for the dataframe
    """

    def __init__(self, df):
        self.df = df

    def apply(self):
        """
        Apply all transformations here.
        :return:
        """
        # applying is_date tranformation, storing the output in a new dataframe column
        self.df["is_date"] = self.df.Word_text.apply(FeatureEngineering().is_date).astype("int")

        # applying is_number tranformation, storing the output in a new dataframe column
        self.df["is_number"] = self.df.Word_text.apply(FeatureEngineering().is_number).astype("int")

        #applying is_percent transformation, storing the output in new dataframe
        #self.df["is_percent"] = self.df.Word_text.apply(FeatureEngineering().is_percent).astype("boolean")

        #applying is_number_with_percent transformation, storing the output in new dataframe
        self.df["is_number_with_percent"]= self.df.Word_text.apply(FeatureEngineering().is_number_with_percent).astype("boolean")

        #applying is_UN transformation, storing the output in new Dataframe
        self.df["is_UN"] = self.df.Word_text.apply(FeatureEngineering().is_UN).astype("boolean")
        self.df["is_a_unit"] = self.df.Word_text.apply(FeatureEngineering().is_a_unit).astype("boolean")

        self.df["unit_type"] = self.df.Word_text.apply(FeatureEngineering().unit_type).astype("int")


from file_loader import DataLoader
from transformer import Transformer

"""
if __name__ == '__main__':
    data_loader = DataLoader(glob_path="interview material V2/interview material/training_data_new/predictions_labels/template7_*.csv")
    # obtain the dataframe
    df = data_loader.load()

    # apply transformations on the dataframe
    transformer = Transformer(df=df)
    transformer.apply()


    print(df.head(50))
    #print(df["label"].unique())  #prints the unique labels of the dataframe

"""