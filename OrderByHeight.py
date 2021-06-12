import pandas as pd
import matplotlib.pyplot as plt

# チーム・ポジション別、身長比較

indexes = ['投手', '捕手', '内野手', '外野手']

def printOrderByHeight(fileName, lblTitle):
    dfMember = pd.read_csv(fileName)
    grMember = dfMember.groupby(['ポジション'])['身長'].mean()
    grMember = grMember.reindex(indexes)
    plt.plot(grMember, label=lblTitle)

printOrderByHeight('Data/読売選手_2021.csv', 'ジャイアンツ')
printOrderByHeight('Data/阪神選手_2021.csv', '阪神')
printOrderByHeight('Data/中日選手_2021.csv', '中日')

printOrderByHeight('Data/ソフトバンク選手_2021.csv', 'ソフトバンク')
printOrderByHeight('Data/ロッテ選手_2021.csv', 'ロッテ')
printOrderByHeight('Data/西武選手_2021.csv', '西武')

plt.legend()
plt.show()




