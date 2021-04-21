# This is the beginning of the code 
import requests
import pyfiglet
import sys
import time
import threading
import math



url=None
wordlist=None

def intro():   #Prints the welcome message
    print(pyfiglet.figlet_format("pybuster"))
    print("_________________________________")
    print("an open source tool for enumerating websites\n\n")
    print("python main.py -h for displaying the help menu")
    print("\n NOTE : Sometimes pressing ctrl-c while the program is running might not stop the process in that case try using ctrl-break/pause")



def help():    #Prints the help message
    print("Help menu")
    print("_________")
    print("-h Prints the help menu")
    print("-u specify the url")
    print("-w specify the wordlist")



def command_parser():
    global url
    global wordlist
    for i in range(len(sys.argv)):
        if(sys.argv[i]=="-h"):
            help()
        if(sys.argv[i]=="-u"):
            # print("Ent 1")
            if(sys.argv[i+1]):
                # print("rnt 1")
                url=sys.argv[i+1]
                # print(url)
            else:
                print("Please Enter the url")
        if(sys.argv[i]=="-w"):
            # print("Ent 2")
            if(sys.argv[i+1]):
                # print("rnt 2")
                wordlist=sys.argv[i+1]
                # print(wordlist)
            else:
                print("Please Enter the wordlist")

            
  






def explore(url,wordlist,no,total_threads):
    wl=open(wordlist,"r")
    wl=wl.readlines()
    start=math.floor((no)*len(wl)/total_threads)
    end=math.floor((no+1)*len(wl)/total_threads)
    for i in range(start,end):
        if(wl[i][0]=="#"):
            continue
        res=requests.get(url+"/"+wl[i])
        
        # print(res.status_code)
        # print(url+"/"+wl[i])
        
        

        if(res.status_code==200):
            print("FOUND "+wl[i])
            print((url+"/"+wl[i]))
        else:
            # print("NOT FOUND!!!")
            pass
        # time.sleep(1)





def main():
    intro()
    command_parser()
    # print(url)
    # print(wordlist)
    if(url and wordlist):
        # explore(url,wordlist,0,100)
        
        thread1=threading.Thread(target=explore,args=(url,wordlist,0,2,))  
        thread2=threading.Thread(target=explore,args=(url,wordlist,1,2,))
        # 3rd arg is the index of current thread and 4th arg is the total no of threads



        thread1.start()
        thread2.start()
        

        thread1.join()
        thread2.join()





if(__name__=="__main__"):
    main()


