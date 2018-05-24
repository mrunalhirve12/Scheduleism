"""
#====================================================================
Process Simulator

Execute: python3 simulator.py ['fifo','rr'] [timer interrupt value]
#====================================================================
"""
import sys
import copy
from collections import deque

import process

from schedulers import *

from defines import COMPLETE
from defines import INCOMPLETE

# checks if it's time to add a new process to simulation
def check_add_new_proc(processQ, scheduler, sysTime):
    addProcTime = sysTime+1
    if len(processQ) > 0:
        nextProc = processQ.popleft()
        addProcTime = nextProc.get_startTime()
        processQ.appendleft(nextProc)
    if addProcTime <= sysTime:
        proc = processQ.popleft()
        print("NEW PROC:  ",proc.getPid()," at ",sysTime)
        scheduler.addProcess(proc)

def main():
    if sys.argv[1] == "fifo":
        print("SCHEDULER: FIFO")
        scheduler = fifo.FIFO();
    elif sys.argv[1] == "rr":
        print("SCHEDULER: ROUND-ROBIN")
        scheduler = round_robin.RR();
    else:
        # TODO: CFS
        print("SCHEDULER: FIFO")
        scheduler = fifo.FIFO();
    timerInterrupt = int(sys.argv[2])

    # TODO: import processes from random process generator 
    # process queue in the order in which to add
    processQ = deque([])
    # Add a process to processQ with a process id, priority, time for completion,
    # and time to start the process relative to systemTime
    # Note: must add processes in sorted order by start time
    processQ.append(process.Process(1, "High", 100, 0))
    processQ.append(process.Process(2, "Low", 200, 11))
    processQ.append(process.Process(3, "High", 100, 0))

    simulator(processQ, scheduler, timerInterrupt)

def simulator(processQ, scheduler, timerInterrupt):
    prevProc = None
    curProc = None
    systemTime = 0
    procTime = 0

    while True:
        # detect conclusion of simulation
        if curProc is None and len(processQ) == 0 and scheduler.empty():
            print("FINISHED:  ",systemTime)
            break

        check_add_new_proc(processQ, scheduler, systemTime) 
        # simulated kernel space execution
        # entered via timer interrupt or no user process running
        if procTime == timerInterrupt or curProc is None or \
            (curProc is not None and curProc.get_status() == COMPLETE):
            print("EXEC:       0  at ",systemTime)
            # run the scheduler
            # impose extra time cost when switching to a new user process
            curProc = scheduler.get_next(curProc)
            if prevProc != curProc and curProc is not None:
                systemTime += 1        
                print("CTXT SWTCH:",curProc.getPid()," at ",systemTime)
                prevProc = curProc
            procTime = 0

        # simulated user space execution
        elif curProc is not None:
            print("EXEC:      ",curProc.getPid()," at ",systemTime)
            curProc.run(systemTime)
            procTime += 1

        # increment simulated hardware counter
        systemTime += 1

main()
