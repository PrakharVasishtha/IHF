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


credential_file = '/media/pi/pi/IHF3/Python/creds.json'
with open(credential_file, 'rb') as input:
    usr_creds= json.load(input)
today = dt.datetime.today()

#SQL Pre Initiation
mydb = mysql.connector.connect(
  host="localhost",
  user="user1",
  password="fd74F&fs",
  database="IHF3D"
)

mycursor = mydb.cursor()


# Per Watchlist

# Zerodha Instance
usr_creds['trade_watchlist']=2
z = ZerodhaConnect(usr=usr_creds, headless = False)  
z.subscribe(time_interval = 1,mode = ZC.MODE_LTP)    


def on_ticks(ticks):
    sid=51
    for tic in ticks:
        print(tic['ltp'])
        x=tic['ltp']
        sql = "UPDATE stocksltp SET ltp = %s WHERE stockid = %s"
        val = (x, sid)
        mycursor.execute(sql, val)
        mydb.commit()
        sid =sid+1
        print(mycursor.rowcount, "record(s) affected")
        
    exit(1)
    
z.on_ticks=on_ticks
    
z.start()
z.join()
z.stop()
os.system("killall chromium-browser-v7")

