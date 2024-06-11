import pandas as pd
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("E:/pandas_project/adult.data.csv")
    print(df)
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()
    race_count