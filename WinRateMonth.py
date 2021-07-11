import pandas as pd
import matplotlib.pyplot as plt

dfSeazon2020 = pd.read_csv('Data/シーズン勝敗_2020.csv')

def fncResult(x, teamName):
    if x['ホーム'] == teamName:
        if x['ホーム得点'] > x['ビジター得点']:
            return 'win'
        elif x['ホーム得点'] < x['ビジター得点']:
            return 'loss'
        else:
            return 'draw'
    elif x['ビジター'] == teamName:
        if x['ホーム得点'] > x['ビジター得点']:
            return 'loss'
        elif x['ホーム得点'] < x['ビジター得点']:
            return 'win'
        else:
            return 'draw'
    else:
        return None

def fncFirstResult(x, teamName):
    return max(x[teamName].fillna(''))


dfWinLoseDraw = pd.DataFrame({'月日':dfSeazon2020['月日'], 
                              '西武':dfSeazon2020.apply(lambda x:fncResult(x, '西武'), axis=1),                           
                              'ソフトバンク':dfSeazon2020.apply(lambda x:fncResult(x, 'ソフトバンク'), axis=1),
                              'オリックス':dfSeazon2020.apply(lambda x:fncResult(x, 'オリックス'), axis=1),
                              'ロッテ':dfSeazon2020.apply(lambda x:fncResult(x, 'ロッテ'), axis=1),
                              '日本ハム':dfSeazon2020.apply(lambda x:fncResult(x, '日本ハム'), axis=1),                 
                              '楽天':dfSeazon2020.apply(lambda x:fncResult(x, '楽天'), axis=1)})

dfTeams = pd.concat({'西武':dfWinLoseDraw.groupby('月日').apply(fncFirstResult, '西武'),
                       'ソフトバンク':dfWinLoseDraw.groupby('月日').apply(fncFirstResult, 'ソフトバンク'),
                       'オリックス':dfWinLoseDraw.groupby('月日').apply(fncFirstResult, 'オリックス'),
                       'ロッテ':dfWinLoseDraw.groupby('月日').apply(fncFirstResult, 'ロッテ'),
                       '日本ハム':dfWinLoseDraw.groupby('月日').apply(fncFirstResult, '日本ハム'),
                       '楽天':dfWinLoseDraw.groupby('月日').apply(fncFirstResult, '楽天')}, axis=1)

dfTeams['月日'] = dfTeams.index
dfTeams['月'] = dfTeams['月日'].str.split(pat='/', expand=True)[0]

def winCount(x, teamName):
    return len(x.loc[x[teamName] == 'win'].index)

def winRate(x, teamName):
    return len(x.loc[x[teamName] == 'win'].index) / (len(x.loc[x[teamName] == 'win'].index) + len(x.loc[x[teamName] == 'loss'].index))

dsSeibu = dfTeams.groupby('月').apply(winRate, '西武')
dsSoftbank = dfTeams.groupby('月').apply(winRate, 'ソフトバンク')

dsSeibu = dsSeibu.reindex(['6', '7', '8', '9', '10', '11'])
dsSoftbank = dsSoftbank.reindex(['6', '7', '8', '9', '10', '11'])

plt.plot(dsSeibu, label="西武")
plt.plot(dsSoftbank, label="ソフトバンク")

plt.legend()
plt.show()

dfWinNums = pd.concat({'西武':dsSeibu,
                       'ソフトバンク':dsSoftbank})







