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




def CustFund():
    print("-----------------------------------------")
    print("-----------Starting CustFund.py----------")

    #SQL Pre Initiation
    mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="fd74F&fs",
     database="CUSTOMER"
    )
    mycursor = mydb.cursor()

    CustNumber=NumberOfCustomer()
    
    #Looping through all stocks
    for CustomerID in range(1,CustNumber+1):
        print("CustomerID:",CustomerID)
        #Initiating Variables:
        AvailableMargin=0
        UsedMargin=0
        CurrentValue=0   
        
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
        
        print("Getting Funds Webpage")
        driver.get("https://kite.zerodha.com/funds")
        try:
            AvailableMargin=driver.find_element(By.XPATH, "//h1[@class='value text-blue']").text
            AvailableMargin=ConvertToInt(AvailableMargin)
            print(AvailableMargin)
            UsedMargins=driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/h1[1]").text
            UsedMargins=ConvertToInt(UsedMargins)
            print(UsedMargins)
        except:
            print("Funds Skip")
            UsedMargins=0
        time.sleep(5)

        print("Getting Holdings Webpage")
        driver.get("https://kite.zerodha.com/holdings")
        try:
            CurrentValue=driver.find_element(By.XPATH, "//div[@class='holdings']//div[2]//h1[1]").text
            CurrentValue=ConvertToInt(CurrentValue)
            print(CurrentValue)
        except:
            print("Holdings Skip")
        
        TotalFund=CurrentValue+AvailableMargin+UsedMargins
        print("TotalFund:",TotalFund)
        sql = "UPDATE CustFund SET Holdings = %s, AvailableMargins = %s, UsedMargins = %s, TotalFund = %s WHERE CustID = %s"
        val = (CurrentValue, AvailableMargin,UsedMargins,TotalFund, CustomerID)
        x=mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted")
        
        
        
        print("Finished For Customer:",CustomerID)
        driver.quit()
        
    
    print("-----------Finished CustFund.py----------")
    print("-----------------------------------------")
   
        
#CustFund()

