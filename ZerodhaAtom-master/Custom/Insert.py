import mysql.connector

# initializing StockID Array
StockID=[i for i in range(1,251)]

# Defining BuyerStgy1
def InsertIntoTable():
    #SQL Pre Initiation
    mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="fd74F&fs",
     database="CUSTOMER"
    )
    mycursor = mydb.cursor()
    
    for Ind in range(3,251):
        print(Ind)
        sql = "INSERT INTO CustHoldings (CustID,StockID, QuantityToday, QuantityOld, TotalQuantity) VALUES(2,%s, 0, 0, 0)"
        val = (Ind,)
        x=mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted")
        
        
    

InsertIntoTable()
