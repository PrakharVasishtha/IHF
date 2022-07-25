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
     database="MODULES"
    )
    mycursor = mydb.cursor()
    
    for Ind in range(1,251):
        print(Ind)
        sql = "UPDATE StockIndicators SET CustomRating = 7 WHERE StockID = %s" 
        val = (Ind,)
        x=mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted")
        
        
    

InsertIntoTable()


