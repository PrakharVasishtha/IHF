import investpy
import mysql.connector
from datetime import timedelta, date




def SrcIndicesPriceHigh():
    print("--------------------------------------")
    print("--------SrcIndicesPriceHigh-----------")

    # Dates
    #Highest1 tdy -30 to t
    y=date.today()-timedelta(days=30)
    StrDate1=str(y.day)+"/"+str(y.month)+"/"+str(y.year)
    z=date.today()-timedelta(days=2)
    EndDate1=str(z.day)+"/"+str(z.month)+"/"+str(z.year)

    #Highest2 tdy -5 to t
    y=date.today()-timedelta(days=5)
    StrDate2=str(y.day)+"/"+str(y.month)+"/"+str(y.year)
    z=date.today()-timedelta(days=2)
    EndDate2=str(z.day)+"/"+str(z.month)+"/"+str(z.year)

    #Highest3 tdy -15 to t-7
    y=date.today()-timedelta(days=15)
    StrDate3=str(y.day)+"/"+str(y.month)+"/"+str(y.year)
    z=date.today()-timedelta(days=7)
    EndDate3=str(z.day)+"/"+str(z.month)+"/"+str(z.year)


    #Highest1  tdy -30 to t
    def Highest1(Indice1, Country1):
        StrDate='18/12/2021'
        EndDate='16/1/2022'


        data = investpy.get_index_historical_data(index=Indice1, country=Country1, from_date=StrDate1, to_date=EndDate1)
        ln=len(data)
        high=1
        for i in range(0,ln):
            new=data['High'][i]
            if new > high:
                high = new
        high=int(high)
        #print(high)
        return high

    #Highest2  enddate= tdy -5 to t
    def Highest2(Indice1, Country1):
        StrDate2='12/1/2022'
        EndDate2='16/1/2022'


        data = investpy.get_index_historical_data(index=Indice1, country=Country1, from_date=StrDate2, to_date=EndDate2)
        #print(data)
        ln=len(data)
        high=1
        for i in range(0,ln):
            new=data['High'][i]
            if new > high:
                high = new
        high=int(high)
        #print(high)
        return high



    #Highest3  enddate= tdy -15 to t-7
    def Highest3(Indice1, Country1):
        StrDate2='2/1/2022'
        EndDate2='10/1/2022'


        data = investpy.get_index_historical_data(index=Indice1, country=Country1, from_date=StrDate3, to_date=EndDate3)
        #print(data)
        ln=len(data)
        high=1
        for i in range(0,ln):
            new=data['High'][i]
            if new > high:
                high = new
        high=int(high)
        #print(high)
        return high


    a1p1=Highest1('BSE Sensex', 'india')
    a2p1=Highest1('Nifty 50', 'india')
    a3p1=Highest1('SmallCap 2000', 'united states')
    a4p1=Highest1('S&P 100', 'united states')
    a5p1=Highest1('DOW 30', 'united states')
    a6p1=Highest1('Nikkei 225', 'japan')

    a1p2=Highest2('BSE Sensex', 'india')
    a2p2=Highest2('Nifty 50', 'india')
    a3p2=Highest2('SmallCap 2000', 'united states')
    a4p2=Highest2('S&P 100', 'united states')
    a5p2=Highest2('DOW 30', 'united states')
    
    a1p3=Highest3('BSE Sensex', 'india')
    a2p3=Highest3('Nifty 50', 'india')
    a3p3=Highest3('SmallCap 2000', 'united states')
    a4p3=Highest3('S&P 100', 'united states')
    a5p3=Highest3('DOW 30', 'united states')

    #SQL Pre Initiation
    mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="fd74F&fs",
    database="SOURCES"
    )
    mycursor = mydb.cursor()

    # Updating Table SQL
    sql = "UPDATE IndicesPriceHigh SET Price1 = %s, Price2 = %s, Price3 = %s WHERE IndiceID = 1"
    val = (a1p1, a1p2, a1p3, )
    mycursor.execute(sql, val)
    mydb.commit()
    #print(mycursor.rowcount, "record(s) affected")

    sql = "UPDATE IndicesPriceHigh SET Price1 = %s, Price2 = %s, Price3 = %s WHERE IndiceID = 2"
    val = (a2p1, a2p2, a2p3, )
    mycursor.execute(sql, val)
    mydb.commit()
    #print(mycursor.rowcount, "record(s) affected")
    
    sql = "UPDATE IndicesPriceHigh SET Price1 = %s, Price2 = %s, Price3 = %s WHERE IndiceID = 3"
    val = (a3p1, a3p2, a3p3, )
    mycursor.execute(sql, val)
    mydb.commit()
    #print(mycursor.rowcount, "record(s) affected")

    sql = "UPDATE IndicesPriceHigh SET Price1 = %s, Price2 = %s, Price3 = %s WHERE IndiceID = 4"
    val = (a4p1, a4p2, a4p3, )
    mycursor.execute(sql, val)
    mydb.commit()
    #print(mycursor.rowcount, "record(s) affected")

    sql = "UPDATE IndicesPriceHigh SET Price1 = %s, Price2 = %s, Price3 = %s WHERE IndiceID = 5"
    val = (a5p1, a5p2, a5p3, )
    mycursor.execute(sql, val)
    mydb.commit()
    #print(mycursor.rowcount, "record(s) affected")

    sql = "UPDATE IndicesPriceHigh SET Price1 = %s WHERE IndiceID = 6"
    val = (a6p1, )
    mycursor.execute(sql, val)
    mydb.commit()
    #print(mycursor.rowcount, "record(s) affected")

    print("-----------------------------------------------------")


#SrcIndicesPriceHigh()