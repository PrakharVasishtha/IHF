import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium import *
from selenium.webdriver.common.keys import Keys
from SOURCES.SOURCE import FindSymbol
import mysql.connector



def SrcStocksRecommendations():
    print("-----------------------------------------")
    print("-----Starting SrcStocksRecmmendations----")

    #SQL Pre Initiation
    mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="fd74F&fs",
     database="SOURCES"
    )
    mycursor = mydb.cursor()

    #Webdriver Initiation
    driver = webdriver.Chrome()
    driver.get("https://www.tickertape.in")
    driver.set_window_size(1224, 568)
    #time.sleep(2)
    driver.get("https://www.tickertape.in/stocks/hdfc-bank-HDBK?checklist=basic")

    #Looping through all stocks
    for sid in range(12,251):
        symbol=FindSymbol(sid)
        print(symbol)
        #Opening webpage for the symbol
    
        SearchBar=driver.find_element(By.XPATH, "//input[@id='search-stock-input']")
        SearchBar.send_keys(symbol)
        time.sleep(3)
        SearchBar.send_keys(Keys.RETURN)
        time.sleep(3)


        #Finding StickerTape Recommendations
        try:
            TitleLink=driver.find_element(By.XPATH, "//span[@class='jsx-3770717616 percBuyReco-value typography-h5 text-primary ']")
            x=int(TitleLink.text[0])
            y=TitleLink.text[1]
            if y == "\n":
                y=0
            else:
                y=int(TitleLink.text[1])
            z=(x*10)+y
            print(z)
        except:
            print("exception")
            z=0
            print(z)
            
            
        #Updating Table SQL
        sql = "UPDATE StockRecommendations SET Rcm1 = %s WHERE StockID = %s"
        val = (z, sid)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")



    time.sleep(1)
    driver.quit()
    print("-----Finished SrcStocksRecmmendations----")
    print("-----------------------------------------")

#SrcStocksRecommendations()