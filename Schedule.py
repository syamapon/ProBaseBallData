import pandas as pd
import matplotlib.pyplot as plt
import glob

def getSchedule():

    # ファイル読み込み
    files = glob.glob("Data/スケジュール/*")
    dfSchedule = None
    for file in files:
        dfOneSchedule = pd.read_csv(file)
        dfOneSchedule['年'] = file.split('_')[1]
        dfSchedule = pd.concat([dfSchedule, dfOneSchedule])

    # 月日曜日に分割
    dfMonthDayWeek = dfSchedule['月日'].fillna(method='ffill').str.extract('(.+)/(.+)（(.+)）')

    # ホームチーム　ホームチーム得点 ビジターチーム得点 ビジターチームに分割
    dfHomeVisitor = dfSchedule['対戦カード'].str.extract('(.+) (.+) - (.+) (.+)')

    # 勝敗(H:ホーム、V：ビジター、D：引分）の取得
    def winHVD(row):
        if row[1] > row[2]:
            return 'H'
        elif row[2] > row[1]:
            return 'V'
        else:
            return 'D'
    dsWinHVD = dfHomeVisitor.apply(lambda row:winHVD(row), axis=1)

    # 開始時間、球場
    dfStartTime = dfSchedule['球場・開始時間'].str.extract('(.+) (.+)')

    # 勝ち投手、負け投手
    dfPitcher = dfSchedule['予告先発／責任投手'].str.extract('(.+)：(.+) (.+)：(.+)')

    dfSeazon = pd.DataFrame({'年':dfSchedule['年'],
                            '月':dfMonthDayWeek[0],
                            '日':dfMonthDayWeek[1],
                            '曜日':dfMonthDayWeek[2],
                            'ホームチーム':dfHomeVisitor[0],
                            'ビジターチーム':dfHomeVisitor[3],
                            'ホームチーム得点':dfHomeVisitor[1],
                            'ビジターチーム得点':dfHomeVisitor[2],
                            '開始時間':dfStartTime[0],
                            '球場':dfStartTime[1],
                            '勝敗':dsWinHVD,
                            '勝ち投手':dfPitcher[0],
                            '負け投手':dfPitcher[1]})


    # 勝ちチーム・負けチーム
    def winOrLossTeam(row, isWin):
        if row['勝敗'] == 'H':
            if isWin:
                return row['ホームチーム']
            else:
                return row['ビジターチーム']
        elif row['勝敗'] == 'V':
            if isWin:
                return row['ビジターチーム']
            else:
                return row['ホームチーム']
        else:
            return None
    dfSeazon['勝ちチーム'] = dfSeazon.apply(lambda row:winOrLossTeam(row, True), axis=1)
    dfSeazon['負けチーム'] = dfSeazon.apply(lambda row:winOrLossTeam(row, False), axis=1)


    return dfSeazon