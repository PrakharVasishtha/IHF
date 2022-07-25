import mysql.connector


#SQL Pre Initiation
mydb = mysql.connector.connect(
  host="localhost",
  user="user1",
  password="fd74F&fs",
  database="SOURCES"
)

mycursor = mydb.cursor()



def StockSymbol(SID):
    sql = "SELECT symbol FROM stocksid WHERE stockID=%s"
    val = (SID,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for y in myresult:
        return y[0]

def StockIDArray():
    #initialize an array
    
StockIDArray()    


