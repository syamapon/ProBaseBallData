import pandas as pd
import matplotlib.pyplot as plt

dfMember2020 = pd.read_csv("Data/西武ライオンズ_打撃成績/2020年.csv", index_col='選手')
dfMember2019 = pd.read_csv("Data/西武ライオンズ_打撃成績/2019年.csv", index_col='選手')
dfMember2018 = pd.read_csv("Data/西武ライオンズ_打撃成績/2018年.csv", index_col='選手')
dfMember2017 = pd.read_csv("Data/西武ライオンズ_打撃成績/2017年.csv", index_col='選手')

# 2020年に100試合以上出場した選手
#print(dfMember2019 [dfMember2019 ['試合'] > 100][['選手', '試合']])

# merageを用いた方法
members1920 = pd.merge(dfMember2019, dfMember2020, left_index=True, right_index=True, how='outer', suffixes=('_2019', '_2020')) 
members1718 = pd.merge(dfMember2017, dfMember2018, left_index=True, right_index=True, how='outer', suffixes=('_2017', '_2018'))
members = pd.merge(members1920, members1718, left_index=True, right_index=True, how='outer')

members100over = members [members['試合_2020'] > 80][members['試合_2019'] > 80][members['試合_2018'] > 80][members['試合_2017'] > 80]
print(members100over.loc[:, ['試合_2017', '試合_2018', '試合_2019', '試合_2020']])

# concatを用いた方法
dfMembers = pd.concat({'2020':dfMember2020, '2019':dfMember2019, '2018':dfMember2018}, axis=1)
dfMembers100Over =  dfMembers[dfMembers['2020', '試合'] > 100][dfMembers['2019', '試合'] > 100][dfMembers['2018', '試合'] > 100]
dfMembers100Over.loc[:, [('2020', '試合'), ('2019', '試合'), ('2018', '試合')]]
