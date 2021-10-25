"""
2020年シーズンの西武の勝率遷移
"""

import pandas as pd
import matplotlib.pyplot as plt

dfSeazon2020 = pd.read_csv('Data/シーズン勝敗_2020.csv')

dfSeibuData = pd.DataFrame({'日付':dfSeazon2020['月日'], 
                   'ホーム勝ち':dfSeazon2020['ホーム得点'] > dfSeazon2020['ビジター得点'],
                   '引分':dfSeazon2020['ホーム得点'] == dfSeazon2020['ビジター得点'],
                   'ホーム負け':dfSeazon2020['ホーム得点'] < dfSeazon2020['ビジター得点'],   
                   '西武ホームゲーム':dfSeazon2020['ホーム'] == '西武',
                   '西武ビジターゲーム':dfSeazon2020['ビジター'] == '西武'           
                   })

dfSeibu = dfSeibuData[dfSeibuData['西武ホームゲーム'] | dfSeibuData['西武ビジターゲーム']]

def fncWin(x, homeTeam, visitorTeam):
    if x.ホーム勝ち & x[homeTeam]:
        return 1
    elif x.ホーム負け & x[visitorTeam]:
        return 1
    else:
        return 0

def fncLose(x, homeTeam, visitorTeam):
    if x.ホーム負け & x[homeTeam]:
        return 1
    elif x.ホーム勝ち & x[visitorTeam]:
        return 1
    else:
        return 0

def fncDraw(x, homeTeam, visitorTeam):
    if x.引分 & x[homeTeam]:
        return 1
    elif x.引分 & x[visitorTeam]:
        return 1
    else:
        return 0


dfSeibuWin = pd.DataFrame({'日付':dfSeibu['日付'], 
                           '西武勝ち':dfSeibu.apply(lambda x:fncWin(x, '西武ホームゲーム', '西武ビジターゲーム'), axis=1),
                           '西武負け':dfSeibu.apply(lambda x:fncLose(x, '西武ホームゲーム', '西武ビジターゲーム'), axis=1),
                           '西武分け':dfSeibu.apply(lambda x:fncDraw(x, '西武ホームゲーム', '西武ビジターゲーム'), axis=1)})

dfSeibuWinSum = dfSeibuWin.expanding().sum()
dfSeibuWinRate = pd.DataFrame({'日付':dfSeibuWin['日付'],
                               '勝率':(dfSeibuWinSum['西武勝ち'] / (dfSeibuWinSum['西武負け'] + dfSeibuWinSum['西武勝ち']))})
dfSeibuWinRate = dfSeibuWinRate.set_index('日付')

plt.plot(dfSeibuWinRate)
plt.show()
