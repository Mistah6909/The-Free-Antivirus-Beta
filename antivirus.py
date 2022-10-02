#from cryptography.fernet import fernet
import os
import re
file_extensions = [".txt",".py",".jar"]
item = None
scanned_files = []
folders = []
files = []
checked_files = []
print("please give the directory of the file youd like to scan")

def file_scan(file = None):
  file = input()
  scanned_files.append(os.listdir(file))
  for file_extension in file_extensions:
    for file in scanned_files:
      checked_files = re.findall(str(file_extension),str(file))
      print(checked_files)
      print(file)
      if file in checked_files:
        files.append(file)
      if file not in checked_files:
        folders.append(file)
    
file_scan()
print(checked_files)
print("scanned files:" + str(scanned_files))
print("scanned folders:" + str(folders))
print(files)
