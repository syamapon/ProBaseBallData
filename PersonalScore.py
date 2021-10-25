"""
西武ライオンズ・山川選手の年度別本塁打数
"""

import pandas as pd
import matplotlib.pyplot as plt

dfMember2020 = pd.read_csv("Data/西武ライオンズ_打撃成績/2020年.csv", index_col='選手')
dfMember2019 = pd.read_csv("Data/西武ライオンズ_打撃成績/2019年.csv", index_col='選手')
dfMember2018 = pd.read_csv("Data/西武ライオンズ_打撃成績/2018年.csv", index_col='選手')
dfMember2017 = pd.read_csv("Data/西武ライオンズ_打撃成績/2017年.csv", index_col='選手')
dfMember2016 = pd.read_csv("Data/西武ライオンズ_打撃成績/2016年.csv", index_col='選手')
dfMember2015 = pd.read_csv("Data/西武ライオンズ_打撃成績/2015年.csv", index_col='選手')

dfMembers = pd.concat({'2020':dfMember2020, 
                       '2019':dfMember2019, 
                       '2018':dfMember2018, 
                       '2017':dfMember2017, 
                       '2016':dfMember2016, 
                       '2015':dfMember2015}, axis=0)

scoreYamakawa = dfMembers.xs('山川　穂高', level='選手')

fig, axes = plt.subplots(2, 2)


axes[0, 0].plot(scoreYamakawa['試合'])
axes[0, 1].plot(scoreYamakawa['本塁打'])
plt.show()
