import paramiko
import time
import re
import os, sys



#mmeName=' '
global mmeName

def open_ssh_conn(ip,username,password,commands,fileLocation,MME,number0fboard):
    mmeName=''
    e=''
    #global mmeName
    mmeName=MME
    # try command to handle if there is error
    
    try:
       
        #logging into device
        session = paramiko.SSHClient()

        #For testing purpose this will allow accepting un-known host keys
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        #connect to the device using the username, password and IP
        session.connect(ip, username =username, password = password)
        #start and interactive shell session on the MME
        connection = session.invoke_shell()

        #Setting the terminal length for entire output
        connection.send("\n")
        time.sleep(1)

        
        # A serial list of commands
        
        for cmd in commands:
            connection.send(cmd+ '\n')
            if cmd== 'sctp_status':
                  time.sleep(15)
            time.sleep(2)
        



        #Expect to recieve a maximum of 65535 bytes of data and store it in a variable

       
        mme_output = connection.recv(10000000)
        
        mme_output1 = str(mme_output)
       

        #open a file
        mme_output_file = open (fileLocation,'a')
        #First line
        mme_output_file.write ("####   "+mmeName+"  ####"+"\n")

        #Output of the command
        for line in mme_output1.split("\\r\\n"):
            
            mme_output_file.write (line+"\n")


        
    #The error handler
    except paramiko.AuthenticationException:
           #open a file
           mme_output_file = open (fileLocation,'a')
           #First line
           mme_output_file.write ("####   "+mmeName+"   ####"+"\n")
           # Second line
           mme_output_file.write ("Invalid username or password"+"\n")

           print("Invalid username or password.\n")
           print( "Closing the program")

    except Exception as e:
         
           #open a file
           mme_output_file = open (fileLocation,'a')

           mme_output_file.write ("\n")
           #First line
           mme_output_file.write ("####  "+mmeName+"  ####"+"\n")

           #catching the Exception
           mme_output_file.write ("Unable to connect to node, please check if node is reachable and operational."+"\n")
        



    finally:
        
        # closing the file
        mme_output_file.close()

    
        #Closing the connection
        session.close()
    
print("Connection Established......")





              


        
        


            


        


        
