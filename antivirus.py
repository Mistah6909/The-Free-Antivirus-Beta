#import cryptography
#from cryptography.fernet import Fernet
#key = Fernet.generate_key()
#my_secret = os.environ[key 

import os
import re
file_scanned = ""
suspicion = 0
viruses = []
unscanned_files = []
files= []
folders= []
for cwd, folders_,files_ in os.walk("virus_samples"):
  name = os.path.join(cwd,name)
  viruses.append
def file_scan():
  print("input the folder/file you want to be scan")
  for cwd, folders_, files_ in os.walk(input(),topdown=False):
    for name in files:
      item_scanned = os.path.join(cwd, name)
      if os.path.isfile(item_scanned):
        print(name + " is file") 
        files.append(item_scanned)
      elif os.path.isfile(item_scanned) == False:
        print(name + " is folder")
        folders.append(item_scanned)
  for folder in folders:
     name = os.path.join() 
def virus_compare(content="",virus="" ):
  for file in files_:
    content = read(file,"r")
    for virus_ in viruses:
      virus = read(virus,"r")
      for code_line in enumerate(file):
        for virus_line in enumerate(virus):
          if re.match(virus_line,code_line) == True:
            suspicion =+ 100/len(content.readlines())
         
file_scan()
print(files_)
print(folders_)
        for virus_line in enumerate(virus):
          re.match(virus_line,code_line)
         
file_scan()
print(files_)
print(folders_)
