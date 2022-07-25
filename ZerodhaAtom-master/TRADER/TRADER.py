import mysql.connector


#SQL Pre Initiation
mydb = mysql.connector.connect(
  host="localhost",
  user="user1",
  password="fd74F&fs",
  database="TRADER"
)

mycursor = mydb.cursor()


def MBIS(StrID):
    sql = "SELECT MBIS FROM SetTraderStrategy WHERE StrategyID= %s"
    val = (StrID, )
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    return myresult[0][0]
    
def MBID(StrID):
    sql = "SELECT MBID FROM SetTraderStrategy WHERE StrategyID= %s"
    val = (StrID, )
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    return myresult[0][0]
    
def IndStkLimitFind(StrID):
    sql = "SELECT IndStkLimit FROM SetTraderStrategy WHERE StrategyID= %s"
    val = (StrID, )
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    return myresult[0][0]

# B=1  S=2
def UpdateStockSheet(StrID,Qty1,BS,StkID,LTP):
    if StrID == 1:
        if BS == 1:
            sql = "SELECT AlrdyBght,RunCountBuy,LBP FROM TraderStrategy1 WHERE StockID= %s"
            val = (StkID, )
            mycursor.execute(sql,val)
            myresult = mycursor.fetchall()
            AlrdyBght=myresult[0][0]
            RunCountBuy=myresult[0][1]
            LBP=myresult[0][2]
            print(AlrdyBght,RunCountBuy,LBP)
            UpAlrdyBght=AlrdyBght+Qty1
            UpRunCountBuy=RunCountBuy+1
    
            sql = "UPDATE TraderStrategy1 SET AlrdyBght = %s, RunCountBuy = %s, LBP = %s WHERE StockID = %s"
            val = (UpAlrdyBght,UpRunCountBuy,LTP, StkID)
            x=mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted")
        elif BS == 2:
            sql = "SELECT AlrdySold,RunCountSell,LSP FROM TraderStrategy1 WHERE StockID= %s"
            val = (StkID, )
            mycursor.execute(sql,val)
            myresult = mycursor.fetchall()
            AlrdySold=myresult[0][0]
            RunCountSell=myresult[0][1]
            LSP=myresult[0][2]
            print(AlrdySold,RunCountSell,LSP)
            UpAlrdySold=AlrdySold+Qty1
            UpRunCountSell=RunCountSell+1
    
            sql = "UPDATE TraderStrategy1 SET AlrdySold = %s, RunCountSell = %s, LSP = %s WHERE StockID = %s"
            val = (UpAlrdySold,UpRunCountSell,LTP, StkID)
            x=mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted")
    
    if StrID == 2:
        if BS == 1:
            sql = "SELECT AlrdyBght,RunCountBuy,LBP FROM TraderStrategy2 WHERE StockID= %s"
            val = (StkID, )
            mycursor.execute(sql,val)
            myresult = mycursor.fetchall()
            AlrdyBght=myresult[0][0]
            RunCountBuy=myresult[0][1]
            LBP=myresult[0][2]
            print(AlrdyBght,RunCountBuy,LBP)
            UpAlrdyBght=AlrdyBght+Qty1
            UpRunCountBuy=RunCountBuy+1
    
            sql = "UPDATE TraderStrategy2 SET AlrdyBght = %s, RunCountBuy = %s, LBP = %s WHERE StockID = %s"
            val = (UpAlrdyBght,UpRunCountBuy,LTP, StkID)
            x=mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted")
        elif BS == 2:
            sql = "SELECT AlrdySold,RunCountSell,LSP FROM TraderStrategy2 WHERE StockID= %s"
            val = (StkID, )
            mycursor.execute(sql,val)
            myresult = mycursor.fetchall()
            AlrdySold=myresult[0][0]
            RunCountSell=myresult[0][1]
            LSP=myresult[0][2]
            print(AlrdySold,RunCountSell,LSP)
            UpAlrdySold=AlrdySold+Qty1
            UpRunCountSell=RunCountSell+1
    
            sql = "UPDATE TraderStrategy2 SET AlrdySold = %s, RunCountSell = %s, LSP = %s WHERE StockID = %s"
            val = (UpAlrdySold,UpRunCountSell,LTP, StkID)
            x=mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted")
    
    
    
    
    
    
    return 0
                        

    
    

#UpdateStockSheet(1,5,1,2,71)