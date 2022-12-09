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
for cwd, folders_,files_ in os.walk("virus_samples")
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
def virus_compare(content="",virus="" ):
  for file in files_:
    content = read(file,"r")
    for virus_ in viruses:
      virus = read(virus,"r")
      for code_line in enumerate(file):
        for virus_line in enumerate(virus)
          re_search
file_scan()
print(files_)
print(folders_)
