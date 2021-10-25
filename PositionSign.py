"""
西武選手のポジション別のサイン
"""

import pandas as pd

dfSeibu = pd.read_csv('Data/選手一覧/西武選手_2021.csv')
print(pd.get_dummies(dfSeibu['ポジション']))