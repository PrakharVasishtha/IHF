import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium import *
from selenium.webdriver.common.keys import Keys
from SOURCES.SOURCE import *
import mysql.connector
from SOURCES.BaseSrcStockFinancials import *
from COMMON.Common import *




def SrcStockFin():
    print("-----------------------------------------")
    print("-----Starting SrcStockFin----")
    #SQL Pre Initiation
    mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="fd74F&fs",
     database="SOURCES"
    )
    mycursor = mydb.cursor()

    
    
    #Looping through all stocks
    #IDBI
    for sid in range(156,251):
        time.sleep(1)
        symbol=FindTTSymbol(sid)
        print(symbol)
        # Webdriver Initiation
        driver = webdriver.Chrome()
        # Opening webpage for the symbol
        driver.get("https://www.tickertape.in/stocks/abbott-india-ABOT?checklist=basic")
        time.sleep(1)
        driver.set_window_size(1224, 568)
        SearchBar=driver.find_element(By.XPATH, "//input[@id='search-stock-input']")
        SearchBar.send_keys(symbol)
        time.sleep(4)
        SearchBar.send_keys(Keys.RETURN)
        time.sleep(12)
        
        # Getting PE
        try:
            PE=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]")
            #print("PE")
        except Exception as Argument:
            PE=100
            print("Problem in PE")
            Logger("LogSrcStockFinancialsError.txt",Argument,"PE")
            Logger("LogSrcStockFinancialsError.txt",symbol,"PE")
        PE1=ConvertToInt(PE.text)
        #print(PE1)
        
        
        # Processing URL
        url1=driver.current_url
        url2=url1.replace("?checklist=basic","/financials?checklist=basic&period=annual&statement=income&view=normal")
        url3=url1.replace("?checklist=basic","/financials?checklist=basic&period=quarter&statement=income&view=normal")
        url4=url1.replace("?checklist=basic","/financials?checklist=basic&period=annual&statement=balancesheet&view=normal")
        time.sleep(1)
        driver.close()
        driver.quit()
        
        time.sleep(2)
        try:
            x=Yearly(url2)
            Rvn0A=x[0]
            Rvn1A=x[1]
            Rvn2A=x[2]
            Inc0A=x[3]
            Inc1A=x[4]
            Inc2A=x[5]
            MSC=x[6]
            OB=x[7]
        except Exception as Argument:
            print("Problem in Yearly")
            Logger("LogSrcStockFinancialsError.txt",Argument,"Yearly")
            Logger("LogSrcStockFinancialsError.txt",symbol,"Yearly")
            Rvn0A=0
            Rvn1A=0
            Rvn2A=0
            Inc0A=0
            Inc1A=0
            Inc2A=0
            MSC=0
            OB=0
        #print(x)
        
        time.sleep(3)
        
        try:
            y=Quaterly(url3)
            RvnQ0A=y[0]
            RvnQ1A=y[1]
            RvnQ2A=y[2]
            IncQ0A=y[3]
            IncQ1A=y[4]
            IncQ2A=y[5]
        except Exception as Argument:
            print("Problem in Quaterly")
            Logger("LogSrcStockFinancialsError.txt",Argument,"Quaterly")
            Logger("LogSrcStockFinancialsError.txt",symbol,"Quaterly")
            RvnQ0A=0
            RvnQ1A=0
            RvnQ2A=0
            IncQ0A=0
            IncQ1A=0
            IncQ2A=0
            
        
        #print(y)
        
        time.sleep(3)

        try:
            NADif=NADiffun(url4)
        except Exception as Argument:
            print("Problem in NADiffun")
            Logger("LogSrcStockFinancialsError.txt",Argument,"NADiffun")
            Logger("LogSrcStockFinancialsError.txt",symbol,"NADif")
            NADif=0
        
        #print(NADif)
        time.sleep(1)
        
        
    
        # Updating Table SQL
        sql = "UPDATE StockFin SET RevYr0 = %s, RevYr1 = %s, RevYr2 = %s, RevQt0 = %s, RevQt1 = %s, RevQt2 = %s, IncmYr0 = %s, IncmYr1 = %s, IncmYr2 = %s, IncmQt0 = %s, IncmQt1 = %s, IncmQt2 = %s, MktShrChng = %s, PE = %s, TtlEqty = %s, OvrUndrBght = %s  WHERE StockID = %s"
        val = (Rvn0A, Rvn1A, Rvn2A, RvnQ0A, RvnQ1A, RvnQ2A, Inc0A, Inc1A, Inc2A, IncQ0A, IncQ1A, IncQ2A, MSC, PE1, NADif, OB, sid)
        mycursor.execute(sql, val)
        mydb.commit()
        #print(mycursor.rowcount, "record(s) affected")


        print("-------------------------------------")
        
        #Updating Database 
        
        
#SrcStockFin()
