import mysql.connector

def MdlFullStockIndicators():
    print("----------------------------------------------")
    print("-------------MdlFullStockIndicators-----------")
    for sid in range(1,251):
        #SQL Pre Initiation
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="fd74F&fs",
        database="SOURCES"
        )
        mycursor = mydb.cursor()

        #Fetching StlToBuy=ToBuy-AlrdyBght #
        StkID=sid
        #print(StkID)
        sql = "SELECT RevYr0, RevYr1, RevQt0, RevQt1, IncmYr0, IncmYr1, IncmQt0, IncmQt1, TtlEqty, OvrUndrBght from StockFin WHERE StockID = %s"
        val = (StkID,)
        x=mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        #print(myresult)
        RevYr0=myresult[0][0]
        RevYr1=myresult[0][1]
        RevQt0=myresult[0][2]
        RevQt1=myresult[0][3]
        IncmYr0=myresult[0][4]
        IncmYr1=myresult[0][5]
        IncmQt0=myresult[0][6]
        IncmQt1=myresult[0][7]
        TtlEqty=myresult[0][8]
        OvrUndrBght=myresult[0][9]
    
        #Rcm1
        sql = "SELECT Rcm1 from StockRecommendations WHERE StockID = %s"
        val = (StkID,)
        x=mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        #print(myresult)
        Rcm1a=myresult[0][0]
        Rcm1=int(Rcm1a/10)
        if Rcm1<1 or Rcm1>10:
            Rcm1=0
    
    
        #Initiating Variables for Zeroer
        ZerQtrProfitChange=1
        ZerQtrRevenueChange=1
        ZerYrProfitChange=1
        ZerYrRevenueChange=1
    
    

        #Incm
         #error condition to avoid division by zero
        if IncmQt1 == 0:
            IncmQt1=1
        QtrProfitChange=int(((IncmQt0-IncmQt1)/IncmQt1)*50)
        if QtrProfitChange>10:
            QtrProfitChange=10
        if (QtrProfitChange+5)<1:
            ZerQtrProfitChange=0
    
        #Revenue
            #error condition to avoid division by zero
        if RevQt1 == 0:
            RevQt1=1
        QtrRevenueChange=int(((RevQt0-RevQt1)/RevQt1)*50)
        if QtrRevenueChange>10:
            QtrRevenueChange=10
        if (QtrRevenueChange+5)<1:
            ZerQtrRevenueChange=0
    
            #error condition to avoid division by zero
        if IncmYr1 == 0:
            IncmYr1=1
        YrProfitChange=int(((IncmYr0-IncmYr1)/IncmYr1)*50)
        if YrProfitChange>10:
            YrProfitChange=10
        if (YrProfitChange+5)<1:
            ZerYrProfitChange=0
    
            #error condition to avoid division by zero
        if RevYr1 == 0:
            RevYr1=1
        YrRevenueChange=int(((RevYr0-RevYr1)/RevYr1)*50)
        if YrRevenueChange>10:
            YrRevenueChange=10
        if (YrRevenueChange+5)<1:
            ZerYrRevenueChange=0
    
        #SQL Pre Initiation for MODULES DBS
        mydb1 = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="fd74F&fs",
        database="MODULES"
        )
        mycursor1 = mydb1.cursor()
    
        sql = "SELECT  CustomRating from StockIndicators WHERE StockID = %s"
        val = (StkID,)
        x=mycursor1.execute(sql, val)
        myresult1 = mycursor1.fetchall()
        CustRtng=myresult1[0][0]
        #print(CustRtng)


        #Zeroer
        Zeroer=Rcm1*ZerQtrProfitChange*ZerQtrRevenueChange*ZerYrProfitChange*ZerYrRevenueChange*CustRtng
        if Zeroer!=0:
            Zeroer=1
    
        #print("Zeroer", Zeroer)
        #print("Rcm1", Rcm1)
        #print("QtrProfitChange", QtrProfitChange)
        #print("QtrRevenueChange :", QtrRevenueChange)
        #print("YrProfitChange :", YrProfitChange)
        #print("YrRevenueChange :", YrRevenueChange)
    
    

        # Overall
        Overall=(Rcm1+QtrProfitChange+QtrRevenueChange+YrProfitChange+YrRevenueChange+CustRtng)*Zeroer
        Overall=int(Overall/5)
        if Overall>10:
            Overall=10
        #print("overall :", Overall)
    
    
        # Updating Table SQL
        sql = "UPDATE StockIndicators SET QtrProfitChange = %s, QtrRevenueChange= %s, YrProfitChange= %s, YrRevenueChange= %s, CustomRating= %s, ExternalRecommendation= %s, Overall = %s WHERE StockID = %s"
        val = (QtrProfitChange,QtrRevenueChange,YrProfitChange,YrRevenueChange,CustRtng,Rcm1,Overall, sid)
        mycursor1.execute(sql, val)
        mydb1.commit()
        #print("StockID :",sid,mycursor1.rowcount, "record(s) affected")
    print("----------------------------------------------")
    
MdlFullStockIndicators()