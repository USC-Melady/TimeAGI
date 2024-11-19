import pandas as pd
import sqlite3

data1= pd.read_csv('data/InputData1.csv')
data2 =pd.read_csv('data/InputData2.csv')
con = sqlite3.connect('datashow.db')
data1.to_sql('inputdata1',con,if_exists='replace',index=False)
data2.to_sql('inputdata2', con, if_exists='replace', index=False)
con.close()