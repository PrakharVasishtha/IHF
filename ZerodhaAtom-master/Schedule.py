# Schedule Library imported
import schedule
import time
from COMMON.Common import *
from OnceInMorning import *
from CyclicRun import *
import os



  
# Functions setup
def ScheduleCyclicRun():
    Logger("LogSchedule.txt",":Start :","ScheduleCyclicRun")
    try:
        CyclicRun()
    except Exception as Argument:
        print("Problem in CyclicRun")
        Logger("LogScheduleError.txt",Argument,"CyclicRun")
    Logger("LogSchedule.txt",":end :","ScheduleCyclicRun")

def ScheduleOnceInMorning():
    Logger("LogSchedule.txt",":Start :","ScheduleOnceInMorning")
    try:
        OnceInMorning()
    except Exception as Argument:
        print("Problem in OnceInMorning")
        Logger("LogScheduleError.txt",Argument,"OnceInMorning")
    Logger("LogSchedule.txt",":end :","ScheduleOnceInMorning")
    
def ShutDownComputer():
    Logger("LogSchedule.txt",":Start :","ShutDownComputer")
    try:
        print("ShutDownComputer")
        os.system("shutdown /s /t 1")
    except Exception as Argument:
        print("Problem in ShutDownComputer")
        Logger("LogScheduleError.txt",Argument,"ShutDownComputer")
    Logger("LogSchedule.txt",":end :","ShutDownComputer")
    
def RestartComputer():
    Logger("LogSchedule.txt",":Start :","RestartComputer")
    try:
        print("RestartComputer")
        os.system("shutdown -t 0 -r -f")
    except Exception as Argument:
        print("Problem in RestartComputer")
        Logger("LogScheduleError.txt",Argument,"RestartComputer")
    Logger("LogSchedule.txt",":end :","RestartComputer")

# Task scheduling
schedule.every().day.at("06:30").do(ScheduleOnceInMorning)
schedule.every().day.at("09:14").do(ScheduleCyclicRun)
schedule.every().day.at("09:55").do(ScheduleCyclicRun)
schedule.every().day.at("11:30").do(ScheduleCyclicRun)
schedule.every().day.at("12:15").do(ScheduleCyclicRun)
schedule.every().day.at("13:15").do(ScheduleCyclicRun)
schedule.every().day.at("14:30").do(ScheduleCyclicRun)
schedule.every().day.at("15:15").do(ScheduleCyclicRun)
schedule.every().day.at("15:45").do(ScheduleOnceInMorning)
schedule.every().day.at("17:55").do(RestartComputer)

#Holidays
#Later on to use pi on sat sun, Delete these shutdowncomputer, and schedule cyclicrun each daywise: Mon to friday
# Shutting down on Saturday and Sunday
schedule.every().saturday.at("09:05").do(ShutDownComputer)
schedule.every().saturday.at("09:07").do(ShutDownComputer)
schedule.every().sunday.at("09:05").do(ShutDownComputer)
schedule.every().sunday.at("09:07").do(ShutDownComputer)


# Loop so that the scheduling task
# keeps on running all time.
while True:
  
    # Checks whether a scheduled task 
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
