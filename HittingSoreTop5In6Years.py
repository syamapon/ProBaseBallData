"""
西武ライオンズの選手の打撃成績
"""

import pandas as pd
import matplotlib.pyplot as plt

dfMember2020 = pd.read_csv("Data/西武ライオンズ_打撃成績/2020年.csv", index_col='選手')
dfMember2019 = pd.read_csv("Data/西武ライオンズ_打撃成績/2019年.csv", index_col='選手')
dfMember2018 = pd.read_csv("Data/西武ライオンズ_打撃成績/2018年.csv", index_col='選手')
dfMember2017 = pd.read_csv("Data/西武ライオンズ_打撃成績/2017年.csv", index_col='選手')
dfMember2016 = pd.read_csv("Data/西武ライオンズ_打撃成績/2016年.csv", index_col='選手')
dfMember2015 = pd.read_csv("Data/西武ライオンズ_打撃成績/2015年.csv", index_col='選手')

dfMembers = pd.concat({'2020':dfMember2020
                       ,'2019':dfMember2019
                       ,'2018':dfMember2018
                       ,'2017':dfMember2017
                       ,'2016':dfMember2016
                       ,'2015':dfMember2015})
grp = dfMembers.groupby(level = '選手')

# 山川選手過去5年の成績
print(grp.sum().loc['山川　穂高'])

# ホームランTOP10
dfHomeran = grp.sum().sort_values('本塁打', ascending=False).loc[:, ['本塁打']]
dfHomeran['No'] = range(1,len(dfHomeran) + 1)
dfHomeran10 = dfHomeran[dfHomeran['No'] < 10]
print(dfHomeran10)

# 打率TOP10
dasu_anda =  grp.sum()[grp.sum()['打数'] > 100].loc[:, ['打数','安打']]
dfHitAtBat = pd.DataFrame({'Ave.': dasu_anda['安打'] / dasu_anda['打数']})
dfHitAtBat = dfHitAtBat.sort_values('Ave.', ascending=False)
dfHitAtBat['No'] = range(1,len(dfHitAtBat) + 1)
dfHitAverage10 = dfHitAtBat[dfHitAtBat['No'] < 10]
print(dfHitAverage10)


