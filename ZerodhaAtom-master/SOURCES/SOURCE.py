import mysql.connector

#SQL Pre Initiation
    
mydb = mysql.connector.connect(
host="localhost",
user="user1",
password="fd74F&fs",
database="SOURCES"
)

def ConvertToInt(x):
    x1=x.replace(",","")
    x2=x1.replace("%","")
    x3=int(float(x2))
    return(x3)



def WatchListNo(StkID):
    Wln=1
    if StkID > 50:
        Wln=2
    if StkID > 100:
        Wln=3
    if StkID > 150:
        Wln=4
    if StkID > 200:
        Wln=5
    return Wln

def FindSymbol(StkID):
    mycursor = mydb.cursor()
    sql = "SELECT symbol from stocksid WHERE stockid = %s"
    val = (StkID,)
    x=mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult[0][0]

def FindStockID(Sym):
    mycursor = mydb.cursor()
    try:
        sql = "SELECT stockid from stocksid WHERE symbol = %s"
        val = (Sym,)
        x=mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
    except:
        print("NOT FOUND",Sym)
    return myresult[0][0]

def FindTTSymbol(StkID):
    mycursor = mydb.cursor()
    sql = "SELECT TTSymbol from stocksid WHERE stockID = %s"
    val = (StkID,)
    x=mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult[0][0]


def FindLtp(StkID):
    mycursor = mydb.cursor()
    sql = "SELECT ltp from stocksltp WHERE stockid = %s"
    val = (StkID,)
    x=mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult[0][0]
    
def FindStockPrice1(StkID):
    mycursor = mydb.cursor()
    sql = "SELECT Price1 from StocksPriceHist WHERE stockID = %s"
    val = (StkID,)
    x=mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult[0][0]

def FindStockPrice2(StkID):
    mycursor = mydb.cursor()
    sql = "SELECT Price2 from StocksPriceHist WHERE stockID = %s"
    val = (StkID,)
    x=mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult[0][0]

def FindStockPrice3(StkID):
    mycursor = mydb.cursor()
    sql = "SELECT Price3 from StocksPriceHist WHERE stockID = %s"
    val = (StkID,)
    x=mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult[0][0]

def FindStockPrice4(StkID):
    mycursor = mydb.cursor()
    sql = "SELECT Price4 from StocksPriceHist WHERE stockID = %s"
    val = (StkID,)
    x=mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult[0][0]

#print(FindStockPrice3(1))

#print(FindLtp(57))
#print(FindStockID("GULFOILLUB"))
#print(FindSymbol(57))
#print(ConvertToInt("-19.27%"))

