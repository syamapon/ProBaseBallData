"""
西武ライオンズの選手(2021年)を年齢別にグラフ表示します
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# CSVファイル読み込み
dfSeibu = pd.read_csv('Data/選手一覧/西武選手_2021.csv')

# 年齢一覧の取得
seYears = dfSeibu['生年月日'].str.split(pat='.', expand=True)[0]
seAges = datetime.now().year - seYears.astype(int)

# 離散化・ビニング
bins = [10, 20, 30, 40, 50, 60, 70]
binTtls = ['10代', '20代', '30代', '40代', '50代', '60代']
cuts = pd.cut(seAges, bins, labels=binTtls)

# 頻度計算
histGra = pd.value_counts(cuts)

# 再インデックス
histGra = histGra.reindex(binTtls)

# グラフ表示
print(histGra)
plt.plot(histGra)
plt.show()


