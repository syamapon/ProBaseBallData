"""
チーム・ポジション別、身長比較
"""
import pandas as pd
import matplotlib.pyplot as plt

# 表示インデックス
indexes = ['投手', '捕手', '内野手', '外野手']

def printOrderByHeight(fileName, lblTitle):
    """
    ポジション別の身長グラフを表示します

    Parameters
    ----------
    fileName : CSVファイル名
    lblTitle : グラフのラベル
    """
    dfMember = pd.read_csv(fileName)
    grMember = dfMember.groupby(['ポジション'])['身長'].mean()
    grMember = grMember.reindex(indexes)
    plt.plot(grMember, label=lblTitle)

# ファイル読込・グラフ表示
printOrderByHeight('Data/選手一覧/読売選手_2021.csv',        'ジャイアンツ')
printOrderByHeight('Data/選手一覧/阪神選手_2021.csv',        '阪神')
printOrderByHeight('Data/選手一覧/中日選手_2021.csv',        '中日')
printOrderByHeight('Data/選手一覧/ソフトバンク選手_2021.csv', 'ソフトバンク')
printOrderByHeight('Data/選手一覧/ロッテ選手_2021.csv',      'ロッテ')
printOrderByHeight('Data/選手一覧/西武選手_2021.csv',        '西武')

# 凡例表示
plt.legend()
plt.show()




