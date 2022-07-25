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
usr_creds['trade_watchlist']=1
z = ZerodhaConnect(usr=usr_creds, headless = False)  
z.subscribe(time_interval = 1,mode = ZC.MODE_LTP)    


def on_ticks(ticks):
    sid=1
    for tic in ticks:
        x=tic['ltp']
        print(x)
        print("1st done ggggggggggggggg")

    exit(1)
    
z.on_ticks=on_ticks
 
# Zerodha Instance
usr_creds['trade_watchlist']=2
z = ZerodhaConnect(usr=usr_creds, headless = False)  
z.subscribe(time_interval = 1,mode = ZC.MODE_LTP)    
    
    
def on_ticks(ticks):
    sid=1
    for tic in ticks:
        x=tic['ltp']
        print(x)
    exit(1)
    
    
z.on_ticks=on_ticks
    
z.start()
z.join()
z.stop()