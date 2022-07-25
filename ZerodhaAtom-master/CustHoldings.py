import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from SOURCES.SOURCE import *
from COMMON.Common import *
from CUSTOMER.CUSTOMER import *
import mysql.connector
from SOURCES.BaseSrcStockFinancials import *



def CustHoldings():
    #SQL Pre Initiation
    mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="fd74F&fs",
     database="CUSTOMER"
    )
    mycursor = mydb.cursor()

    print("-------------***************************---------- ")
    print("-------------Starting CustHoldings.py ---------- ")
    
    
    
    #Looping through all stocks
    CustNumber=NumberOfCustomer()

    for CustomerID in range(1,CustNumber+1):
        print("------------ Cleaning CustHoldings ---------- ")
        for ID in range(1,251):
            # Updating table CustHoldings
            sql = "UPDATE CustHoldings SET QuantityToday = 0,QuantityOld = 0, PercentChange = 0 WHERE StockID = %s AND CustID =%s"
            val = (ID, CustomerID )
            mycursor.execute(sql, val)
            mydb.commit()
            #print(mycursor.rowcount, "record(s) affected of TotalQuantity for Customer",CustomerID,"and StockID",ID)
        
        
        #Initiating Variables:
          
        print("-----Starting CustomerID :--- ", CustomerID)
        login=CustLogin(CustomerID)
        print(login)
        UsrID=login[0][0]
        Psw=login[0][1]
        PIN=login[0][2]
        print("Starting fetch",UsrID,Psw,PIN)
        # Webdriver Initiation
        driver = webdriver.Chrome()
        # Opening webpage for the symbol
        driver.get("https://kite.zerodha.com")
        time.sleep(1)
        driver.set_window_size(1224, 568)
        UserBox=driver.find_element(By.XPATH, "//input[@id='userid']")
        UserBox.send_keys(UsrID)
        time.sleep(1)
        PswBox=driver.find_element(By.XPATH, "//input[@id='password']")
        PswBox.send_keys(Psw)
        time.sleep(2)
        SubmitBox=driver.find_element(By.XPATH, "//button[@type='submit']")
        SubmitBox.click()
        time.sleep(3)
        try:
            try:
                UserBox=driver.find_element(By.XPATH, "//input[@id='pin']")
                UserBox.send_keys(PIN)
            except:
                print("2nd attempt")
                time.sleep(5)
                UserBox=driver.find_element(By.XPATH, "//input[@id='pin']")
                UserBox.send_keys(PIN)
        except:
                driver.quit()
                time.sleep(1)
                break
        SubmitBox=driver.find_element(By.XPATH, "//button[@type='submit']")
        SubmitBox.click()
        
        time.sleep(3)
        
        # -----------------------getting Old Holdings---------------------------
        print("Getting holdings Webpage")
        driver.get("https://kite.zerodha.com/holdings")
        time.sleep(5)

        i=0
        j=0
        k=0
        ValueArray=[0]*20
        SymbolArray=[0]*20
        NoOfSharesArray=[0]*20
        StkIDArray=[0]*20
        PerArray=[0]*20
        while k == 0:
            j=j+1
            Value_selector="tbody tr:nth-child("+str(j)+") td:nth-child(5) div:nth-child(1)"
            Symbol_selector="body > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > table:nth-child(2) > tbody:nth-child(2) > tr:nth-child("+str(j)+") > td:nth-child(1) > span:nth-child(1)"
            Percent_selector="/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/table[1]/tbody[1]/tr["+str(j)+"]/td[7]/span[1]"
            try:
                Value=driver.find_element(By.CSS_SELECTOR, Value_selector).text
                #print("Value1",Value)
                if Value=="N/A":
                    Value=0
                else:
                    Value=ConvertToInt(Value)
                ValueArray[i]=Value
                Percent=driver.find_element(By.XPATH, Percent_selector).text
                Percent=ConvertToInt(Percent)
                #print(Percent)
                PerArray[i]=Percent
                SymbolArray[i]=driver.find_element(By.CSS_SELECTOR, Symbol_selector).text
                
                try:
                    StkIDArray[i]=FindStockID(SymbolArray[i])
                    LTP=FindLtp(StkIDArray[i])
                    NoOfSharesArray[i]=int(ValueArray[i]/LTP)
                except Exception as Argument:
                    print("Symbol Not Found for Symbol:",SymbolArray[i])
                    f = open("ErrorLog.txt", "a")
                    f.write(str(Argument))
                    f.write(": Exception in CustHoldings, cant find Symbol in stocksid:")
                    f.write(": Symbol :")
                    f.write(SymbolArray[i])
                    f.write("\n")
                    f.close()
                    i=i-1
                
            except:
                k=1
                break
            i=i+1
        AL1=i+2
        #print("array length",i)
        #print("StkIDArray",StkIDArray)
        #print("PerArray",PerArray)
        #print("SymbolArray",SymbolArray)
        #print("NoOfSharesArray",NoOfSharesArray)
        #print("old holding finished for Customer :", CustomerID)
        # Updating table CustHoldings
        for AI in range(1,AL1):
            QTY=NoOfSharesArray[AI-1]
            SID=StkIDArray[AI-1]
            PC=PerArray[AI-1]
            if QTY==0:
                PC=0
            #print("PC:",PC)
            sql = "UPDATE CustHoldings SET QuantityOld = %s, PercentChange = %s WHERE StockID = %s AND CustID =%s"
            val = (QTY,PC, SID, CustomerID )
            mycursor.execute(sql, val)
            mydb.commit()
            #print(mycursor.rowcount, "record(s) affected ",CustomerID,"and StockID",AI)

        
        
        #------------------------ getting Todays Holdings ------------------------------
        #print("Getting positions Webpage")
        driver.get("https://kite.zerodha.com/positions")
        time.sleep(5)
        
        k=0
        j=1
        Array1=[0]*20
        Array2=[0]*20
        
        for ind in range(1,20):
            try:
                selector1="/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/table[1]/tbody[1]/tr["+str(j)+"]/td[3]/span[1]"
                Symbol=driver.find_element(By.XPATH, selector1).text
                #print(Symbol)
                Array2[j-1]=FindStockID(Symbol)
                #print(Array2[j-1])
                selector2="/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/table[1]/tbody[1]/tr["+str(j)+"]/td[4]"
                Num=driver.find_element(By.XPATH, selector2).text
                Num=ConvertToInt(Num)
                print(Num)
                if Num<1:
                    Num=0
                Array1[j-1]=Num
                j=j+1
            except:
                break
        AL2=j+1
        
            
        print("positions array length :",j)
        print("positions finished for Customer:",CustomerID)
        print("Quantity:",Array1)
        print("StockID :",Array2)
        # Updating table CustHoldings
        for OI in range(1,AL2):
            QTY=Array1[OI-1]
            SID=Array2[OI-1]
            sql = "UPDATE CustHoldings SET QuantityToday = %s WHERE StockID = %s AND CustID =%s"
            val = (QTY,SID, CustomerID )
            mycursor.execute(sql, val)
            mydb.commit()
            #print(mycursor.rowcount, "record(s) affected ",CustomerID,"and StockID",OI)
        
        
        
        
        for UI in range(1,251):
            sql = "SELECT QuantityToday,QuantityOld FROM CustHoldings WHERE StockID = %s AND CustID =%s"
            val = (UI, CustomerID )
            x=mycursor.execute(sql, val)
            myresult = mycursor.fetchall()
            QuantityToday=myresult[0][0]
            QuantityOld=myresult[0][1]
            TotalQuantity=QuantityOld+QuantityToday
            # Updating table CustHoldings
            sql = "UPDATE CustHoldings SET TotalQuantity = %s WHERE StockID = %s AND CustID =%s"
            val = (TotalQuantity,UI, CustomerID )
            mycursor.execute(sql, val)
            mydb.commit()
            #print(mycursor.rowcount, "record(s) affected of TotalQuantity for Customer",CustomerID,"and StockID",UI)
        
        
        
        
        
        
        print("-------Finished-------- Customer -",CustomerID,"---------")
        driver.quit()
        
    print("-------------Finished CustHoldings.py ---------- ")
    print("---------------***********--------------------------- ---------- ")
   
        
#CustHoldings()

