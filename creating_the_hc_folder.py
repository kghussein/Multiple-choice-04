import os, sys
import hc_lab_env_varibles as VART




def CreateDir(path, release, testcasefolder):

   global dir_created
   dir_created= os.path.join(path, release, testcasefolder)


   if os.path.exists(dir_created):
       print('already exist')
       
   else:
       os.makedirs(dir_created)
       print('Directory been created: '+ dir_created)
       
    


