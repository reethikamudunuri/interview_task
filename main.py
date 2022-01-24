import pandas as pd


from file_loader import DataLoader
from sklearn.pipeline import Pipeline
from feature_engineering import FeatureEngineering


class DataframeFunctionTransformer(object):
    def __init__(self, func):
        self.func = func

    def transform(self, input_df, **transform_params):
        return self.func(input_df)

    def fit(self, X, y=None, **fit_params):
        return self


if __name__ == '__main__':
    data_loader = DataLoader(glob_path="interview material V2/interview material/training_data_new/predictions_labels/template7_*.csv")
    # obtain the dataframe
    df = data_loader.load()



    # apply various transformations on the dataframe
    pipeline = Pipeline(
        [
            ('is_date', DataframeFunctionTransformer(FeatureEngineering().DateTransformer().apply)),

            ('is_number', DataframeFunctionTransformer(FeatureEngineering().NumberTransformer().apply)),

            ('is_number_with_percent', DataframeFunctionTransformer(FeatureEngineering().Number_with_percentTransformer().apply)),

            ('is_UN',DataframeFunctionTransformer(FeatureEngineering().UN_Transformer().apply)),

            ('is_unit_is_unit_type', DataframeFunctionTransformer(FeatureEngineering().UnitsTransformer().apply)),

            ('y_mean', DataframeFunctionTransformer(FeatureEngineering().MeanTransformer().apply)),

            ('one_replace_l', DataframeFunctionTransformer(FeatureEngineering().One_lTransformer().apply)),
        ]
    )
    #updated_data object is created and the pipeline fit,transformations are performed
    updated_data = pipeline.fit_transform(df)

    #displays all the columns in dataframe
    pd.set_option('display.max_columns',None)

    #prints the first 50 rows in dataframe
    print(updated_data.head(50))
