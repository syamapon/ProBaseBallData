import pandas as pd
import matplotlib.pyplot as plt

dfYomiuri = pd.read_csv('読売選手_2021.csv')
dfHanshin = pd.read_csv('阪神選手_2021.csv')
dfSoftbank = pd.read_csv('ソフトバンク選手_2021.csv')

# チーム別、ポジション別・身長平均比較
indexes = ['投手', '捕手', '内野手', '外野手']
grYomiuri = dfYomiuri.groupby(['ポジション'])['身長'].mean()
grYomiuri = grYomiuri.reindex(indexes)
grHanshin = dfHanshin.groupby(['ポジション'])['身長'].mean()
grHanshin = grHanshin.reindex(indexes)
grSoftbank = dfSoftbank.groupby(['ポジション'])['身長'].mean()
grSoftbank = grSoftbank.reindex(indexes)

plt.plot(grYomiuri, label="読売")
plt.plot(grHanshin, label="阪神")
plt.plot(grSoftbank, label="ソフトバンク")

plt.legend()
plt.show()


