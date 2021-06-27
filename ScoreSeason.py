import pandas as pd
import matplotlib.pyplot as plt

dfSeazon2020 = pd.read_csv('Data/シーズン勝敗_2020.csv')

def score(x, teamName):
    if x.ホーム == teamName:
        return x.ホーム得点
    elif x.ビジター == teamName:
        return x.ビジター得点
    else:
        return None

def scoreLoss(x, teamName):
    if x.ホーム == teamName:
        return x.ビジター得点
    elif x.ビジター == teamName:
        return x.ホーム得点
    else:
        return None

dfSeibuScore = pd.DataFrame({'日付':dfSeazon2020['月日'], 
                           '西武得点':dfSeazon2020.apply(lambda x:score(x, '西武'), axis=1),
                           '西武失点':dfSeazon2020.apply(lambda x:scoreLoss(x, '西武'), axis=1)})
dfSeibuScore = dfSeibuScore.loc[dfSeibuScore['西武得点'].notnull()]
dfSeibuScore = dfSeibuScore.set_index('日付')

