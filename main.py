# This is the beginning of the code 
import requests
import pyfiglet
import sys
import time

url=None
wordlist=None

def intro():   #Prints the welcome message
    print(pyfiglet.figlet_format("pybuster"))
    print("_________________________________")
    print("an open source tool for enumerating websites\n\n")
    print("python main.py -h for displaying the help menu")




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

            
  






def explore(url,wordlist):
    wl=open(wordlist,"r")
    for i in wl:
        if(i[0]=="#"):
            continue
        res=requests.get(url+"/"+i)
        
        # print(url+"/"+i)
        # print(res.status_code)
        
        

        if(res.status_code==200):
            print("FOUND "+i)
            print((url+"/"+i))
        else:
            # print("NOT FOUND!!!")
            pass
        time.sleep(1)





def main():
    intro()
    command_parser()
    # print(url)
    # print(wordlist)
    if(url and wordlist):
        explore(url,wordlist)
    





if(__name__=="__main__"):
    main()


