from Schedule import getSchedule

dfSchedule = getSchedule()

winNum = dfSchedule.groupby(['年', '月', '勝ちチーム']).count()['勝敗']
lossNum = dfSchedule.groupby(['年', '月', '負けチーム']).count()['勝敗']

winNum.loc['2020', :, 'オリックス']


