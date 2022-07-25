import mysql.connector


#SQL Pre Initiation
mydb = mysql.connector.connect(
  host="localhost",
  user="user1",
  password="fd74F&fs",
  database="CUSTOMER"
)

mycursor = mydb.cursor()



def CustLogin(CID):
    xlist=("CustBroker")
    sql = "SELECT ClientID,Password,PIN FROM {table} WHERE CustID=CID".format(xlist)
    val = {CID,}
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for y in myresult:
        print(y)
    return myresult

CustLogin(3)
