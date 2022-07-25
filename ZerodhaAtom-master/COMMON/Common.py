from datetime import datetime


def ConvertToInt(x):
    x1=x.replace(",","")
    x2=int(float(x1))
    return(x2)

def Logger(file,StringText="OK",FunctionName="In Function"):
    s = FunctionName+str(StringText)+" at time :"+str(datetime.now()) 
    f = open(file, "a")
    f.write(s)
    f.write("\n")
    f.close()


#Logger("Str","Test.txt")