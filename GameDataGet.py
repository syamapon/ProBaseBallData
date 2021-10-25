"""
ゲームスコアデータをWEBから取得
"""

import pandas as pd
import datetime as dt

from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

import sqlite3

con = sqlite3.connect('GAMEDATA_YEAR.sqlite')

stmt = "DROP TABLE GAMESCORE"
con.execute(stmt)

stmt = """
CREATE TABLE GAMESCORE
(
    DAY VARCHAR(8),
    FRSTTEAM VARCHAR(90),
    SECDTEAM VARCHAR(90),
    INN1FRST VARCHAR(5),
    INN2FRST VARCHAR(5),    
    INN3FRST VARCHAR(5),
    INN4FRST VARCHAR(5),   
    INN5FRST VARCHAR(5),
    INN6FRST VARCHAR(5),    
    INN7FRST VARCHAR(5),
    INN8FRST VARCHAR(5),      
    INN9FRST VARCHAR(5),    
    INN10FRST VARCHAR(5),
    INN1SECD VARCHAR(5),
    INN2SECD VARCHAR(5),    
    INN3SECD VARCHAR(5),
    INN4SECD VARCHAR(5),   
    INN5SECD VARCHAR(5),
    INN6SECD VARCHAR(5),    
    INN7SECD VARCHAR(5),
    INN8SECD VARCHAR(5),      
    INN9SECD VARCHAR(5),    
    INN10SECD VARCHAR(5),   
    RFRST VARCHAR(5),     
    RSECD VARCHAR(5),      
    HFRST VARCHAR(5),     
    HSECD VARCHAR(5),   
    EFRST VARCHAR(5),     
    ESECD VARCHAR(5)
)
"""
con.execute(stmt)

stmt = """
INSERT INTO GAMESCORE VALUES (?, ?, ?, 
                              ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                              ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                              ?, ?, ?, ?, ?, ?)
"""



def getNumStr(org):
    try:
        return str(int(org))
    except:
        return org


for year in range(22):
    print("YEAR:" + str(year))
    
    for month in range(13):
        url = 'https://npb.jp/bis/20' + '{:02d}'.format(year) + '/calendar/index_' + '{:02d}'.format(month) + '.html'
        res = requests.get(url)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            for link in soup.find_all('a'):
                href = link.get("href")
                
                search = 'bis/20' + '{:02d}'.format(year) + '/games/s20' + '{:02d}'.format(year)
                if search in href:
                    getUrl = 'https://npb.jp/' + href
                    try:
                        tables = pd.read_html(getUrl)

                        # 年月日
                        monthday = href[17:25]

                        # 得点経過
                        firstTeam = tables[5][0][1]
                        secondTeam = tables[5][0][2]
                        day = '20' + '{:02d}'.format(year) + '{:02d}'.format(month)

                        data = (monthday, firstTeam, secondTeam,
                                getNumStr(tables[5][1][1]), getNumStr(tables[5][2][1]), getNumStr(tables[5][3][1]), getNumStr(tables[5][5][1]), getNumStr(tables[5][6][1]), 
                                getNumStr(tables[5][7][1]), getNumStr(tables[5][9][1]), getNumStr(tables[5][10][1]), getNumStr(tables[5][11][1]), getNumStr(tables[5][12][1]), 
                                getNumStr(tables[5][1][2]), getNumStr(tables[5][2][2]), getNumStr(tables[5][3][2]), getNumStr(tables[5][5][2]), getNumStr(tables[5][6][2]), 
                                getNumStr(tables[5][7][2]), getNumStr(tables[5][9][2]), getNumStr(tables[5][10][2]), getNumStr(tables[5][11][2]), getNumStr(tables[5][12][2]),  
                                getNumStr(tables[5][13][1]), getNumStr(tables[5][13][2]),
                                getNumStr(tables[5][14][1]), getNumStr(tables[5][14][2]),
                                getNumStr(tables[5][15][1]), getNumStr(tables[5][15][2]) 
                                )
                        con.execute(stmt, data)

                    except Exception as e:
                        print('Not Found')

con.commit()

'''
dtStart = dt.datetime(2010, 1, 1)

for addDay in range(365 * 11):
    dtDay = dtStart + dt.timedelta(days=addDay)

    for postFix in range(1500):
        url = 'https://npb.jp/bis/' + dtDay.strftime('%Y') + '/games/s' + dtDay.strftime('%Y%m%d') + '{:05d}'.format(postFix) + '.html'
        print(url)
        try:
            tables = pd.read_html(url)
            print('Found')
        except:
            print('Not Found')






#tables = pd.read_html('https://npb.jp/bis/2021/games/s2021050501013.html')
'''
