import mysql.connector
from CUSTOMER.CUSTOMER import *

def CustFundAlocToStr():
    print("--------------------------------------")
    print("------CustFundAllocation Started------")
    UnitFund=100000
    mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="fd74F&fs",
     database="CUSTOMER"
    )
    mycursor = mydb.cursor()
    CustNumber=NumberOfCustomer()
    for CID in range(1,CustNumber+1):
        print("CustomerID:",CID)
        sql = "SELECT TotalFund from CustFund WHERE CustID = %s"
        val = (CID,)
        x=mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        TotalFund=myresult[0][0]
        print(TotalFund)
        sql = "SELECT Str1Per,Str2Per from CustFundAllocation WHERE CustID = %s"
        val = (CID,)
        x=mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        Str1Per=myresult[0][0]
        Str2Per=myresult[0][1]
        print(Str1Per,Str2Per)
        Str1Factor=float((TotalFund*Str1Per)/(UnitFund*100)-.1)
        Str2Factor=(TotalFund*Str2Per)/(UnitFund*100)-.1
        print(Str1Factor,Str2Factor)
        sql = "UPDATE CustFundAllocation SET Str1Factor = %s,Str2Factor = %s WHERE CustID = %s"
        val = (Str1Factor,Str2Factor,CID )
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        
        print("CustFundAllocation Finished")

        

    
       

#CustFundAlocToStr()
