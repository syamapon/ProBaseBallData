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
homeWinNum = len(dfHomeSeibu[dfHomeSeibu['ホーム得点'] > dfHomeSeibu['ビジター得点']])
homeLostNum = len(dfHomeSeibu[dfHomeSeibu['ホーム得点'] < dfHomeSeibu['ビジター得点']])
homeDrawNum = len(dfHomeSeibu[dfHomeSeibu['ホーム得点'] == dfHomeSeibu['ビジター得点']])

# ビジター勝ち負け
visitorWinNum = len(dfVisitorSeibu[dfVisitorSeibu['ホーム得点'] < dfVisitorSeibu['ビジター得点']])
visitorLostNum = len(dfVisitorSeibu[dfVisitorSeibu['ホーム得点'] > dfVisitorSeibu['ビジター得点']])
visitorDrawNum = len(dfVisitorSeibu[dfVisitorSeibu['ホーム得点'] == dfVisitorSeibu['ビジター得点']])

print("ホーム勝ち：{0}、ホーム負け：{1}、ホーム引き分け：{2}".format(homeWinNum, homeLostNum, homeDrawNum))
print("ビジター勝ち：{0}、ビジター負け：{1}、ビジター引き分け：{2}".format(visitorWinNum, visitorLostNum, visitorDrawNum))