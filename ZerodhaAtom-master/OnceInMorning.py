from SrcStocksLtp import *
from SrcStocksRecommendations import *
from SrcStockFinancials import *
from MdlFullStockIndicators import *
from SrcIndicesPriceHigh import *
from SrcIndicesPriceHist import *
from COMMON.Common import *




def OnceInMorning():
    print("---------------------------------------")
    print("---------Starting OnceInMorning--------")
    Logger("LogOnceInMorning.txt",":Start :","OnceInMorning")


    
    # SrcStocksLTP
    try:
        SrcStocksLtp()
    except Exception as Argument:
        print("Problem in SrcStocksLTP")
        Logger("LogOnceInMorningError.txt",Argument,"SrcStocksLtp")
    
    

    # SrcIndicesPriceHigh
    try:
        SrcIndicesPriceHigh()
    except Exception as Argument:
        print("Problem in SrcIndicesPriceHigh")
        Logger("LogOnceInMorningError.txt",Argument,"SrcIndicesPriceHigh")
    
    #SrcIndicesPriceHist
    try:
        SrcIndicesPriceHist()
    except Exception as Argument:
        print("Problem in SrcIndicesPriceHist")
        Logger("LogOnceInMorningError.txt",Argument,"SrcIndicesPriceHist")

    # SrcStocksRecommendations
    try:
        SrcStocksRecommendations()
    except Exception as Argument:
        print("Problem in SrcStocksRecommendations")
        Logger("LogOnceInMorningError.txt",Argument,"SrcStocksRecommendations")

    # SrcStockFin
    try:
        SrcStockFin()
    except Exception as Argument:
        print("Problem in SrcStockFin")
        Logger("LogOnceInMorningError.txt",Argument,"SrcStockFin")
   
    # MdlFullStockIndicators
    try:
        MdlFullStockIndicators()
    except Exception as Argument:
        print("Problem in MdlFullStockIndicators")
        Logger("LogOnceInMorningError.txt",Argument,"MdlFullStockIndicators")
    
    print("-----------------------------------")
    
    Logger("LogOnceInMorning.txt",":Finished :","OnceInMorning")
#OnceInMorning()