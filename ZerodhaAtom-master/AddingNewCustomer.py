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



# Function to buy stock
def AddCustomer(CustID=1):
    #Initiating Variables:
          
    print("-----adding stocks to zerodha watchlist for CustomerID :--- ", CustID)
    login=CustLogin(CustID)
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
    SubmitBox=driver.find_element(By.XPATH, "//button[@type='submit']")
    SubmitBox.click()
        
    time.sleep(3)
        
    
    #Fetching Stocks lists for watchlist wln
    #SQL Pre Initiation
    mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="fd74F&fs",
     database="SOURCES"
    )
    mycursor = mydb.cursor()
    
    #initializing for loop x act wln
    SymbolArray=[0]*251
    for i in range(1,251):
        sql = "SELECT symbol from stocksid WHERE stockID = %s"
        val = (i,)
        x=mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        SymbolArray[i-1]=myresult[0][0]
        print(SymbolArray[i-1])
    
    time.sleep(2)
    #Watchlist No1
    element=driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]")
    print("Watchlist :", element.text)
    element.click()
    for Ind in range(1,51):
        Sym=SymbolArray[Ind-1]
        element=driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search eg: infy bse, nifty fut weekly, gold mcx']")
        print(element.text)
        element.send_keys(Sym)
        time.sleep(1)
        element.send_keys(Keys.RETURN)
        time.sleep(1)

    #Watchlist No2
    element=driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[2]")
    print("Watchlist :", element.text)
    element.click()
    for Ind in range(1,51):
        y=Ind+50
        Sym=SymbolArray[y-1]
        element=driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search eg: infy bse, nifty fut weekly, gold mcx']")
        print(element.text)
        element.send_keys(Sym)
        time.sleep(1)
        element.send_keys(Keys.RETURN)
        time.sleep(1)
    
    #Watchlist No3
    element=driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[3]")
    print("Watchlist :", element.text)
    element.click()
    for Ind in range(1,51):
        y=Ind+100
        Sym=SymbolArray[y-1]
        element=driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search eg: infy bse, nifty fut weekly, gold mcx']")
        print(element.text)
        element.send_keys(Sym)
        time.sleep(1)
        element.send_keys(Keys.RETURN)
        time.sleep(1)
    
    #Watchlist No4
    element=driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[4]")
    print("Watchlist :", element.text)
    element.click()
    for Ind in range(1,51):
        y=Ind+150
        Sym=SymbolArray[y-1]
        element=driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search eg: infy bse, nifty fut weekly, gold mcx']")
        print(element.text)
        element.send_keys(Sym)
        time.sleep(1)
        element.send_keys(Keys.RETURN)
        time.sleep(1)
    
    #Watchlist No5
    element=driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[5]")
    print("Watchlist :", element.text)
    element.click()
    for Ind in range(1,51):
        y=Ind+200
        Sym=SymbolArray[y-1]
        element=driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search eg: infy bse, nifty fut weekly, gold mcx']")
        print(element.text)
        element.send_keys(Sym)
        time.sleep(1)
        element.send_keys(Keys.RETURN)
        time.sleep(1)
    
    
    driver.quit()
   

AddCustomer(1)

