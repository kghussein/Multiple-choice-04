import paramiko
import time, datetime
import re
import os, sys
import hc_lab_logic as lgc
from datetime import timedelta


global mmeName
def open_ssh_conn(ip,username,password,commands,fileLocation,MME,number0fboard):
    mmeName=''
    #global mmeName
    mmeName=MME
    # try command to handle if there is error in connection
    
    try:
        #definning the global and the list parameters
        
        global cmd
        global tNow
        ex=''
        
        #logging into device
        session = paramiko.SSHClient()

        #For testing purpose this will allow accepting un-known host keys
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        #Connect to the device using the username, password and IP
        session.connect(ip, username =username, password = password)
        #start and interactive shell session on the MME
        connection = session.invoke_shell()

        # getting the time before we run the commands
        tNow= datetime.datetime.now().strftime('%Y-%m-%d')
        
        time.sleep(1)
       
        

        
        # A serial list of commands
        
        for cmd in commands:
          
            
            connection.send(cmd+ '\n')
            time.sleep(4)
        # calling the logic function to perform parameter analysis in a real time processing from a command    
         
            lgc.analysis(cmd,connection,tNow,number0fboard)
           
        # Output to file after defining mme_outputFinal for each loop i define a number of output(2,3,4,..) 
        
        mme_output=lgc.mme_outputFinal
        #mme_output=lgc.mme_outputFinal


        #open a file
        mme_output_file = open (fileLocation,'a')

        # Space between the two MME runs
        mme_output_file.write ("\n")
        mme_output_file.write ("\n")
        #First line
        mme_output_file.write ("####   "+lgc.fetchingMmeName+"  ####"+"\n")
        #Second line collecting the overall result of the search
        mme_output_file.write (lgc.Success_result+"\n")
        
        #Third line to start collecting the output of the commands
        mme_output_file.write ("\n")
        mme_output_file.write ("Issues: "+"\n")

        #Output of the command
        for line in mme_output.split("\\r\\n"):
            
            mme_output_file.write (line+"\n")

 
        
    #The error handler if it failed to ssh
    except paramiko.AuthenticationException:
           #open a file
           mme_output_file = open (fileLocation,'a')
           #First line
           mme_output_file.write ("####  "+mmeName+"  ####"+"\n")
           #second line
           mme_output_file.write ("Invalid username or password"+"\n")

           print("Invalid username or password.\n")
           print( "Closing the program")

    except Exception as ex:

           #open a file
           mme_output_file = open (fileLocation,'a')
           #First line
           mme_output_file.write ("####  "+mmeName+"  ####"+"\n")
           #catching the Exception
           mme_output_file.write ("Unable to connect to node, please check if node is reachable and operational."+"\n")
        
           print (ex)


    finally:
        
        # closing the file
        mme_output_file.close()

    
        #Closing the connection
        session.close()


# The below print to show that the program runned successfully
print("Testcase Started ...")





              


        
        


            


        


        
