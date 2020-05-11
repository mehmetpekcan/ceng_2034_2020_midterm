import os
import sys
import time
import threading
import requests

def requestByThread(url):
    print("Url {}: requesting".format(url))
    r = requests.get(url)
    r.status_code = str(r.status_code)

    if(r.status_code[0] == "2"):
      print("Url {}: is valid and status code: {}\n".format(url, r.status_code))

    elif(r.status_code[0] == "5" or r.status_code[0] == "4"):
      print("Url {}: is not valid and status code: {}\n".format(url, r.status_code))

def printCommand():
    print("""
Select a command:\n
    (0) Exit from app\n
    (1) Print PID (Process ID)\n
    (2) Print loadavg\n
    (3) Print 5 minutes loadavg and cpu core count\n 
    (4) Check the Urls are valid or not (USING THREAD\n)
    (5) Check the Urls are valid or not (BRUTAL WAY)
""")

os.system("clear")
printCommand()

urlList = ["https://api.github.com","http://bilgisayar.mu.edu.tr","https://www.python.org/",
                    "http://akrepnalan.com/ceng2034","https://github.com/caesarsalad/wow"]

while(1):
    command = input("Enter a command number: ")

    if (os.cpu_count() - os.getloadavg()[1] < 1):
        print("This is too much. Sorry\nExitting...")
        time.sleep(1)
        sys.exit()

    elif (command == "0"):
        print("Quitting...")
        time.sleep(1)
        sys.exit()

    elif (command == "1"):
        print("Pid of that running script is: {}\n"
            .format(os.getpid()) )

    elif (command == "2"):
        print("""Load average over the last 1 minute is: {}\n
Load average over the last 5 minute is: {}\n
Load average over the last 15 minute is: {}\n
        """
            .format(os.getloadavg()[0], os.getloadavg()[1], os.getloadavg()[2]))
    
    elif (command == "3"):
        print("Load average over the last 5 minute is: {}\n"
            .format(os.getloadavg()[1]))
    
    elif (command == "4"):

        startTime = time.time()
        for url in urlList:
            x = threading.Thread(target=requestByThread, args=(url,))
            x.start()
            x.join()
        finishTime = time.time()

        print("Main: All requested done successfully and passing time: {} seconds\n"
            .format( str(finishTime - startTime)[:4] ))
    
    elif (command == "5"):
        startTime = time.time()
        for url in urlList:
            requestByThread(url)
        finishTime = time.time()

        print("Main: All requested done successfully and passing time: {} seconds\n"
            .format( str(finishTime - startTime)[:4] ))

    else:
        print("Enter a valid command!\n")
        printCommand()