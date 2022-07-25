
from Brokers.Zerodha import ZC, ZerodhaConnect
from Loggers.StockDataLogger import StockLogger
from signal import signal, SIGINT
from sys import exit
import threading

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

'''
Put the credential in following format in credential_file
{"usr":"AB1234", "pswd":"abcdef@1234',"pin":"123456","trade_watchlist":1}
'''

#Get the crederntial from following Json File change the path if required
credential_file = '/media/pi/Pi1Ext4/IHF3/Python/creds.json'
with open(credential_file, 'rb') as input:
    usr_creds= json.load(input)
today = dt.datetime.today()

#hs_logger = StockLogger(chunk_size = 100)

z = ZerodhaConnect(usr=usr_creds, headless = False)  
z.subscribe(time_interval = 1,mode = ZC.MODE_LTP)    
#z.set_logger(hslogger=hs_logger)


def on_ticks(ticks):
    for tic in ticks:
        print(tic['ltp'])
        
    exit(1)
    
z.on_ticks=on_ticks
    
z.start()
z.join()