import mysql.connector
from Brokers.Zerodha import ZC, ZerodhaConnect
from Loggers.StockDataLogger import StockLogger
from signal import signal, SIGINT
from sys import exit
import threading

import time
import json
import datetime as dt

import sys
import os

def SrcStocksLtp():
    print("-------------------------------")
    print("----------SrcStocksLtp---------")

    # Zerodha pre initiation

    if len(sys.argv) > 1:
        now = dt.datetime.now() 
        if now < ZerodhaConnect.start_time or now > ZerodhaConnect.close_time:
            print('This time Market ramain closed')
            exit(1)
        
    def handler(signal_received, frame):
        print('Signler Handler is called')
        z.stop()

    signal(SIGINT, handler)


    credential_file = '/media/pi/p/V0/ZerodhaAtom-master/creds.json'
    with open(credential_file, 'rb') as input:
        usr_creds= json.load(input)
    today = dt.datetime.today()

    #SQL Pre Initiation
    mydb = mysql.connector.connect(
      host="localhost",
      user="user1",
      password="fd74F&fs",
      database="SOURCES"
    )

    mycursor = mydb.cursor()


    # Per Watchlist

    time.sleep(2)

    # Zerodha Instance 1
    usr_creds['trade_watchlist']=1
    z = ZerodhaConnect(usr=usr_creds, headless = False)  
    z.subscribe(time_interval = 1,mode = ZC.MODE_LTP)    


    def on_ticks(ticks):
        sid=1
        print("from id 1 to 51")

        for tic in ticks:
            #print(tic['ltp'])
            x=tic['ltp']
            sql = "UPDATE stocksltp SET ltp = %s WHERE stockid = %s"
            val = (x, sid)
            mycursor.execute(sql, val)
            mydb.commit()
            sid =sid+1
            #print(mycursor.rowcount, "record(s) affected")
        
        exit(1)
    
    z.on_ticks=on_ticks
    
    z.start()
    z.join()
    z.stop()
    os.system("killall chromium-browser-v7")

    time.sleep(2)

    # Zerodha Instance 2
    usr_creds['trade_watchlist']=2
    z = ZerodhaConnect(usr=usr_creds, headless = False)  
    z.subscribe(time_interval = 1,mode = ZC.MODE_LTP)    


    def on_ticks(ticks):
        sid=51
        print("from id 51 to 100")

        for tic in ticks:
            #print(tic['ltp'])
            x=tic['ltp']
            sql = "UPDATE stocksltp SET ltp = %s WHERE stockid = %s"
            val = (x, sid)
            mycursor.execute(sql, val)
            mydb.commit()
            sid =sid+1
            #print(mycursor.rowcount, "record(s) affected")
        
        exit(1)
    
    z.on_ticks=on_ticks
    
    z.start()
    z.join()
    z.stop()
    os.system("killall chromium-browser-v7")



    time.sleep(3)
    # Zerodha Instance 3
    usr_creds['trade_watchlist']=3
    z = ZerodhaConnect(usr=usr_creds, headless = False)  
    z.subscribe(time_interval = 1,mode = ZC.MODE_LTP)    


    def on_ticks(ticks):
        sid=151
        print("from id 151 to 200")

        for tic in ticks:
            #print(tic['ltp'])
            x=tic['ltp']
            sql = "UPDATE stocksltp SET ltp = %s WHERE stockid = %s"
            val = (x, sid)
            mycursor.execute(sql, val)
            mydb.commit()
            sid =sid+1
            #print(mycursor.rowcount, "record(s) affected")
        
        exit(1)
    
    z.on_ticks=on_ticks
    
    z.start()
    z.join()
    z.stop()
    os.system("killall chromium-browser-v7")

    time.sleep(5)
    # Zerodha Instance 4
    usr_creds['trade_watchlist']=4
    z = ZerodhaConnect(usr=usr_creds, headless = False)  
    z.subscribe(time_interval = 1,mode = ZC.MODE_LTP)    


    def on_ticks(ticks):
        sid=151
        print("from id 151 to 200")
        for tic in ticks:
            #print(tic['ltp'])
            x=tic['ltp']
            sql = "UPDATE stocksltp SET ltp = %s WHERE stockid = %s"
            val = (x, sid)
            mycursor.execute(sql, val)
            mydb.commit()
            sid =sid+1
            #print(mycursor.rowcount, "record(s) affected")
        
        exit(1)
    
    z.on_ticks=on_ticks
    
    z.start()
    z.join()
    z.stop()
    os.system("killall chromium-browser-v7")


    time.sleep(5)

    # Zerodha Instance 5
    usr_creds['trade_watchlist']=5
    z = ZerodhaConnect(usr=usr_creds, headless = False)  
    z.subscribe(time_interval = 1,mode = ZC.MODE_LTP)    


    def on_ticks(ticks):
        sid=201
        print("from id 201 to 250")
        for tic in ticks:
            #print(tic['ltp'])
            x=tic['ltp']
            sql = "UPDATE stocksltp SET ltp = %s WHERE stockid = %s"
            val = (x, sid)
            mycursor.execute(sql, val)
            mydb.commit()
            sid =sid+1
            #print(mycursor.rowcount, "record(s) affected")
        
        exit(1)
    
    z.on_ticks=on_ticks
    
    z.start()
    z.join()
    z.stop()
    os.system("killall chromium-browser-v7")
    print("-------------------------------")

#SrcStocksLtp()