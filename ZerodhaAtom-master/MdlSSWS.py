import pandas as pd
import mysql.connector
from MODULES.BaseModule import *
from SOURCES.SOURCE import *
import time
from selenium import webdriver


def MdlSSWS():
    print("-----------------------------------")
    print("----------MdlSSWS-----------")

    #Initiation
    SumOfGNLMPR=0
    TotalFund=100000
    print("-------------------****************----------------")
    print("------MdlSSWS.py Initiated------")


# Links for Initializing google sheets loading
# https://docs.google.com/spreadsheets/d/1p3bcZYUuH-Uw_GQ0qGHZMgzvG2WzCo0VfwkiOSzi044/edit?usp=sharing
# https://docs.google.com/spreadsheets/d/10MVZ4t0bHrvQAgRm-xtSHOmjxRTeyb3hGVDKqhMVaag/edit?usp=sharing
# https://docs.google.com/spreadsheets/d/1WLeh0icTzc0ya5OOzxu-2CXO0_JjwMB1a2HzDWf6ztI/edit?usp=sharing

    # Webdriver Initiation
    driver = webdriver.Chrome()
    # Opening webpage for the symbol
    driver.get("https://docs.google.com/spreadsheets/d/1p3bcZYUuH-Uw_GQ0qGHZMgzvG2WzCo0VfwkiOSzi044/edit?usp=sharing")
    time.sleep(15)
    driver.quit()

    driver = webdriver.Chrome()
    # Opening webpage for the symbol
    driver.get("https://docs.google.com/spreadsheets/d/10MVZ4t0bHrvQAgRm-xtSHOmjxRTeyb3hGVDKqhMVaag/edit?usp=sharing")
    time.sleep(5)
    driver.quit()

    driver = webdriver.Chrome()
    # Opening webpage for the symbol
    driver.get("https://docs.google.com/spreadsheets/d/1WLeh0icTzc0ya5OOzxu-2CXO0_JjwMB1a2HzDWf6ztI/edit?usp=sharing")
    time.sleep(5)
    driver.quit()


    mydb = mysql.connector.connect(
      host="localhost",
      user="user1",
      password="fd74F&fs",
      database="MODULES"
    )
    mycursor = mydb.cursor()

    # Fetching Gain % per share MNGNPR should be changed in SetSS to change Min Gain % to buy stocks
    
    x=mycursor.execute("SELECT MNGNPR from SetSS WHERE ModuleID = 1")
    myresult = mycursor.fetchall()
    MNGNPR=myresult[0][0]
    #print("MNGNPR :",MNGNPR)

    #  Getting Data from StockLists and calculating, updating PRGNONSLPRand GNLMPR
    #StockList1
    i=0
    Cycle=0
    while i == 0:
        try:
            df=pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vTezVc99B50U-9fDwaQsyPzW1bU1vqoX9-sPhtwZA0Qsq3Nsknl1h_WDvLEgWq7sJiwxNDoWnPi67yU/pub?output=xlsx")
            print(df)
            SMWS=int(df.iloc[3][18])
            print(SMWS)
            i=1
        except:
            print("NaN")
            i=0
        Cycle=Cycle+1
        print("Cycle :",Cycle)

    for id in range(1,101):
        SID=2+id
        PRGNONSLPR=int(df.iloc[SID][18])
        #print("StkID :", id,"PRGNONSLPR : ",PRGNONSLPR)
        sql = "UPDATE SSWS SET PRGNONSLPR = %s WHERE stockID = %s"
        val = ( PRGNONSLPR, id)
        x=mycursor.execute(sql, val)
        mydb.commit()
        #print(mycursor.rowcount, "PRGNONSLPR record inserted")
    
        Overall=FindOverall(id)
        #print("Overall :",Overall)
    
        #GNLMPR = Moderating Gain% according to Overall Rating
        GNLMPR=((PRGNONSLPR*Overall)/10)
        if GNLMPR < MNGNPR:
            GNLMPR = 0
        #print("Rationalised GainPercent act Overall: GNLMPR :",GNLMPR)
        sql = "UPDATE SSWS SET GNLMPR = %s WHERE stockID = %s"
        val = ( GNLMPR, id)
        x=mycursor.execute(sql, val)
        mydb.commit()
        #print(mycursor.rowcount, "GNLMPR record inserted")
   
    #StockList2
    i=0
    Cycle=0
    while i == 0:
        try:
            df=pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vSen4z9QEe8ZxEl0Sxt1Ci47Ab8IYp_030m6u3dSWsDz8r68BsFj7RgFwfUGa9mOKjkxxN2v0QZXXl9/pub?output=xlsx")
            print(df)
            SMWS=int(df.iloc[3][18])
            print(SMWS)
            i=1
        except:
            print("NaN")
            i=0
        Cycle=Cycle+1
        print("Cycle :",Cycle)
    for id in range(1,101):
        SID=2+id
        PRGNONSLPR=int(df.iloc[SID][18])
        IhfID=id+100
        #print("IhfID",IhfID)
        #print("StkID :", IhfID,"PRGNONSLPR : ",PRGNONSLPR)
        sql = "UPDATE SSWS SET PRGNONSLPR = %s WHERE stockID = %s"
        val = ( PRGNONSLPR, IhfID)
        x=mycursor.execute(sql, val)
        mydb.commit()
        #print(mycursor.rowcount, "PRGNONSLPR record inserted")
    
        Overall=FindOverall(IhfID)
        #print("Overall :",Overall)
    
        #GNLMPR = Moderating Gain% according to Overall Rating
        GNLMPR=((PRGNONSLPR*Overall)/10)
        if GNLMPR < MNGNPR:
            GNLMPR = 0
        #print("Rationalised GainPercent act Overall: GNLMPR :",GNLMPR)
        sql = "UPDATE SSWS SET GNLMPR = %s WHERE stockID = %s"
        val = ( GNLMPR, IhfID)
        x=mycursor.execute(sql, val)
        mydb.commit()
        #print(mycursor.rowcount, "GNLMPR record inserted")

    #StockList3
    i=0
    Cycle=0
    while i == 0:
        try:
            df=pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vSVzkq77U16AsBq4RniZncc8UlDCN64B2LqyCutcl6aMZaPQGI0I8t2TAo1RDabKjeLMDCl7EqOyFpk/pub?output=xlsx")
            print(df)
            SMWS=int(df.iloc[3][18])
            print(SMWS)
            i=1
        except:
            print("NaN")
            i=0
        Cycle=Cycle+1
        print("Cycle :",Cycle)
    
    for id in range(1,51):
        SID=2+id
        PRGNONSLPR=df.iloc[SID][18]
        #print(PRGNONSLPR)
        #print(type(PRGNONSLPR))
    
        if type(PRGNONSLPR) is float:
            PRGNONSLPR=int(PRGNONSLPR)
        else:
            PRGNONSLPR=0
        IhfID=id+200
        #print("IhfID",IhfID) 
        #print("StkID :", IhfID,"PRGNONSLPR : ",PRGNONSLPR)
        sql = "UPDATE SSWS SET PRGNONSLPR = %s WHERE stockID = %s"
        val = ( PRGNONSLPR, IhfID)
        x=mycursor.execute(sql, val)
        mydb.commit()
        #print(mycursor.rowcount, "PRGNONSLPR record inserted")
    
        Overall=FindOverall(IhfID)
        #print("Overall :",Overall)
    
        #GNLMPR = Moderating Gain% according to Overall Rating
        GNLMPR=((PRGNONSLPR*Overall)/10)
        if GNLMPR < MNGNPR:
            GNLMPR = 0
        #print("Rationalised GainPercent act Overall: GNLMPR :",GNLMPR)
        sql = "UPDATE SSWS SET GNLMPR = %s WHERE stockID = %s"
        val = ( GNLMPR, IhfID)
        x=mycursor.execute(sql, val)
        mydb.commit()
        #print(mycursor.rowcount, "GNLMPR record inserted")

    
    
    
        # Finding SumOfGNLMPR
    for id in range(1,251):
        sql = "SELECT GNLMPR from SSWS WHERE StockID = %s"
        val = (id,)
        x=mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        GNLMPR=myresult[0][0]
        #print("GNLMPR :",GNLMPR)
        SumOfGNLMPR=SumOfGNLMPR+GNLMPR
        #print("SumOfGNLMPR :",SumOfGNLMPR)
    
    if SumOfGNLMPR == 0:
        SumOfGNLMPR=1
        
    print("------SSWS UPDATE Initiated------")
    for id in range(1,251):
        #Fund allocation for particular share : PRFRFNSRB
        sql = "SELECT GNLMPR from SSWS WHERE StockID = %s"
        val = (id,)
        x=mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        GNLMPR=myresult[0][0]
        #print("GNLMPR :",GNLMPR)
        PRFRFNSRBY=((GNLMPR*TotalFund)/SumOfGNLMPR)
        #print("PRFRFNSRBY",PRFRFNSRBY)
        sql = "UPDATE SSWS SET PRFRFNSRBY = %s WHERE stockID = %s"
        val = (PRFRFNSRBY, id)
        x=mycursor.execute(sql, val)
        mydb.commit()
        #print(mycursor.rowcount, "PRFRFNSRBY record inserted")
        ltp=FindLtp(id)
        QtToBuy=int(PRFRFNSRBY/ltp)
        #print("QtToBuy",QtToBuy)
        sql = "UPDATE SSWS SET QTTOBY = %s WHERE stockID = %s"
        val = (QtToBuy, id)
        x=mycursor.execute(sql, val)
        mydb.commit()
        #print(mycursor.rowcount, "QtToBuy record inserted")
    
    print("------SSWS UPDATE Finished------")
    print("------MdlSSWS.py Finished------")
    print("-------------------****************----------------")

#MdlSSWS()