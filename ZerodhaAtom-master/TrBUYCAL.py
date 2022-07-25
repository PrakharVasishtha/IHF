from SOURCES.SOURCE import *
from CUSTOMER.CUSTOMER import *
from TRADER.TRADER import *
from ApiBuy import *
import time

def TrBuyCal(StrID,StkID,Stl,ISL,LTP):
    print("Function TrBuyCal Started")
    time.sleep(5)
    Qty1=Stl
    print("Qty1 :", Qty1)
    Wln=WatchListNo(StkID)
    print("Wln :", Wln)
    Sym=FindSymbol(StkID)
    print("Symbol :", Sym)
    
    #finding MBIS & MBID
    Mbis=MBIS(StrID)
    Mbid=MBID(StrID)
    print("Mbis :", Mbis," Mbid :", Mbid)
    
    #Looping CustID
    #1 first finding size of customer table
    Noc=NumberOfCustomer()
    
    #2 Looping through all customers
    for cid3 in range(1,Noc+1):
        print("Customer Id No. :", cid3)
        factor=CustomerFundFactor(cid3,StrID)
        print("Factor :", factor)
        Qty2=int(Qty1/Mbid)
        Qty3=int((Qty2/Mbis)*factor)
        print("Qty3 :", Qty3)
        Qty4=CustBuyQtyFin(StrID,StkID,Qty3,cid3,ISL,LTP)
        Qty5=int(Qty4)
        print("Qty5 :", Qty5)
        if Qty5 != 0:
            x=BuyStock(Sym,Qty5,Wln,cid3)

            
    
#TrBuyCal(1,1,100,5000,100)

