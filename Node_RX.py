
import threading, paramiko
import time, datetime
import os, sys
import hc_lab_env_varibles as VART
import hc_lab_logic as lgc
import hc_lab_mme as dana



ip1=''
MME=''

def main():
  
  
  try:
   global MMEname
   global ip1
   global MME
   global fetchingMmeName
   for MMEname in VART.mmelist:
 
    
      
      ip1=MMEname[0]
      MME=MMEname[1]
      number0fboard=int(MMEname[2])
      print(ip1)
      
      print(MMEname[1])
      print(MMEname[2])
      lgc.nFSB=0
      lgc.boardNumber=0
      lgc.list0=[]
      lgc.list_s=[]
      
      
     #calling the MME Parameters and executing the board Status
      argsMME=(ip1,MME,number0fboard)
      MME_Run= threading.Thread(target=dana.board_testing_loop(*argsMME))  
      #MME_Run= threading.Thread(target=board_testing_loop(*argsMME))
      MME_Run.start()

      MME_Run.join()
      
   
   
  except Exception as e:
         print (e)


if __name__ == '__main__':
      main()
