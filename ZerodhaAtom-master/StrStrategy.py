import mysql.connector


def StrStrategy():
    print("------------------------")    
    print("StrStrategy Started")
    print("------------------------") 

    for StrID in range(1,3):
        BuyTraderFlag=0
        SellTraderFlag=0
    
        # Select from SM
        #SQL Sources
    
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="fd74F&fs",
         database="MODULES"
        )
        mycursor = mydb.cursor()
        sql = "SELECT Value1 from SM WHERE MdlID = 1"
        x=mycursor.execute(sql,)
        myresult = mycursor.fetchall()
        SMWL=myresult[0][0]
        print("SMWL :", SMWL)
        sql = "SELECT Value1 from SM WHERE MdlID = 2"
        x=mycursor.execute(sql,)
        myresult = mycursor.fetchall()
        SMWS=myresult[0][0]
        print("SMWS :", SMWS)
    
    
        # Select from SetStrategy
        #SQL Sources
    
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="fd74F&fs",
         database="STRATEGIES"
        )
        mycursor = mydb.cursor()
        sql = "SELECT SMWLBUY,SMWLSELL,SMWSBUY,SMWSSELL from SetStrategy WHERE StrategyID = %s"
        val = (StrID,)
        x=mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        SMWLBUY=myresult[0][0]
        SMWLSELL=myresult[0][1]
        SMWSBUY=myresult[0][2]
        SMWSSELL=myresult[0][3]
        #print(SMWLBUY,SMWLSELL,SMWSBUY,SMWSSELL)
        if SMWL > SMWLBUY and SMWS > SMWSBUY:
            BuyTraderFlag=1
            print("BuyTraderFlag : 1","For Str",StrID)
        if SMWL < SMWLSELL and SMWS < SMWSSELL:
            SellTraderFlag=1
            print("SellTraderFlag : 1","For Str",StrID)
    
        # Error Check for exceptional conditions
        if BuyTraderFlag == 1 and SellTraderFlag == 1:
            break
    
        #SQL Pre Initiation
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="fd74F&fs",
        database="STRATEGIES"
        )
        mycursor = mydb.cursor()

        # Updating Table SQL
        sql = "UPDATE Strategy SET BuyTradeFlag = %s,SellTradeFlag = %s WHERE StrategyID = %s"
        val = (BuyTraderFlag,SellTraderFlag,StrID)
        mycursor.execute(sql, val)
        mydb.commit()
        #print(mycursor.rowcount, "record(s) affected")
    
    print("------------------------") 

#StrStrategy()