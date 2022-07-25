import investpy
import mysql.connector

def SrcIndicesLTP():
    print("-----------------------------------")
    print("----------SrcIndicesLTP-----------")
    #BSE
    current= investpy.indices.get_index_recent_data('BSE Sensex', 'india')
    ln=len(current)-1
    bseLTP=int(current['Close'][ln])
    print(bseLTP)

    #Nifty 50
    current= investpy.indices.get_index_recent_data('Nifty 50', 'india')
    ln=len(current)-1
    NiftyLTP=int(current['Close'][ln])
    print(NiftyLTP)

    #RUT
    current= investpy.indices.get_index_recent_data('SmallCap 2000', 'united states')
    ln=len(current)-1
    RUTLTP=int(current['Close'][ln])
    print(RUTLTP)

    #OEX
    current= investpy.indices.get_index_recent_data('S&P 100', 'united states')
    ln=len(current)-1
    OEXLTP=int(current['Close'][ln])
    print(OEXLTP)

    #DJI
    current= investpy.indices.get_index_recent_data('DOW 30', 'united states')
    ln=len(current)-1
    DJILTP=int(current['Close'][ln])
    print(DJILTP)

    #Nikky
    current= investpy.indices.get_index_recent_data('Nikkei 225', 'japan')
    ln=len(current)-1
    NikkyLTP=int(current['Close'][ln])
    print(NikkyLTP)


    #SQL Pre Initiation
    mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="fd74F&fs",
    database="SOURCES"
    )
    mycursor = mydb.cursor()

    # Updating Table SQL
    sql = "UPDATE IndicesLTP SET LTP = %s WHERE IndiceID = 1"
    val = (bseLTP, )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

    # Updating Table SQL
    sql = "UPDATE IndicesLTP SET LTP = %s WHERE IndiceID = 2"
    val = (NiftyLTP, )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

    # Updating Table SQL
    sql = "UPDATE IndicesLTP SET LTP = %s WHERE IndiceID = 3"
    val = (RUTLTP, )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

    # Updating Table SQL
    sql = "UPDATE IndicesLTP SET LTP = %s WHERE IndiceID = 4"
    val = (OEXLTP, )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

    # Updating Table SQL
    sql = "UPDATE IndicesLTP SET LTP = %s WHERE IndiceID = 5"
    val = (DJILTP, )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

    # Updating Table SQL
    sql = "UPDATE IndicesLTP SET LTP = %s WHERE IndiceID = 6"
    val = (NikkyLTP, )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    print("-----------------------------------")

#SrcIndicesLTP()
