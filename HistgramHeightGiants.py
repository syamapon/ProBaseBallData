"""
読売選手のポジション別、身長分布
"""

import pandas as pd
import matplotlib.pyplot as plt
import math

'''
指定された行の身長を取得して、分類を返す
'''
def numByRange(index):
    height = dfYomiuri.loc[index]['身長']
    if math.isnan(height):
        return "不明"
    elif height < 160.0:
        return "160.0cm未満"
    elif height < 165.0:
        return "165.0cm未満"
    elif height < 170.0:
        return "170.0cm未満"
    elif height < 175.0:
        return "175.0cm未満"
    elif height < 180.0:
        return "180.0cm未満"
    elif height < 185.0:
        return "185.0cm未満"
    elif height < 190.0:
        return "190.0cm未満"
    elif height < 195.0:
        return "195.0cm未満"
    elif height < 200.0:
        return "200.0cm未満"
    else:
        return "200.0cm以上"

# ファイル読み込み
dfYomiuri = pd.read_csv('Data/選手一覧/読売選手_2021.csv')

# ポジション別の数を取得
pitcherNum = dfYomiuri[dfYomiuri['ポジション'] == '投手'].groupby(numByRange)['No.'].count()
catcherNum = dfYomiuri[dfYomiuri['ポジション'] == '捕手'].groupby(numByRange)['No.'].count()
infielderNum = dfYomiuri[dfYomiuri['ポジション'] == '内野手'].groupby(numByRange)['No.'].count()
outfielderNum = dfYomiuri[dfYomiuri['ポジション'] == '外野手'].groupby(numByRange)['No.'].count()

# 再インデックス
indexes = ["160.0cm未満", 
           "165.0cm未満", 
           "170.0cm未満", 
           "175.0cm未満", 
           "180.0cm未満", 
           "185.0cm未満", 
           "190.0cm未満", 
           "195.0cm未満", 
           "200.0cm未満", 
           "200.0cm以上"]
pitcherNum = pitcherNum.reindex(indexes).fillna(0)
catcherNum = catcherNum.reindex(indexes).fillna(0)
infielderNum = infielderNum.reindex(indexes).fillna(0)
outfielderNum = outfielderNum.reindex(indexes).fillna(0)

# プロット
fig = plt.figure()
axPitcher = fig.add_subplot(2, 2, 1)
axCatcher = fig.add_subplot(2, 2, 2)
axInfielder = fig.add_subplot(2, 2, 3)
axOutfielder = fig.add_subplot(2, 2, 4)

axPitcher.plot(pitcherNum, label="投手")
axCatcher.plot(catcherNum, label="捕手")
axInfielder.plot(infielderNum, label="内野手")
axOutfielder.plot(outfielderNum, label="外野手")

plt.legend()
plt.show()



