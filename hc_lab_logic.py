
import time, datetime
import re
import os, sys
from datetime import timedelta

#definning the parameters
end_result=''
Success_result=''
mme_output1=''
mme_output3=''
mme_output6=''
mme_output9=''
mme_output12=''
mme_output18=''
nFSB=0
list0=[]
list_s=[]
boardNumber=0
pri=''
sec=''
unkn=''
fetchingMmeName=''


def analysis(cmd, connection,tNow,number0fboard):
            #definning the global and the list parameters
            
            eqmL_d=[]           
            global list0
            global list_s
            list2=[]
            list3=[]
            list4=[]
            list6=[]
            list7=[]
            list8=[]
            global nFSB
            global boardNumber
            global pri
            global sec
            global unkn
            global fetchingMmeName

            # To get the time befor 24 hour
            yesterday_date_time = datetime.datetime.now()-timedelta(hours =24)
            yesterday_date=yesterday_date_time.strftime('%Y-%m-%d')

           
        
            # Analyzing the hw_status output loop
            if cmd== 'hw_status':
               time.sleep(1)
               print('Starting the analysis of hw_status command')
               #list0.append("\t"+"HW Issues: ")
               global mme_output12
               #Expect to recieve a maximum of 1000000 bytes of data and store it in a variable
               
               mme_output11 = connection.recv(10000000)
               mme_output12 = str(mme_output11)
               #Analyzing the output of the command per line
               for line in mme_output12.split("\\r\\n"):

                   
                   #for Pythical/Virtual CB MME board
                   if ' CB ' in line:
                      boardNumber+=1
                      
                      #changing the line to list 
                      list4= line.split()
                      if list4[4]== 'Blocked' and list4[5]== 'Up':
                         string_board= " ".join(list4[0:6])
                         string_board2= "\t".join(list4[0:6])
                         string_summary= "\t".join(list4[4:6])
                         
                         list0.append("\t"+"\t"+str(list4[0:6]))

                      elif list4[4]== 'Blocked' and list4[5]== 'Down':
                         string_board= " ".join(list4[0:6])
                         string_board2= "\t".join(list4[0:6])
                         string_summary= "\t".join(list4[4:6])
                         
                         list0.append("\t"+"\t"+str(list4[0:6]))
                         
                      elif list4[4]== 'Unblocked' and list4[5]== 'Down':
                         string_board= " ".join(list4[0:6])
                         string_board2= "\t".join(list4[0:6])
                         string_summary= "\t".join(list4[4:6])
                        
                         list0.append("\t"+"\t"+str(list4[0:6]))
                         
                      elif list4[4]== 'Unblocked' and list4[5]== 'Up':
                         continue
                        
                         
                   #For Pythical FSB MME board
                   elif ' PM ' in line:
                      boardNumber+=1
                      
                      #changing the line to list 
                      list4= line.split()
                      if list4[3]== 'FSB':
                         nFSB +=1
                         
                         if list4[5]== 'Down' or nFSB>=3:
                            string_boardFSB= " ".join(list4[0:2])

                            list0.append("\n"+"\t"+"FSB Issues: ")
                            list0.append("\t"+"\t"+"Check FSBs"+"\n")
                            list0.append("\t"+"\t"+str(list4[0:6]))
                            


                         elif 'secondary' in line and list4[5]!= 'Down' :
                            sec='Secondary'

                         elif 'primary' in line and list4[5]!= 'Down' :
                            pri='Primary'
  
                            
                        
                      elif list4[3]== '-' and list4[5]== 'Down':
                         string_board= " ".join(list4[0:2])
                         print('board - '+ string_board)
                         list0.append("\t"+"\t"+str(list4[0:6]))

                      
                         
                   #The below logic is for the FSB in vMME
                   elif '1 11' in line and list4[1]!= '-':
                      boardNumber+=1
                      if 'secondary' in line:
                          
                        sec='Secondary'
                        #changing the line to list 
                        list4= line.split()
                        nFSB +=1
                        if list4[3]== 'FSB':
                           string_boardFSB= " ".join(list4[0:2])

                      elif 'primary' in line:
                          
                        pri='Primary'
                        #changing the line to list 
                        list4= line.split()
                        nFSB +=1
                        if list4[3]== 'FSB':
                           string_boardFSB= " ".join(list4[0:2])
                      ##############################################################################
                      elif 'unknown' in line:
                          
                        unkn='unknown'
                        #changing the line to list 
                        list4= line.split()
                        nFSB +=1
                        if list4[3]== 'FSB':
                           string_boardFSB= " ".join(list4[0:2])
                      
                   #The below logic is for the FSB in vMME

                   elif '1 13' in line and list4[1]!= '-':
                      boardNumber+=1
                      if 'secondary' in line:
                          
                        sec='Secondary'
                        #changing the line to list 
                        list4= line.split()
                        nFSB +=1
                        if list4[3]== 'FSB':
                           string_boardFSB= " ".join(list4[0:2])

                      elif 'primary' in line:
                          
                        pri='Primary'
                        #changing the line to list 
                        list4= line.split()
                        nFSB +=1
                        if list4[3]== 'FSB':
                           string_boardFSB= " ".join(list4[0:2])                


                      elif 'unknown' in line:
                          
                        unkn='unknown'
                        #changing the line to list 
                        list4= line.split()
                        nFSB +=1
                        if list4[3]== 'FSB':
                           string_boardFSB= " ".join(list4[0:2])
            
            global Success_result
            if nFSB==2 and cmd== 'hw_status' and pri=='Primary' and sec=='Secondary': 
               
               list_s.append("\n"+"FSB status: ")
               list_s.append("\t"+"Active FSBs are "+pri+' and '+sec)

            elif nFSB==2 and cmd== 'hw_status' and unkn == 'unknown' and pri=='Primary':
                 list_s.append("\n"+"FSB Issues: ")
                 list_s.append("\t"+"Active FSB is "+pri)
                 

            elif nFSB==2 and cmd== 'hw_status' and sec == '' and pri =='' :
                 list_s.append("\n"+"FSB Issues: ")
                 list_s.append("\t"+"No Active FSB ")


            elif nFSB==2 and cmd== 'hw_status' and sec == 'Secondary' and unkn =='unknown' :
                 list_s.append("\n"+"FSB Issues: ")
                 list_s.append("\t"+"Active FSB is "+sec)




            elif nFSB<=1 and cmd== 'hw_status':
               
               list0.append("\n"+"\t"+"FSB Issues: ")
               list0.append("\t"+"\t"+"Check FSBs")
            elif nFSB>=3 and cmd== 'hw_status':
               
               list0.append("\t"+"\t"+"FSB   Failure")
               
            if boardNumber == number0fboard and cmd== 'hw_status' :
               list_s.append("\n"+"HW Status:")
               list_s.append("\t"+"VM/Board Number:  "+str(number0fboard)+" of "+str(boardNumber))
            elif boardNumber!= number0fboard and cmd== 'hw_status':
               
               
               list0.append("\n"+"\t"+"HW Issues: ")
               list0.append("\t"+"\t"+"VM/Board Number:  "+str(boardNumber)+" of "+str(number0fboard))
                      
            # Analyzing the isp.log output loop
            elif cmd.startswith('sed'):
               
               time.sleep(1)
               print('Starting the analysis of isp.log command')
               list0.append("\n"+"\t"+"ISP Log Events: ")
               
               global mme_output18
               #Expect to recieve a maximum of 1000000 bytes of data and store it in a variable
               
               mme_output17 = connection.recv(10000000)
               mme_output18 = str(mme_output17)
               #Analyzing the output of the command per line
               for line in mme_output18.split("\\r\\n"): 
                  
                  if 'deblock_eqm' in line:       
                    #changing the line to list 
                      list6= line.split()
                      
                      #eqm_status=list6[2]
                      eqm_status=list6[2]
                      eqmL= eqm_status.split(';')
                      
                      list6.extend([eqmL[1],eqmL[3]])
                      del list6[2]
                      
                      list0.append("\t"+"\t"+str(list6[0:]))                        


                  elif 'block_eqm' in line:       
                    #changing the line to list 
                      list6= line.split()
                      
                      #eqm_status=list6[2]
                      eqm_status=list6[2]
                      eqmL= eqm_status.split(';')
                      
                      list6.extend([eqmL[1],eqmL[3]])
                      del list6[2]
                      
                      list0.append("\t"+"\t"+str(list6[0:]))                        

                  elif 'node_restart' in line:       
                    #changing the line to list 
                      list6= line.split()
                      print(list6[0:3])
                      #eqm_status=list6[2]
                      eqm_status=list6[2]
                      eqmL= eqm_status.split(';')
                      
                      list6.extend([eqmL[1],eqmL[3]])
                      del list6[2]
                      
                      list0.append("\t"+"\t"+str(list6[0:]))                        

                  elif 'StartUpAfter_node_restart' in line:       
                    #changing the line to list 
                      list6= line.split()
                      print(list6[0:3])
                      #eqm_status=list6[2]
                      eqm_status=list6[2]
                      eqmL= eqm_status.split(';')
                      print(eqmL)
                      print(eqmL[1])
                      list6.extend([eqmL[1],eqmL[3]])
                      del list6[2]
                      
                      list0.append("\t"+"\t"+str(list6[0:]))                        


                  elif 'StartUpAfter_large_restart' in line:       
                    #changing the line to list 
                      list6= line.split()
                      
                      #eqm_status=list6[2]
                      eqm_status=list6[2]
                      eqmL= eqm_status.split(';')
                      
                      list6.extend([eqmL[1],eqmL[3]])
                      del list6[2]
                      
                      list0.append("\t"+"\t"+str(list6[0:]))                        

                  elif 'StartUpAfter_small_restart' in line:       
                    #changing the line to list 
                      list6= line.split()
                      
                      #eqm_status=list6[2]
                      eqm_status=list6[2]
                      eqmL= eqm_status.split(';')
                      
                      list6.extend([eqmL[1],eqmL[3]])
                      del list6[2]
                      
                      list0.append("\t"+"\t"+str(list6[0:]))                        

                  elif 'StartUpAfter_initial_start' in line:       
                    #changing the line to list 
                      list6= line.split()
                      
                      #eqm_status=list6[2]
                      eqm_status=list6[2]
                      eqmL= eqm_status.split(';')
                      
                      list6.extend([eqmL[1],eqmL[3]])
                      del list6[2]
                      
                      list0.append("\t"+"\t"+str(list6[0:]))                        




            # Analyzing the get_ne output loop
            elif cmd== 'gsh get_ne':
               time.sleep(1)
               print('Starting the analysis of get_ne command')
               list_s.append("\n"+"Node Info: ")
               global mme_output6
               #Expect to recieve a maximum of 1000000 bytes of data and store it in a variable
               
               mme_output5 = connection.recv(10000000)
               mme_output6 = str(mme_output5)
               #Analyzing the output of the command per line
               for line in mme_output6.split("\\r\\n"):

                   #ni (NodeId) 
                   if r"(NodeId)" in line:
                      #changing the line to list 
                      list2= line.split()
                     
                      fetchingMmeName=str(list2[2])
                      



                   #swl (SoftwareLevel) 
                   elif line.startswith('swl'):
                      #changing the line to list 
                      list2= line.split()
                      
                      list_s.append("\t"+"Software Level: "+str(list2[2]))

                   #mgi (MmeGroupId)
                   elif line.startswith('mgi'):
                      #changing the line to list 
                      list2= line.split()
                      
                      list_s.append("\t"+"MmeGroupId: "+str(list2[2]))

                   #mc (MmeCode)
                   elif line.startswith('mc'):
                      #changing the line to list 
                      list2= line.split()
                      
                      list_s.append("\t"+"MmeCode: "+str(list2[2]))




                   #rmc (RelativeMmeCapacity)
                   elif line.startswith('rmc'):
                      #changing the line to list 
                      list2= line.split()
                      
                      list_s.append("\t"+"RelativeMmeCapacity: "+str(list2[2]))


            # Analyzing the listScs output loop
            elif cmd== 'listSCs':
               time.sleep(1)
               print('Starting the analysis of listSCs command')
               list_s.append("\n"+"Checkpoints:")
               global mme_output3
               #Expect to recieve a maximum of 1000000 bytes of data and store it in a variable
               
               mme_output2 = connection.recv(10000000)
               mme_output3 = str(mme_output2)
               #Analyzing the output of the command per line
               for line in mme_output3.split("\\r\\n"):

                   # To get the time befor 24 hour
                   #yesterday_date_time = datetime.datetime.now()-timedelta(hours =24)
                   #yesterday_date=yesterday_date_time.strftime('%Y-%m-%d')

                   #global yesterday_date
                   #today_date and change it to string: str(tNow)
                   if str(tNow) in line:
                      #changing the line to list 
                      list8= line.split()
                      
                      
                      list_s.append("\t"+str(list8[0:2]))
                    

                   #yesterday_date and change it to string: str(yesterday_date)
                   elif str(yesterday_date) in line:
                      #changing the line to list 
                      list8= line.split()
                      
                      list_s.append("\t"+str(list8[0:2]))



            # Analyzing the list_config_activated output loop
            elif cmd== 'gsh list_config_activated':
               time.sleep(1)
               print('Starting the analysis of gsh list_config_activated command')
               
               list_s.append("\n"+"Activated config:")
               global mme_output9
               #Expect to recieve a maximum of 1000000 bytes of data and store it in a variable
               
               mme_output8 = connection.recv(10000000)
               mme_output9 = str(mme_output8)
               #Analyzing the output of the command per line
               for line in mme_output9.split("\\r\\n"):

                   # To get the time befor 24 hour
                   #yesterday_date_time = datetime.datetime.now()-timedelta(hours =24)
                   #yesterday_date=yesterday_date_time.strftime('%Y-%m-%d')
                   #global yesterday_date

                   
                   #today_date and change it to string: str(tNow)
                   if str(tNow) in line:
                      #changing the line to list 
                      list7= line.split()
                      
                      list_s.append("\t"+str(list7[0:]))

                   #yesterday_date and change it to string: str(yesterday_date)
                   elif str(yesterday_date) in line:
                      #changing the line to list 
                      list7= line.split()
                      
                      list_s.append("\t"+str(list7[0:]))




               
            else:
               print('Collecting the data from '+cmd+' command without analyzing it')
               global mme_output1
               
               mme_output4 = connection.recv(10000000)
               mme_output1 += str(mme_output4)

            
            Success_result= '\n'.join(str(z) for z in list_s)   
            
            end_result= '\n'.join(str(z) for z in list0)
            
            
            #Sending the feed of the result of the commands to a file   
            global mme_outputFinal
            mme_outputFinal = end_result

print('Starting the analysis of the command/commands')
