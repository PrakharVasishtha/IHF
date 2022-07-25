
from Brokers.Zerodha import ZC, ZerodhaConnect
from Loggers.StockDataLogger import StockLogger
from signal import signal, SIGINT
from sys import exit
import threading
from CUSTOMER.CUSTOMER import *
import os

import time
import json
import datetime as dt

import sys


if len(sys.argv) > 1:
    now = dt.datetime.now() 
    if now < ZerodhaConnect.start_time or now > ZerodhaConnect.close_time:
        print('This time Market ramain closed')
        exit(1)
        
def handler(signal_received, frame):
    print('Signler Handler is called')
    z.stop()

signal(SIGINT, handler)



#Get the crederntial from following Json File change the path if required
credential_file = '/media/pi/p/V0/ZerodhaAtom-master/creds.json'
with open(credential_file, 'rb') as input:
    usr_creds= json.load(input)
    
today = dt.datetime.today()


# Function to buy stock
def BuyStock(Sym,Qty=1,wln=1,CustID=1):
    
    #Fetching Customer login details
    LoginDetails=["ClntID","Password","PIN"]
    x=CustLogin(CustID)
    for y in x:
        ClntID=y[0]
        pwd=y[1]
        ClntPin=y[2]
      
    
    
    
    #Custom Login parameters
    usr_creds['trade_watchlist']=wln
    usr_creds['usr']=ClntID
    usr_creds['pswd']=pwd
    usr_creds['pin']=ClntPin
    
    z = ZerodhaConnect(usr=usr_creds, headless = False)  
        
    z.subscribe(time_interval = 1,mode = ZC.MODE_LTP)
    z.place_order(symbol = Sym,
            exchange= 'NSE', 
            product = ZC.PRODUCT_TYPE_CNC,
            transaction_type =ZC.TRANSACTION_TYPE_BUY,
            order_type = ZC.ORDER_TYPE_MARKET,
            price = None, 
            qtn = Qty )
    
    z.start()
    #z.join()
    time.sleep(3)
    z.stop()
    z.driver.quit()



#k=BuyStock("ASHOKA",Qty=1,wln=1,CustID=1)
#print(k)
#BuyStock('ASHOKA',1,1,1)


