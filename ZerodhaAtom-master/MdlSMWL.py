import mysql.connector



def MdlSMWL():
    print("-----------------------------------")
    print("----------MdlSMWL-----------")
    Sum = 0
    for Ind in range(1,7):
    
        #SQL Sources
    
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="fd74F&fs",
        database="SOURCES"
        )
        mycursor = mydb.cursor()
        sql = "SELECT LTP from IndicesLTP WHERE IndiceID = %s"
        val = (Ind,)
        x=mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        IndiceLTP=myresult[0][0]
        print("IndiceLTP :", IndiceLTP)
    
        sql = "SELECT Price1 from IndicesPriceHigh WHERE IndiceID = %s"
        val = (Ind,)
        x=mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        HighPrice1=myresult[0][0]
        print("HighPrice1 :", HighPrice1)
    
        #SQL Strategies
    
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="fd74F&fs",
         database="STRATEGIES"
        )
        mycursor = mydb.cursor()
        sql = "SELECT MS1, COND1, L16, L1 from SetSMWL WHERE IndiceID = %s"
        val = (Ind,)
        x=mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        MS1=myresult[0][0]
        COND1=myresult[0][1]
        L16=myresult[0][2]
        L1=myresult[0][3]
        print("MS1 :", MS1)
        print("L16 :", L16)
        print("L1 :", L1)

    


        #f1 =((F3-D3)/D3)*100 =((HighPrice1-IndiceLTP)/IndiceLTP)*100
        F1 = (((HighPrice1-IndiceLTP)/IndiceLTP)*100)
        print("F1 :", F1)

        #if1 : if(f1>Cond1):F1 else: 0
        if F1 > COND1:
            IF1 = F1
        else:
            IF1 = 0
        print("IF1 :", IF1)
    
        #f2 : IF1 * MS1
        F2 = IF1 * MS1
        print("F2 :", F2)
    
        Sum = Sum + F2
        print("Sum ", Sum)
    
        #Updating SQL F1 IF1 F2
        #SQL Pre Initiation
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="fd74F&fs",
        database="MODULES"
        )
        mycursor = mydb.cursor()

        # Updating Table SQL
        sql = "UPDATE SMWL SET F1 = %s, IF1 = %s, F2 = %s WHERE IndiceID = %s"
        val = (F1, IF1, F2, Ind )
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
    
    

    #fs1 = (Sum of all F2)*10 / L1
    print("Final Sum :", Sum)
    FS1 = (Sum * 10)/L1
    print(FS1)
        #if2 : if FS1 > L16: FS1 else: 0
    if FS1 > L16:
        IF2 = FS1
    else:
        IF2 = 0
    IF2 = int(IF2)
    print("IF2 :", IF2)


    #SQL Pre Initiation
    mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="fd74F&fs",
    database="MODULES"
    )
    mycursor = mydb.cursor()

    # Updating Table SQL
    sql = "UPDATE SMWL SET FS1 = %s, IF2 = %s"
    val = (FS1, IF2 )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

    print("-----------------------------------")


#MdlSMWL()