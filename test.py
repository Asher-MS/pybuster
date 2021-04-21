import time
file=open("wordlist1.txt","r")

lines=file.readlines()


for i in lines:
    print(i)
    time.sleep(1)