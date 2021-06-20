"""
ポジション別の打撃成績を表します
"""
import pandas as pd
import matplotlib.pyplot as plt

dfHittingScoreLions2020 = pd.read_csv("Data/西武ライオンズ_打撃成績/2020年.csv", index_col='選手')
dfMemberLions2021 = pd.read_csv("Data/西武選手_2021.csv", index_col='名前')

dfMemHScoreLinons = pd.merge(dfHittingScoreLions2020, dfMemberLions2021, left_index=True, right_index=True)

dfHomerunPosition = dfMemHScoreLinons[['本塁打', 'ポジション']].groupby(dfMemHScoreLinons['ポジション'])

sumHomerun = dfHomerunPosition.sum()
sumHomerun = pd.DataFrame(sumHomerun, index=['投手', '捕手', '内野手', '外野手'])

plt.plot(sumHomerun)
plt.show()