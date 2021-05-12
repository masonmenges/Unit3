# Dependencies: pandas and random
import pandas as pd


class RandomDataFrame:
    def __init__(self, df, random_state):
        self.df = df
        self.random_state = random_state

    def randomize(df, random_state=None):
        if random_state:
            randomized = df.sample(len(df.index), random_state=random_state)
        else:
            randomized = df.sample(len(df.index))

        return randomized

    def null_count(df):
        sum = df.isnull().sum().sum()

        return sum


pd.read_csv()