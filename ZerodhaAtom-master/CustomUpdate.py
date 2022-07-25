import mysql.connector
from SOURCES.SOURCE import *

#SQL Pre Initiation
mydb = mysql.connector.connect(
host="localhost",
user="user1",
password="fd74F&fs",
database="MODULES"
)
mycursor = mydb.cursor()

for Ind in range(1,251):
    sym=FindSymbol(Ind)
    print(sym)
    sql = "INSERT INTO SSWS (StockID,TPRC,LWTRGNPR,CRPRGN,RLEXPRACLV,SLPR,PRGNONSLPR,GNLMPR,FNSP,PRLVEXGN,GNMDPR,RLEX1,RLEX2,RLEX3,VLCRHL,SHLMCH,LTGNPR,PRFRFNSRBY,SHQT,CRSHHDQT,QTTOBY) VALUES (%s,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)"   
    val = (Ind,)
    x=mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted")
