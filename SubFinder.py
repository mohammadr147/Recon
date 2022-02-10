import os 


def finding(url,filename):
    print("               SUBFINDER STARTED                     ")
    os.system("subfinder -d "+url+" -silent > "+filename+".txt|sort -u")

    f= open(filename+".txt","r")
    for sub in f:
        os.system("subfinder -d "+sub+" >>"+filename+".txt|sort -u")
        
    print("                    SUBFINDER COMPELET               ")