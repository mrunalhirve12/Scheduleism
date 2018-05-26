"""
#====================================================================
Process Simulator

Execute: python3 simulator.py ['fifo','rr', 'cfs'] [timer interrupt value]
#====================================================================
"""

import sys
import process
from schedulers import fifo, round_robin as rr, cfs
from collections import deque

def main():
    timerInterrupt = int(sys.argv[2])
    # TODO: import processes from random process generator 
    # process queue in the order in which to add
    processQ = deque([])
    # Add a process to processQ with a process id, priority, time for completion,
    # and time to start the process relative to systemTime
    # Note: must add processes in sorted order by start time
    processQ.append(process.Process(1, "High", 100, 0))
    processQ.append(process.Process(2, "High", 100, 0))
    processQ.append(process.Process(3, "Low", 200, 11))

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