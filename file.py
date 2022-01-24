import pandas as pd
import glob

def load_test_data(path):
    files = glob.glob(path +"template7_*.csv")
    li = []


    for filename in files[:]:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)
    df_test = pd.concat(li, axis=0, ignore_index=True)
    df_test.drop(df_test.columns[0], axis=1, inplace=True)
    return df_test
df_test = load_test_data("interview material V2/interview material/training_data_new/predictions_labels/")

print(df_test)