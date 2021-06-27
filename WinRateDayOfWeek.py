"""
ホーム、ビジター別の勝ち負け数
"""

import pandas as pd
import matplotlib.pyplot as plt

dfSeazon2020 = pd.read_csv('Data/シーズン勝敗_2020.csv')


#pd.concat([dfSeazon2020[dfSeazon2020['ホーム'] == '西武'], dfSeazon2020[dfSeazon2020['ビジター'] == '西武']])[['ホーム', 'ビジター']]

# 西武のホームゲーム
isHomeSeibu = dfSeazon2020['ホーム'] == '西武'
# 西武のビジターゲーム
isVisitorSeibu = dfSeazon2020['ビジター'] == '西武'

dfHomeSeibu = dfSeazon2020[isHomeSeibu]
dfVisitorSeibu = dfSeazon2020[isVisitorSeibu]

# ホーム勝ち負け
dfHomeSeibuWin = dfHomeSeibu[dfHomeSeibu['ホーム得点'] > dfHomeSeibu['ビジター得点']]
homeWinNum = len(dfHomeSeibuWin)
dfHomeSeibuLost = dfHomeSeibu[dfHomeSeibu['ホーム得点'] < dfHomeSeibu['ビジター得点']]
homeLostNum = len(dfHomeSeibuLost)
dfHomeSeibuDraw = dfHomeSeibu[dfHomeSeibu['ホーム得点'] == dfHomeSeibu['ビジター得点']]
homeDrawNum = len(dfHomeSeibuDraw)

# ビジター勝ち負け
dfVisitorSeibuWin = dfVisitorSeibu[dfVisitorSeibu['ホーム得点'] < dfVisitorSeibu['ビジター得点']]
visitorWinNum = len(dfVisitorSeibuWin)
dfVisitorSeibuLost = dfVisitorSeibu[dfVisitorSeibu['ホーム得点'] > dfVisitorSeibu['ビジター得点']]
visitorLostNum = len(dfVisitorSeibuLost)
dfVisitorSeibuDraw = dfVisitorSeibu[dfVisitorSeibu['ホーム得点'] == dfVisitorSeibu['ビジター得点']]
visitorDrawNum = len(dfVisitorSeibuDraw)

print("ホーム勝ち：{0}、ホーム負け：{1}、ホーム引き分け：{2}".format(homeWinNum, homeLostNum, homeDrawNum))
print("ビジター勝ち：{0}、ビジター負け：{1}、ビジター引き分け：{2}".format(visitorWinNum, visitorLostNum, visitorDrawNum))

dfHomeSeibuWinGrpDayOfWeek = dfHomeSeibuWin.groupby(['曜日'])['月日'].count()
dfHomeSeibuWinGrpDayOfWeek = dfHomeSeibuWinGrpDayOfWeek.reindex(['月', '火', '水', '木', '金', '土', '日'])

dfHomeSeibuLostGrpDayOfWeek = dfHomeSeibuLost.groupby(['曜日'])['月日'].count()
dfHomeSeibuLostGrpDayOfWeek = dfHomeSeibuLostGrpDayOfWeek.reindex(['月', '火', '水', '木', '金', '土', '日'])

dfHomeSeibuDrawGrpDayOfWeek = dfHomeSeibuDraw.groupby(['曜日'])['月日'].count()
dfHomeSeibuDrawGrpDayOfWeek = dfHomeSeibuDrawGrpDayOfWeek.reindex(['月', '火', '水', '木', '金', '土', '日'])

dfHomeSeibuDayOfWeek = pd.DataFrame({"勝ち":dfHomeSeibuWinGrpDayOfWeek, 
                                     "負け":dfHomeSeibuLostGrpDayOfWeek, 
                                     "引分":dfHomeSeibuDrawGrpDayOfWeek})

dfHomeSeibuDayOfWeek = dfHomeSeibuDayOfWeek.fillna(0)
print(dfHomeSeibuDayOfWeek)

