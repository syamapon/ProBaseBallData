"""
ポジション別の打撃成績を表します
"""
import pandas as pd
import matplotlib.pyplot as plt

# ベースのデータ（2021年選手一覧・2020年打撃成績）読み込み
dfHittingScore = pd.read_csv("Data/西武ライオンズ_打撃成績/2020年.csv", index_col='選手')
dfMemberLions = pd.read_csv("Data/選手一覧/西武選手_2021.csv", index_col='名前')

# マージ処理（選手＝名前)
dfMemHScoreLinons = pd.merge(dfHittingScore, dfMemberLions, left_index=True, right_index=True)

# ポジション別にグループ化
grHomerunByPosition = dfMemHScoreLinons[['本塁打', 'ポジション']].groupby('ポジション')

# 合計
sumHomerun = grHomerunByPosition.sum()
sumHomerun = sumHomerun.reindex(['投手', '捕手', '内野手', '外野手'])

# プロット
plt.plot(sumHomerun)
plt.show()