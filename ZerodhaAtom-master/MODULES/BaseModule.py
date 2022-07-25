import mysql.connector




mydb = mysql.connector.connect(
  host="localhost",
  user="user1",
  password="fd74F&fs",
  database="MODULES"
)
mycursor = mydb.cursor()

def FindOverall(StkID):
    sql=("SELECT Overall from StockIndicators WHERE StockID = %s")
    val=(StkID,)
    x=mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    print(myresult[0][0])
    return myresult[0][0]
    
#FindOverall(2)