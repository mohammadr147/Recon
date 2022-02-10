import os 


def dirsearch(filename):
    f= open(filename+".txt","r")
    for sub in f:
        
        os.system("dirsearch -u https://"+sub+"-F > dirctories.txt|sort -u")