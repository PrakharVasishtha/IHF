import mysql.connector



def TrTraderStrategy():
    print("------------------------")    
    print("TraderStrategy Table Update Started")
    print("------------------------")
    #SQL Pre Initiation
    mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="fd74F&fs",
     database="MODULES"
    )
    mycursor = mydb.cursor()
    QT=['']*250
    for id in range(1,251):
        sql = "SELECT QTTOBY FROM SSWS WHERE StockID= %s"
        val = (id, )
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        QT[id-1]=myresult[0][0]
    #print(QT)
    
    #SQL Pre Initiation
    mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="fd74F&fs",
     database="TRADER"
    )
    mycursor = mydb.cursor()
    for id in range(1,251):
        TOBUY=QT[id-1]
        #print("ToBuy :",TOBUY)
        sql = "UPDATE TraderStrategy1 SET ToBuy = %s WHERE StockID = %s"
        val = (TOBUY, id)
        x=mycursor.execute(sql, val)
        mydb.commit()
        sql = "UPDATE TraderStrategy2 SET ToBuy = %s WHERE StockID = %s"
        val = (TOBUY, id)
        x=mycursor.execute(sql, val)
        mydb.commit()
        #print("StockID :",id,"-",mycursor.rowcount, "record inserted")
    
    print("------------------------")    
    print("TraderStrategy Table Updated")
    print("------------------------")
        
#TrTraderStrategy()
