import matplotlib
import pandas as pd
import pymysql 
import matplotlib.pyplot as plt 
#%matplotlib inline
import seaborn as sns 
sns.set()

conn = pymysql.connect(host='localhost', user = 'root', password='tjsals6092', db = 'DC',charset = 'utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)

sql = '''CREATE TABLE Seoul_temp( 
col_vriable1 varchar (15) not null comment 'date' primary key, 
col_vriable2 int(15) null comment 'month', 
col_vriable3 int(15) null comment 'avg_temp'
) 
'''
curs.execute(sql)

stores_info = pd.read_csv('/Users/dclab/Desktop/data_set/Seoul_temp_2017.csv')

for index, row in DC_DB.iterrows():
    tu = ( row.date, row.month,row.avg_temp)
    curs.execute("""INSERT IGNORE INTO Store_Seoul_Info (col_variable1, col_variable2, col_variable3) VALUES (%s,%s,%s)"""
    ,tu)


conn.commit()
conn.close()
