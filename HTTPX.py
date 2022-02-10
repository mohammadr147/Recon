import os


def checker(filename):
    print("             START VALIDATION URL HTTPX       ")
    os.system("sudo httpx -l"+filename+".txt -mc 200 >"+filename+"_validurl.txt|sort -u")
    print("HTTPX COMPLATE ")

    