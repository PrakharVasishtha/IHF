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
     database="SOURCES"
    )
    mycursor = mydb.cursor()
    
    for Ind in range(1,251):
        print(Ind)
        sql = "INSERT INTO StockFin (StockID, RevYr0, RevYr1, RevYr2, RevQt0, RevQt1, RevQt2, IncmYr0, IncmYr1, IncmYr2, IncmQt0, IncmQt1, IncmQt2, MktShrChng, PE, PB, TtlEqty, OvrUndrBght) VALUES(%s, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)"
        val = (Ind,)
        x=mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted")
        
        
    

InsertIntoTable()

