import investpy
import mysql.connector
from datetime import timedelta, date



def SrcIndicesPriceHist():
    print("--------------------------------------")
    print("--------SrcIndicesPriceHist-----------")
    #SQL Pre Initiation
    mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="fd74F&fs",
    database="SOURCES"
    )
    mycursor = mydb.cursor()

    #6 Months Strdt = tdy-179
    y=date.today()-timedelta(days=180)
    StrDate=str(y.day)+"/"+str(y.month)+"/"+str(y.year)
    #print(StrDate)
    z=date.today()-timedelta(days=178)
    EndDate=str(z.day)+"/"+str(z.month)+"/"+str(z.year)
    #print(EndDate)

    try:
        BSE_hist = investpy.get_index_historical_data(index='BSE Sensex', country='india', from_date=StrDate, to_date=EndDate)
        a=int(BSE_hist['Close'][0])
        #print(a)

        # Updating Table SQL
        sql = "UPDATE IndicesPriceHist SET Price1 = %s WHERE IndiceID = 1"
        val = (a, )
        mycursor.execute(sql, val)
        mydb.commit()
        #print(mycursor.rowcount, "record(s) affected")
    except:
        print("Exception in a BSE_hist")

    try:
        Nifty_hist = investpy.get_index_historical_data(index='Nifty 50', country='india', from_date=StrDate, to_date=EndDate)
        b=int(Nifty_hist['Close'][0])
        #print(b)
        # Updating Table SQL
        sql = "UPDATE IndicesPriceHist SET Price1 = %s WHERE IndiceID = 2"
        val = (b, )
        mycursor.execute(sql, val)
        mydb.commit()
        #print(mycursor.rowcount, "record(s) affected")
    except:
        print("Exception")

    
    try:
        RUT_hist = investpy.get_index_historical_data(index='SmallCap 2000', country='united states', from_date=StrDate, to_date=EndDate)
        c=int(RUT_hist['Close'][0])
        #print(c)
        # Updating Table SQL
        sql = "UPDATE IndicesPriceHist SET Price1 = %s WHERE IndiceID = 3"
        val = (c, )
        mycursor.execute(sql, val)
        mydb.commit()
        #print(mycursor.rowcount, "record(s) affected")

    except:
        print("Exception")
 
    
    try:
        OEX_hist = investpy.get_index_historical_data(index='S&P 100', country='united states', from_date=StrDate, to_date=EndDate)
        d=int(OEX_hist['Close'][0])
        #print(d)
        # Updating Table SQL
        sql = "UPDATE IndicesPriceHist SET Price1 = %s WHERE IndiceID = 4"
        val = (d, )
        mycursor.execute(sql, val)
        mydb.commit()
        #print(mycursor.rowcount, "record(s) affected")
    except:
        print("Exception")

    
    try:
        DJI_hist = investpy.get_index_historical_data(index='DOW 30', country='united states', from_date=StrDate, to_date=EndDate)
        e=int(DJI_hist['Close'][0])
        #print(e)
        # Updating Table SQL
        sql = "UPDATE IndicesPriceHist SET Price1 = %s WHERE IndiceID = 5"
        val = (e, )
        mycursor.execute(sql, val)
        mydb.commit()
        #print(mycursor.rowcount, "record(s) affected")

    except:
        print("Exception")
    
    
    try:
        Nikky_hist = investpy.get_index_historical_data(index='Nikkei 225', country='japan', from_date=StrDate, to_date=EndDate)
        f=int(Nikky_hist['Close'][0])
        #print(f)
    
        # Updating Table SQL
        sql = "UPDATE IndicesPriceHist SET Price1 = %s WHERE IndiceID = 6"
        val = (f, )
        mycursor.execute(sql, val)
        mydb.commit()
        #print(mycursor.rowcount, "record(s) affected")
    except:
        print("exception in f")



    print("-----------------------------------------------------")






