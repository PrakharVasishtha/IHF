import mysql.connector
from selenium import *
import pandas as pd
from selenium import webdriver
from ApiSell import *
import time
from SOURCES.SOURCE import *
from CUSTOMER.CUSTOMER import *

#SQL Strategies
#CustID should be of customer with factor>2


def SellTrader():
    print("-------------***************************---------- ")
    print("--------------Starting TrSellTrader.py ---------- ")
    #Fetching data from SMWL
    mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="fd74F&fs",
     database="MODULES"
    )
    mycursor = mydb.cursor()
    
    x=mycursor.execute("SELECT Value1 from SM WHERE MdlID = 1")
    myresult = mycursor.fetchall()
    SMWL=myresult[0][0]
    print("SMWL:",SMWL)
    x=mycursor.execute("SELECT Value1 from SM WHERE MdlID = 2")
    myresult = mycursor.fetchall()
    SMWS=myresult[0][0]
    print("SMWS",SMWS)
    
    #Fetching data from CUSTOMER, StockID and Percent
    mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="fd74F&fs",
     database="CUSTOMER"
    )
    mycursor = mydb.cursor()
    StockIDArray=[0]*30
    PercentArray=[0]*30
    FinalStockIDArray=[0]*30
    FinalPercentArray=[0]*30
    xi=0
    sql="SELECT StockID,PercentChange from CustHoldings WHERE PercentChange > 0 AND CustID=1"
    x=mycursor.execute(sql)
    StockArray = mycursor.fetchall()
    #SMWL=myresult[0][0]
    print("StockArray:",StockArray)
    length=len(StockArray)
    #print(length)
    for i in range(0,length):
        StockIDArray[i]=StockArray[i][0]
        PercentArray[i]=StockArray[i][1]
    print("StockIDArray",StockIDArray)
    print("PercentArray",PercentArray)
    # Desperate Case: SMWL<10 and SMWS < 1 and PC >1
    if SMWL<10 and SMWS < 1:
        for ind in range(0,length):
            if PercentArray[ind] > 1:
                FinalStockIDArray[xi]=StockIDArray[ind]
                FinalPercentArray[xi]=PercentArray[ind]
            xi=xi+1

    # LongTerm Case: SMWL has Fallen and SMWS has fallen somewhat
    #                SMWL<10 and SMWS<12
    SMWL < 10 and SMWS < 12 and PC >9
    if SMWL<1 and SMWS < 12:
        for ind in range(0,length):
            if PercentArray[ind] > 9:
                if StockIDArray[ind] not in FinalStockIDArray:
                    FinalStockIDArray[xi]=StockIDArray[ind]
                    FinalPercentArray[xi]=PercentArray[ind]
                    xi=xi+1
    # ShorTerm Case: SMWL has not fallen but only SMWS has fallen.
    #                80 < SMWL < 250 and SMWS < 3 and PC >4
    if SMWL>80 and SMWL<250 and SMWS < 1:
        for ind in range(0,length):
            if PercentArray[ind] > 4:
                if StockIDArray[ind] not in FinalStockIDArray:
                    FinalStockIDArray[xi]=StockIDArray[ind]
                    FinalPercentArray[xi]=PercentArray[ind]
                    xi=xi+1
    # Common Case: SMWL < 50 and SMWS < 8 and PC >7
    if SMWL<100 and SMWS < 8:
        for ind in range(0,length):
            if PercentArray[ind] > 7:
                if StockIDArray[ind] not in FinalStockIDArray:
                    FinalStockIDArray[xi]=StockIDArray[ind]
                    FinalPercentArray[xi]=PercentArray[ind]
                    xi=xi+1


    print("FinalStockIDArray",FinalStockIDArray)
    print("FinalPercentArray",FinalPercentArray)
    print("Length Of Array",xi)
    
    CustNumber=NumberOfCustomer()
    # Selling Stocks
    for CID in range(1,CustNumber+1):
        print("Orders for Customer:",CID)
        for Ar in range(0,xi):
            StkID=FinalStockIDArray[Ar]
            Sym=FindSymbol(StkID)
            Qty=CustStockQty(CID,StkID)
            Wln=WatchListNo(StkID)
            Trade=SellStock(Sym,Qty,Wln,CID)
            
            
    
    print("-------------Finished TrSellTrader.py ---------- ")
    print("---------------***********--------------------------- ---------- ")
    
    
#SellTrader()
