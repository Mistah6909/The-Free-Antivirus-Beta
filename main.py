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
#                ____              __  __ _     _        _       __ ___   ___   ___  
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

suspicion = 0
viruses = []
files = []
for cwd, folders_, files_ in os.walk("virus_sample_folder"):
    for name in files_:
        name = os.path.join(cwd,name)
        viruses.append(name)

def file_scan() :
    print("input the folder/file you want to be scan")
    for cwd, folders_, files_ in os.walk(input()):
        for name in files_ :
            files.append(os.path.join(cwd, name))

def virus_compare(virusfile="",file=""):
    global suspicion
    for virus in viruses:
        virusfile = open(virus,"r")
        for file_ in files:
            file =  open(file_,"r")
            for fileline in file.readlines():
               for virusline in virusfile.readlines():
                    comparison = re.search(virusline,fileline)
                    if comparison:
                        file_length = 0
                        print(comparison)
                        file = open(file_,"r")
                        suspicion = suspicion + 100/len(file.readlines())
                        print(f"{file_} is {suspicion} % suspicous")
file_scan()
virus_compare()
