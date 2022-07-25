import mysql.connector
from TrBUYCAL import *
from SOURCES.SOURCE import *
import time


# Defining Buyer StrategyID | BuyTradeFlag 
def Buyer(StrID):
    StrID=StrID
    
    #Checking ToTrade Flag in Strategy In STRATEGIES
    mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="fd74F&fs",
     database="STRATEGIES"
    )
    mycursor = mydb.cursor()
    sql = "SELECT  BuyTradeFlag from Strategy WHERE StrategyID = %s"
    val = (StrID,)
    x=mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    flag=myresult[0][0]
    print("ToTradeFlag :",flag,"for StrID:",StrID)
    if flag==1:
        #SQL Pre Initiation
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="fd74F&fs",
         database="TRADER"
        )
        mycursor = mydb.cursor()
        Qty1=0
    
        # Finding IndStkLimit from SetTraderStrategy
        ISL=IndStkLimitFind(StrID)
        print("ISL :", ISL)
    
    
        #Looping Through all Stocks in stocksid table
        for ID in range(1,251):
            #finding StlTobuy
            print("StockID :", ID)
            StkID=ID
        
            #Finding LTP
            LTP=FindLtp(StkID)
        
        
            # Fetching StlToBuy=ToBuy-AlrdyBght #
            if StrID == 1:
                sql = "SELECT ToBuy, AlrdyBght, RunCountBuy from TraderStrategy1 WHERE stockid = %s"
                val = (StkID,)
            if StrID == 2:
                sql = "SELECT ToBuy, AlrdyBght, RunCountBuy from TraderStrategy2 WHERE stockid = %s"
                val = (StkID,)
            x=mycursor.execute(sql, val)
            myresult = mycursor.fetchall()
            Stl=myresult[0][0]-myresult[0][1]
            RCB=myresult[0][2]
            print("StlToBuy :", Stl)
            print("RCB :", RCB)
        
            if RCB<9 and Stl>0:
                print("calling TrBuyCal")
                time.sleep(5)
                TrBuyCal(StrID,StkID,Stl,ISL,LTP)
        
            #UpdateStockSheet
            UpdateStockSheet(StrID,Qty1,1,StkID,LTP)
        
            
    

