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
    '''
    sql = "UPDATE stocksid SET TTSymbol = %s WHERE stockID = %s"
    val = ( sym, Ind)
    x=mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted")
    '''