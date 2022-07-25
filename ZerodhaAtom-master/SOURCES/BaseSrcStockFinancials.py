import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium import *
from SOURCES.SOURCE import *


def Yearly(urlyearly):
    url2=urlyearly
    print(url2)
    #Opening Financials Page
    driver = webdriver.Chrome()
    driver.get(url2)
    driver.set_window_size(1224, 568)
    time.sleep(14)
    
    #Yearly
    #Finding Revenue
    #Rvn0
    try:
        Rvn0=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/div[11]/div[1]/div[2]/span[1]/span[1]")
    except:
        try:
            Rvn0=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/div[10]/div[1]/div[2]/span[1]/span[1]")
        except:
            Rvn0=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div[1]/div[10]/div[1]/div[2]/span[1]/span[1]")
    print("Rvn0")
    Rvn0A=ConvertToInt(Rvn0.text)
    print(Rvn0A)
     
     
    #Rvn1
    try:
        Rvn1=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/div[10]/div[1]/div[2]/span[1]/span[1]")
    except:
        Rvn1=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div[1]/div[9]/div[1]/div[2]/span[1]/span[1]")
    print("Rvn1")
    Rvn1A=ConvertToInt(Rvn1.text)
    print(Rvn1A)
    
    
    #Rvn2
    try:
        Rvn2=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/div[9]/div[1]/div[2]/span[1]/span[1]")
            
    except:
        Rvn2=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div[1]/div[8]/div[1]/div[2]/span[1]/span[1]")
    print("Rvn2")
    Rvn2A=ConvertToInt(Rvn2.text)
    print(Rvn2A)
        
    #Finding Income
    #inc0
    try:
        Inc0=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/div[11]/div[1]/div[14]/span[1]/span[1]").text
    except:
        try:
            Inc0=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/div[10]/div[1]/div[14]/span[1]/span[1]").text
        except:
            Inc0=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div[1]/div[10]/div[1]/div[14]/span[1]/span[1]").text    
    print("Inc0")
    Inc0A=ConvertToInt(Inc0)
    print(Inc0A)
    
    #inc1
    try:
        Inc1=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/div[10]/div[1]/div[14]/span[1]/span[1]").text
    except:
        Inc1=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div[1]/div[9]/div[1]/div[14]/span[1]/span[1]").text
    print("Inc1")
    Inc1A=ConvertToInt(Inc1)
    print(Inc1A)
    
    #inc2
    try:
        Inc2=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/div[9]/div[1]/div[14]/span[1]/span[1]").text
    except:
        Inc2=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div[1]/div[8]/div[1]/div[14]/span[1]/span[1]").text 
    print("Inc2")
    Inc2A=ConvertToInt(Inc2)
    print(Inc2A)
        
    #MarketShare Change              
    try:
        x=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/p[1]").text     
    except:
        print("Data not available")
        x="Over the last 5 years, market share increased from 2.87% to 2.87%"
        
    print(x)
    MSC=StringDifference(x)
    print(MSC)
        
    #Overbaught=0 underbaught=1
    x=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[5]/section[1]/div[1]/div[4]/div[1]/p[1]").text     
    OB=x.find("ood")
    if OB!=1:
        OB=0
    print("OUB 1: underbaught ,0: overbaught : "+str(OB))
    driver.quit()
    time.sleep(1)
    return [Rvn0A,Rvn1A,Rvn2A,Inc0A,Inc1A,Inc2A,MSC,OB]
    

def Quaterly(urlquaterly):
    url3=urlquaterly
    #Opening Financials Page
    driver = webdriver.Chrome()
    driver.get(url3)
    driver.set_window_size(1224, 568)
    time.sleep(14)
    
    #Finding Revenue
    #revQ0
    try:                                     
        RvnQ0=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div[1]/div[11]/div[1]/div[2]/span[1]/span[1]").text
    except:
        try:
            RvnQ0=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div[1]/div[10]/div[1]/div[2]/span[1]/span[1]").text
        except:
            RvnQ0=driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div[1]/div[11]/div[1]/div[2]/span[1]/span[1]").text     
    print("RvnQ0")
    RvnQ0A=ConvertToInt(RvnQ0)
    print(RvnQ0A)
    
    RvnQ1=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div[1]/div[10]/div[1]/div[2]/span[1]/span[1]").text
    print("RvnQ1")
    RvnQ1A=ConvertToInt(RvnQ1)
    print(RvnQ1A)
    RvnQ2=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div[1]/div[9]/div[1]/div[2]/span[1]/span[1]").text
    print("RvnQ2")
    RvnQ2A=ConvertToInt(RvnQ2)
    print(RvnQ2A)
        
    #Finding Income
    
    try:
        IncQ0=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div[1]/div[11]/div[1]/div[10]/span[1]/span[1]").text
    except:
        IncQ0=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div[1]/div[10]/div[1]/div[10]/span[1]/span[1]").text
    print("IncQ0")
    IncQ0A=ConvertToInt(IncQ0)
    print(IncQ0A)
    IncQ1=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div[1]/div[10]/div[1]/div[10]/span[1]/span[1]").text
    print("IncQ1")
    IncQ1A=ConvertToInt(IncQ1)
    print(IncQ1A)
    IncQ2=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div[1]/div[9]/div[1]/div[10]/span[1]/span[1]").text
    print("IncQ2")
    IncQ2A=ConvertToInt(IncQ2)
    print(IncQ2A)
        
    driver.quit()
    time.sleep(1)
    return [RvnQ0A,RvnQ1A,RvnQ2A,IncQ0A,IncQ1A,IncQ2A]

    
def NADiffun(url4a):
    url4=url4a
    #Net Asset : TotalEquity Difference oyr -1yr : Eqt= Asset - Liability
    driver = webdriver.Chrome()
    driver.get(url4)
    print(url4)
    driver.set_window_size(1224, 568)
    time.sleep(12)
        
    try:
        NA0=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/div[11]/div[1]/div[29]/span[1]/span[1]").text
    except:
        NA0="287"
    print("NA0")
    NA0A=ConvertToInt(NA0)
    print(NA0A)
    try:
        NA1=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/div[10]/div[1]/div[29]/span[1]/span[1]").text
    except:
        NA1="287"
    print("NA1")
    NA1A=ConvertToInt(NA1)
    print(NA1A)
    NADif=NA0A-NA1A
    print("NAdif :"+str(NADif))
    driver.quit()
    time.sleep(1)
    if NADif>0:
        NetAssetChange=((NADif/NA1A)*10)
    else:
        NetAssetChange=0
    return NetAssetChange
    
    
    
    
  
    
    
    



def StringDifference(x):
    # getting first number and converting to int
    i1=x.index("from")
    p1=int(x[i1+5])
    p2=x[i1+6]

    #checking for right digit
    if p2==".":
        p2=0
    elif p2=="%":
        p2=0
    p2=int(p2)
    if p2!=0:
        n1=(p1*10)+p2
    else:
        n1=p1
    

    #second number
    i2=x.index("to")
    p3=int(x[i2+3])
    p4=x[i2+4]

    #checking for right digit
    if p4==".":
        p4=0
    elif p4=="%":
        p4=0
    p4=int(p4)
    if p4!=0:
        n2=(p3*10)+p4
    else:
        n2=p3
    

    #difference
    dif=n2-n1
    print("MarketShareChange")
    return(dif)
