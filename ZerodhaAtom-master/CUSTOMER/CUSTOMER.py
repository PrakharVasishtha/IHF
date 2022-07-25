import mysql.connector


#SQL Pre Initiation
mydb = mysql.connector.connect(
  host="localhost",
  user="user1",
  password="fd74F&fs",
  database="CUSTOMER"
)

mycursor = mydb.cursor()



def CustLogin(CID):
    sql = "SELECT ClientID,Password,PIN FROM CustBroker WHERE CustID=%s"
    val = (CID,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult


def NumberOfCustomer():
    sql = "SELECT Count(CustID) FROM CustGen"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for y in myresult:
        return y[0]
    
    
def CustomerFundFactor(id3,StrID):
    if StrID==1:
        sql = "SELECT Str1Factor FROM CustFundAllocation WHERE CustID = %s"
    elif StrID==2:
        sql = "SELECT Str2Factor FROM CustFundAllocation WHERE CustID = %s"
    else:
        print("No Strategy Factor")
        return 0
    val = (id3,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult[0][0]
    
def CustStockQty(CID,StkID):
    #Finding TotalQuantity
    sql = "SELECT TotalQuantity FROM CustHoldings WHERE CustID = %s AND StockID = %s"
    val = (CID,StkID)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult[0][0]
    
def CustBuyQtyFin(StrID,StkID,Qty3,cid3,ISL,LTP):
    print("LTP :", LTP)
    
    #Finding TotalFund
    sql = "SELECT TotalFund FROM CustFund WHERE CustID = %s"
    val = (cid3,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    TotalFund=myresult[0][0]
    print("TotalFund :", TotalFund)
    
    #Finding StgyfundAllocationPercent
    if StrID == 1:
        sql = "SELECT Str1Per FROM CustFundAllocation WHERE CustID = %s"
    val = (cid3,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    StrPer=myresult[0][0]
    print("Str1Per:",StrPer)
    
    #Calculating Strategy Fund Allocation using total fund and percent
    StrFundAlloc=(TotalFund*StrPer)/100
    print("StrFundAlloc",StrFundAlloc)
    
    #Finding TotalStockQuantity
    sql = "SELECT TotalQuantity FROM CustHoldings WHERE CustID = %s and StockID = %s"
    val = (cid3, StkID)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    TQ=myresult[0][0]
    print("TotalStockQuantity :", TQ)
    
    
    
    #logic
    StkHlding=TQ*LTP
    print("StkHlding",StkHlding)
    
    CrTradeValue=Qty3*LTP
    
    FtrHlding=StkHlding+CrTradeValue
    print("FtrHlding", FtrHlding)
    
    CustIndStkLmt=(StrFundAlloc*ISL)/100
    print("CustIndStkLmt", CustIndStkLmt)
    
    if FtrHlding > CustIndStkLmt:
        return 0
    elif CrTradeValue < 2000:
        return 0
    else:
        return Qty3

# (StrID,StkID,Qty3,cid3,ISL,LTP)
#print(CustBuyQtyFin(1,15,100,1,90,185))
    
#print(CustStockQty(2,56))
#print(CustomerFundFactor(2,1))