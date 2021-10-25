"""
西武ライオンズの選手(2021年)を年齢別にグラフ表示します
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
from datetime import datetime

dfSeibu = pd.read_csv('Data/選手一覧/西武選手_2021.csv')
seYears = dfSeibu['生年月日'].str.split(pat='.', expand=True)[0]
seAges = datetime.now().year - seYears.astype(int)
dfYears = pd.DataFrame({'ages':seAges})

grYears = dfYears.groupby(by='ages')['ages'].count()

baseData = pd.DataFrame(np.zeros(60), index=range(10, 70))
agesData = pd.DataFrame(grYears)

dfHistgram = pd.merge(baseData, agesData, left_index=True, right_index=True, how='outer')
dfHistgram.plot.bar()
#fig = plot.figure()
#ax1 = fig.add_subplot(2, 2, 1)

#plot.bar(grYears)
#ax1.hist(grYears)
#grYears.plot.bar()
plot.show()