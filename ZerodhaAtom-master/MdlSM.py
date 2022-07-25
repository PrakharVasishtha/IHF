import mysql.connector
from selenium import *
import pandas as pd
from selenium import webdriver
import time



#Fetching data from SMWL

#SQL Strategies
def MdlSM():
    print("-------------------------------")
    print("---Starting MdlSM.py---")
    mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="fd74F&fs",
     database="MODULES"
    )
    
    #selecting data from SMWL
    mycursor = mydb.cursor()
    sql = "SELECT IF2 from SMWL WHERE IndiceID = 1"
    x=mycursor.execute(sql)
    myresult = mycursor.fetchall()
    SMWL=myresult[0][0]
    print(SMWL)
    
      
    # Webdriver Initiation
    driver = webdriver.Chrome()
    # Opening webpage for the symbol
    driver.get("https://docs.google.com/spreadsheets/d/1Mzdupgb-eduwh-sMa3QHnLfhkUek1ENmtE0mT6j3FqE/edit#gid=614695683")
    time.sleep(15)
    driver.quit()

    
    
    i=0
    Cycle=0
    while i == 0:
        try:
            df=pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vT5Ij-zuMr879k-0EfslG4zC3bZulHadyKtBT7r7MLhxaryigI5QMjD9MLkpsXI5AZtS1Scqza8d1a5/pub?output=xlsx")
            print(df)
            SMWS=int(df.iloc[13][5])
            print(SMWS)
            i=1
        except:
            print("NaN")
            time.sleep(5)
            i=0
        Cycle=Cycle+1
        if Cycle==5:
            print("SMWS Cant be fetched")
            i=2
        print("Cycle :",Cycle)
    
    if i==1:
        SMWS=int(df.iloc[13][5])
        print(SMWS)
    
        # Updating Table SQL
        sql = "UPDATE SM SET Value1 = %s WHERE MdlID = 1"
        val = (SMWL, )
        mycursor.execute(sql, val)
        sql = "UPDATE SM SET Value1 = %s WHERE MdlID = 2"
        val = (SMWS, )
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
    print("---Finished MdlSM.py---")
    print("-------------------------------")

    
#MdlSM()