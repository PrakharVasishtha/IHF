from MdlSM import *
from CustFund import *
from CustFundAlocToStr import *
from CustHoldings import *
from TrTraderStrategyClean import *
from TrTraderStrategy import *
from TrBuyer import *
from TrSellTrader import *
from SrcStocksLtp import *
from SrcIndicesLTP import *
from MdlSMWL import *
from MdlSSWS import *
from StrStrategy import *
from COMMON.Common import *





def CyclicRun():
    print("-----------------------------------")
    print("---------Starting CyclicRun--------")
    
    # SrcStocksLTP
    try:
        SrcStocksLtp()
    except Exception as Argument:
        print("Problem in SrcStocksLTP")
        Logger("LogCyclicRunError.txt",Argument,"SrcStocksLtp")
    
    # SrcIndicesLTP
    try:
        SrcIndicesLTP()
    except Exception as Argument:
        print("Problem in SrcIndicesLTP")
        Logger("LogCyclicRunError.txt",Argument,"SrcIndicesLTP")

    # MdlSMWL
    try:
        MdlSMWL()
    except Exception as Argument:
        print("Problem in MdlSMWL")
        Logger("LogCyclicRunError.txt",Argument,"MdlSMWL")

    # MdlSM
    try:
        MdlSM()
    except Exception as Argument:
        print("Problem in MdlSM")
        Logger("LogCyclicRunError.txt",Argument,"MdlSM")

    # MdlSSWL
    try:
        MdlSSWS()
    except Exception as Argument:
        print("Problem in MdlSSWS")
        Logger("LogCyclicRunError.txt",Argument,"MdlSSWS")

    # CustFund
    try:
        CustFund()
    except Exception as Argument:
        print("Problem in CustFund")
        Logger("LogCyclicRunError.txt",Argument,"CustFund")
    
    # CustFundAlocToStr
    try:
        CustFundAlocToStr()
    except Exception as Argument:
        print("Problem in CustFundAlocToStr")
        Logger("LogCyclicRunError.txt",Argument,"CustFundAlocToStr")
 

    # CustHoldings
    try:
        CustHoldings()
    except Exception as Argument:
        print("Problem in CustHoldings")
        Logger("LogCyclicRunError.txt",Argument,"CustHoldings")
 


    # StrStrategy
    try:
        StrStrategy()
    except Exception as Argument:
        print("Problem in StrStrategy")
        Logger("LogCyclicRunError.txt",Argument,"StrStrategy")

    # CleanTraderStrategy
    try:
        CleanTraderStrategy()
    except Exception as Argument:
        print("Problem in CleanTraderStrategy")
        Logger("LogCyclicRunError.txt",Argument,"CleanTraderStrategy")
    
    # TrTraderStrategy
    try:
        TrTraderStrategy()
    except Exception as Argument:
        print("Problem in TrTraderStrategy")
        Logger("LogCyclicRunError.txt",Argument,"TrTraderStrategy")

    # TrBuyer
    try:
        Buyer(1)
    except Exception as Argument:
        print("Problem in Buyer")
        Logger("LogCyclicRunError.txt",Argument,"Buyer")

    # TrBuyer
    try:
        Buyer(2)
    except Exception as Argument:
        print("Problem in Buyer 2")
        Logger("LogCyclicRunError.txt",Argument,"Buyer")

    # TrSellTrader
    try:
        SellTrader()
    except Exception as Argument:
        print("Problem in SellTrader")
        Logger("LogCyclicRunError.txt",Argument,"SellTrader")



    print("-----------------------------------")
    
#CyclicRun()