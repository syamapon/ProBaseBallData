"""
イニング別の得点数　
"""

import sqlalchemy as sqla
import pandas as pd

def getNum(x):
    try:
        return int(x)
    except:
        return 0


db = sqla.create_engine('sqlite:///GAMEDATA_YEAR.sqlite')

stmt = """
SELECT
FRSTTEAM,
SECDTEAM,
INN1FRST,
INN2FRST,
INN3FRST,
INN4FRST,
INN5FRST,
INN6FRST,
INN7FRST,
INN8FRST,
INN9FRST,
INN10FRST,
INN1SECD,
INN2SECD,
INN3SECD,
INN4SECD,
INN5SECD,
INN6SECD,
INN7SECD,
INN8SECD,
INN9SECD,
INN10SECD
FROM
GAMESCORE
"""
seazons = pd.read_sql(stmt, db)

numSeazons = pd.DataFrame({'FRSTTEAM':seazons['FRSTTEAM'],
                           'SECDTEAM':seazons['SECDTEAM'],
                           'INN1FRST':seazons['INN1FRST'].apply(lambda x:getNum(x)),
                           'INN2FRST':seazons['INN2FRST'].apply(lambda x:getNum(x)),
                           'INN3FRST':seazons['INN3FRST'].apply(lambda x:getNum(x)),
                           'INN4FRST':seazons['INN4FRST'].apply(lambda x:getNum(x)),        
                           'INN5FRST':seazons['INN5FRST'].apply(lambda x:getNum(x)),
                           'INN6FRST':seazons['INN6FRST'].apply(lambda x:getNum(x)),
                           'INN7FRST':seazons['INN7FRST'].apply(lambda x:getNum(x)),
                           'INN8FRST':seazons['INN8FRST'].apply(lambda x:getNum(x)),    
                           'INN9FRST':seazons['INN9FRST'].apply(lambda x:getNum(x)),
                           'INN10FRST':seazons['INN10FRST'].apply(lambda x:getNum(x)),
                           'INN1SECD':seazons['INN1SECD'].apply(lambda x:getNum(x)),
                           'INN2SECD':seazons['INN2SECD'].apply(lambda x:getNum(x)),      
                           'INN3SECD':seazons['INN3SECD'].apply(lambda x:getNum(x)),
                           'INN4SECD':seazons['INN4SECD'].apply(lambda x:getNum(x)),
                           'INN5SECD':seazons['INN5SECD'].apply(lambda x:getNum(x)),
                           'INN6SECD':seazons['INN6SECD'].apply(lambda x:getNum(x)),        
                           'INN7SECD':seazons['INN7SECD'].apply(lambda x:getNum(x)),
                           'INN8SECD':seazons['INN8SECD'].apply(lambda x:getNum(x)),
                           'INN9SECD':seazons['INN9SECD'].apply(lambda x:getNum(x)),
                           'INN10SECD':seazons['INN10SECD'].apply(lambda x:getNum(x))                                                                                                                                                     
})

print(numSeazons.groupby(['FRSTTEAM', 'SECDTEAM']).agg(lambda x:x.sum()))



