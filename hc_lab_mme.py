import threading, paramiko
import time, datetime
import os, sys
import creating_the_hc_folder as crf
import hc_mme_cmd_output as dsm
import hc_mme_cmd_to_be_analyzed as bb
import hc_lab_env_varibles as VART
import Node_RX as full




#Defining the diretory name where you want to store the logs
global sDir
global MMEname
global ip1
global MME
sDir= VART.Directory_name
number0fboard=0
ip1=full.ip1
MME=full.MME


def board_testing_loop(ip1,MME,number0fboard):

  
  try:

   
     
    # Choosing the board number, the MME, and the sub release directory
   
    global sDir
   
    VART.importP(sDir)
   
    print('printing directory')
    print(VART.dir_name)
   
    # Creating the directory release and the testcase folder by calling them from creatingreleasefolderv1
    testcaseFolder= 'Healthcheck_logs'
    args1= (VART.dir_name,sDir, testcaseFolder)
  
    term1 = threading.Thread(target=crf.CreateDir(*args1))
   
    # Creating the file name and open/close in which directory
    
    if ip1=='':
      ext= '.txt'
   
      filename3='HC_Summary_result'
      fileLocation3= os.path.join(crf.dir_created, filename3 + ext)
      
      #open a file
      mme_output_file = open (fileLocation3,'a')
      mme_output_file.write ("\n")
      mme_output_file.write ("\t"+"\t"+"\t"+"Health Check Summary – last 24 hours"+"\n")
      
    elif ip1 !='':
      ext= '.txt'
      filename= MME+'-'+'HealthCheck'
   
      filename3='HC_Summary_result'
  
   
   
      fileLocation= os.path.join(crf.dir_created, filename + ext)

      fileLocation3= os.path.join(crf.dir_created, filename3 + ext)
   

    # printing the name of the mme that is connecting to
   
    print("Connecting to "+MME+" "+ip1+" ....")
    #calling the SSH connection and executing the pre run command and save the output to the testcase directory
    args2= (ip1, VART.username, VART.password,VART.commands,fileLocation,MME,number0fboard)
    term2 = threading.Thread(target=dsm.open_ssh_conn(*args2))
   


    term1.start()
    term1.join()
   
    term2.start()

    #term1.join()
    term2.join()

    #calling the SSH connection and executing the pre block command and save the output to the testcase directory
    args3= (ip1, VART.username, VART.password,VART.commands3,fileLocation3,MME,number0fboard)
    term3 = threading.Thread(target=bb.open_ssh_conn(*args3))  
   
    term3.start()

    term3.join()

   
    print("Testcase "+ filename+" Passed ...")

  except Exception as e:
         print (e)



board_testing_loop(ip1,MME,number0fboard)





        
