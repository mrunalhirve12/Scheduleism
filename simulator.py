"""
#====================================================================
Process Simulator

Execute: python3 simulator.py ['fifo','rr', 'cfs'] [timer interrupt value] [number of process to generate]
#====================================================================
"""

import sys
import random
import process
from schedulers import fifo, round_robin as rr, cfs
from collections import deque
from defines import START_TIME_START, START_TIME_END, BURST_TIME_START, BURST_TIME_END

#==============================================
#This function randomly generates a specified 
#number of processes
#Params:
#   num = the number of processes to create.
#         Default is 100
#Return:
#   processQ = the deque of processes sorted by
#              process start time
#==============================================
def generateProcess(num = 100):
    processQ = list()
    priorities = ["High", "Low"]

    #Create random processes
    for i in range(1, num + 1):
        processQ.append(process.Process(i, 
                                        random.choice(priorities), 
                                        random.randint(BURST_TIME_START, BURST_TIME_END), 
                                        random.randint(START_TIME_START, START_TIME_END)
                                       ))

    #Sort the process queue by start time in ascending order
    processQ = sorted(processQ, key=lambda process: process.get_startTime())
    
    for p in processQ:
        print(p)
    
    return deque(processQ)

def main():
    #Get the timer interrupt from user
    timerInterrupt = int(sys.argv[2])

    #Generate random processes
    processQ = generateProcess(int(sys.argv[3]))

    if sys.argv[1].casefold() == "fifo".casefold():
        print("SCHEDULER: FIFO")
        scheduler = fifo.FIFO(processQ, timerInterrupt)
    elif sys.argv[1].casefold() == "rr".casefold():
        print("SCHEDULER: ROUND-ROBIN")
        scheduler = rr.RR(processQ, timerInterrupt)
    elif sys.argv[1].casefold() == "cfs".casefold():
        print("SCHEDULER: CFS")
        scheduler = cfs.CFS(processQ, timerInterrupt)
    
    scheduler.run()
    
if __name__ == "__main__":
    main()