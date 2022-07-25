import mysql.connector



def CleanTraderStrategy():
    print("------------------------")    
    print("TraderStrategy Table Cleaning Started")
    print("------------------------") 
    
    #SQL Pre Initiation
    mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="fd74F&fs",
     database="TRADER"
    )
    mycursor = mydb.cursor()
    for id in range(1,251):
        sql = "UPDATE TraderStrategy1 SET ToBuy = 0,AlrdyBght = 0,RunCountBuy=0,LBP=0,ToSell=0,AlrdySold=0,RunCountSell=0,LSP=0 WHERE StockID = %s"
        val = (id,)
        x=mycursor.execute(sql, val)
        mydb.commit()
        sql = "UPDATE TraderStrategy2 SET ToBuy = 0,AlrdyBght = 0,RunCountBuy=0,LBP=0,ToSell=0,AlrdySold=0,RunCountSell=0,LSP=0 WHERE StockID = %s"
        val = (id,)
        x=mycursor.execute(sql, val)
        mydb.commit()
        #print("StockID :",id,"-",mycursor.rowcount, "record inserted Cleaned")
        
    print("------------------------")    
    print("TraderStrategy Cleaned")
    print("------------------------")    

#CleanTraderStrategy()

