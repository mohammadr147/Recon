import os  
from datetime import date
import SubFinder
import HTTPX
import DirectoryBrute

print("insert target url: ")
url = input()
filename = url+"/"+str(date.today())
os.system("mkdir "+url)
SubFinder.finding(url,filename)
HTTPX.checker(filename)
print("run directory bruteforce now[n/y]?")
ques1 = input()
if ques1 == "y":
    DirectoryBrute.dirsearch(filename)


print("SCAN COMPLATE ")
print("you can se result in /$TARGET_URL/$DATE")



