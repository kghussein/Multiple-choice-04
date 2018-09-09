import time, datetime
import re
import os, sys
from datetime import timedelta

#Initializing the Parameters
sDirV=''
dir_name=''
numberofMMEs=[]
commands=[]
commands3=[]
mmelist=[]
MMEname=[]
chooseMME=[]
listM=[]
#credentials

username =input('Please Enter your username:')
password = input('Please Enter Password:')

#MME IP Addresses, name of the node, and number of ports
#my_dictionary ={"MME05": ["155.165.252.60","WTC1ERCMME05","48"],
#"MME06": ["155.165.252.61","WTC3ERCMME06","48"]}



MME05=["155.165.252.60","WTC1ERCMME05","48"]
MME06=["155.165.252.61","WTC3ERCMME06","48"]
MME09= ["155.165.252.144","WTC3ERCMME09","48"]   
MME10= ["155.165.252.146","WTC1ERCMME10","48"]
MME15= ["155.165.163.34","WTC3ERCMME15","48"]
MME16= ["155.165.163.33","WTC3ERCMME16","48"]        
MME17= ["155.165.163.225","WTC1ERCMME17","48"]
MME18= ["107.239.116.56","WTCMME18LTZ","48"]
MME19= ["107.239.116.58","WTCMME19LTZ","48"]        
MME20= ["107.239.116.60","WTCMME20LTZ","48"]
Vmme50=["107.250.254.99","zrdm6bmmex50","8"]
Vmme51=["107.250.254.101","zrdm6bmmex51","8"]
Vmme52=["107.250.254.74","zrdm6bmmex52","8"]
Vmme53=["107.250.254.105","zrdm6bmmex53","44"]
Vmme54=["107.250.254.107","zrdm6bmmex54","14"]      
Vmme55=["107.112.170.208","zrdm6bmmex55","8"]
Vmme56=["107.112.170.217","zrdm6bmmex56","8"]
Vmme57=["107.112.170.226","zrdm6bmmex57","8"]
Vmme58=["107.112.170.235","zrdm6bmmex58","8"]
Vmme59=["107.112.170.244","zrdm6bmmex59","44"]
Vmme60=["107.112.170.253","zrdm6bmmex60","8"]


my_dictionary ={"MME05": MME05, "MME06": MME06, "MME09": MME09,"MME10": MME10 ,"MME15": MME15, "MME16": MME16,"MME17": MME17
                ,"MME18": MME18,"MME19": MME19,"MME20": MME20,
                "VMME50": Vmme50,"VMME51": Vmme51,"VMME52": Vmme52,"VMME53": Vmme53,"VMME54": Vmme54,"VMME55": Vmme55,"VMME56": Vmme56,
                "VMME57": Vmme57,"VMME58": Vmme58,"VMME59": Vmme59,"VMME60": Vmme60}


# To get the time at the time of the run
Directory_name=str(datetime.datetime.now().strftime('%Y-%m-%d'))
time_Now=datetime.datetime.now().strftime('%Y-%m-%d %H:')
str_time_Now=str(time_Now)
# To get the time befor 24 hour
last_24hour_date_time = datetime.datetime.now()-timedelta(hours =24)
last_24_hour_date_time=last_24hour_date_time.strftime('%Y-%m-%d')



# Importing the board number and Directory
def importP(sDir):
    
    global sDirV
    global dir_name
    global commands
    global commands3
    global mmelist
    global MMEname
    global numberofMMEs
    
    global MME05
    global MME06
    global MME09
    global MME10
    global MME15
    global MME16
    global MME17
    global MME18
    global MME19
    global MME20
    global Vmme50
    global Vmme51
    global Vmme52
    global Vmme53
    global Vmme54
    global Vmme55
    global Vmme56
    global Vmme57
    global Vmme58
    global Vmme59
    global Vmme60
    global chooseMME

    #To Initalized the Directory
    sDirV=sDir
    
    dir_name=os.getcwd()
    
    #To Initalized the range that you want to collect the ISP trace 
    xsearch= r'"/'+str(last_24_hour_date_time)+'/,/'+str_time_Now+'/p"'
    commandName='sed -n -e '+xsearch+' /Core/log/isp.log'
    
    # Commands list that it will be executed
    commands=['gsh get_ne','gsh get_lm','listSCs','gsh list_config_activated','hw_status','gsh list_alarms',commandName]
    #commands=['gsh get_ne']
    commands3= ['gsh get_ne','hw_status','listSCs',commandName,'gsh list_config_activated']
    #chooseMME = input('Please Enter which MME, or choose ALL:')
    # mmeName

    while mmelist==[]:
        chooseMME = input('Please Enter which MME\'s you want nodeRX to run on separated by a comma, or choose ALL:')
        if chooseMME.upper()=='ALL':
            mmelist=[MME05,MME06,MME09,MME10,MME15,MME16,MME17,MME18,MME19,MME20,Vmme50,Vmme51,Vmme52,Vmme53,Vmme54,Vmme55,Vmme56,Vmme57,Vmme58,Vmme59,Vmme60]
            break
        
    #Choosing which MME to run the script in
        
        elif chooseMME!='ALL':
            print(chooseMME.upper())
            #print(my_dictionary["MME05"])
            numberofMMEs=chooseMME.split(',')
            print(numberofMMEs)
            for MMEItem in numberofMMEs:
                print(MMEItem)
                if MMEItem.strip().upper() in my_dictionary:
                    mmelist.append(my_dictionary[MMEItem.strip().upper()])

                else:
                    print(MMEItem+" is not a valid entry"+"\n")
                    
                
            #mmelist=my_dictionary[chooseMME]
            print(mmelist)
            break
    
        




         
