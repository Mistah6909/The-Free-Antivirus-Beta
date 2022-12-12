#  _______ _                                                                                           
#|__   __| |                                                                                          
#    | |  | |__   ___                                                                                  
#    | |  | '_ \ / _ \                                                                                 
#    | |  | | | |  __/                                                                                 
#   _|_|__|_|_|_|\___|__ ______            _   _ _______ _______      _______ _____  _    _  _____     
#  |  ____|  __ \|  ____|  ____|     /\   | \ | |__   __|_   _\ \    / /_   _|  __ \| |  | |/ ____|    
#  | |__  | |__) | |__  | |__       /  \  |  \| |  | |    | |  \ \  / /  | | | |__) | |  | | (___      
#  |  __| |  _  /|  __| |  __|     / /\ \ | . ` |  | |    | |   \ \/ /   | | |  _  /| |  | |\___ \     
#  | |    | | \ \| |____| |____   / ____ \| |\  |  | |   _| |_   \  /   _| |_| | \ \| |__| |____) |    
#  |_|    |_|  \_\______|______| /_/    \_\_| \_|  |_|  |_____|   \/   |_____|_|  \_\\____/|_____/     
#                                                                                 | |        | |       
#                                                                                 | |__   ___| |_ __ _ 
#                                                                                 | '_ \ / _ \ __/ _` |
#                                                                                 | |_) |  __/ || (_| |
#                                                                                 |_.__/ \___|\__\__,_|
#               ____              __  __ _     _        _       __ ___   ___   ___  
#               |  _ \         _  |  \/  (_)   | |      | |     / // _ \ / _ \ / _ \ 
#               | |_) |_   _  (_) | \  / |_ ___| |_ __ _| |__  / /| (_) | | | | (_) |
#               |  _ <| | | |     | |\/| | / __| __/ _` | '_ \| '_ \__, | | | |\__, |
#               | |_) | |_| |  _  | |  | | \__ \ || (_| | | | | (_) |/ /| |_| |  / / 
#               |____/ \__, | (_) |_|  |_|_|___/\__\__,_|_| |_|\___//_/  \___/  /_/  
#                       __/ |                                                        
#                      |___/                                                                                                                                                              
#                                   Thanks for the download!                                                                                                      










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
