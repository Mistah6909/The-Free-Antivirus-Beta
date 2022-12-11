import os
import re

file_scanned = ""
global suspicion
suspicion = 0
viruses = []
files = []
for cwd, folders_, files_ in os.walk("virus_sample_folder"):
    for name in files_:
        name = os.path.join(cwd,name)
        viruses.append(name)
print(viruses)

def file_scan() :
    print("input the folder/file you want to be scan")
    for cwd, folders_, files_ in os.walk(input()):
        for name in files_ :
            files.append(os.path.join(cwd, name))

def virus_compare(file_con="", virus_con="") :
    for file in files:
        file_con = open(file,"r")
        for virus in viruses:
            virus_con = open(virus,"r")
            for virusline in virus_con.readlines():
                for fileline in file_con.readlines():
                    match = re.match(fileline,virusline)
                    if match:
                        suspicion =+ len(file_con.readlines())/100
        print(f"{file} is {suspicion}% suspicious ")
file_scan()
virus_compare()
print(files)
print(viruses)
