"""
"""

from Schedule import getSchedule
import pandas as pd

dfSchedule = getSchedule()

winNum = dfSchedule.groupby(['年', '月', '勝ちチーム']).count()['勝敗']
lossNum = dfSchedule.groupby(['年', '月', '負けチーム']).count()['勝敗']

winNum.index.names = ['年', '月', 'チーム']
lossNum.index.names = ['年', '月', 'チーム']

winLossNum = pd.merge(winNum, lossNum, left_index=True, right_index=True)

winLossNum.loc['2020', :, 'オリックス']


