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

from schedulers import fifo
from schedulers import round_robin

from defines import COMPLETE
from defines import INCOMPLETE
from defines import BLOCKED


if sys.argv[1] == "fifo":
    print("SCHEDULER: FIFO")
    scheduler = fifo.FIFO();
elif sys.argv[1] == "rr":
    print("SCHEDULER: ROUND-ROBIN")
    scheduler = round_robin.RR();
else:
    print("SCHEDULER: FIFO")
    scheduler = fifo.FIFO();

timerInterrupt = int(sys.argv[2])

systemTime = 0
procTime = 0

#process queue and order in which to add
processQ = deque([])
add_idx = 0
add_timing = [] 

# Add a process to processQ AND add the general systemTime value this process
# should be added into the simulation to add_timing
processQ.append(process.Process(1, "High", 20, [5,11]))
add_timing.append(0)
processQ.append(process.Process(2, "Low", 20, []))
add_timing.append(10)

curProc = None
scheduler.addProcess(processQ.popleft()) # start with one process ready to go in scheduler
add_idx += 1
status = INCOMPLETE

while True:
    # detect conclusion of simulation
    if curProc is None and len(processQ) == 0 and scheduler.empty():
        print("FINISHED:  ",systemTime)
        break

    # simulated kernel space execution
    # entered via timer interrupt, process blocking, or no user process running
    elif procTime == timerInterrupt or curProc is None or \
        (curProc is not None and (curProc.get_status() == BLOCKED or curProc.get_status() == COMPLETE)):

        scheduler.check_blocked() # unblock all processes
        # check if it's time to add a new process to simulation
        if add_idx < len(add_timing) and add_timing[add_idx] <= systemTime \
           and len(processQ) > 0:
            add_idx += 1
            proc = processQ.popleft()
            print("NEW PROC:  ",proc.getPid()," at ",systemTime)
            scheduler.addProcess(proc)

        # run the scheduler
        curProc = scheduler.get_next(curProc)

        # print context for next CPU cycle
        if curProc is not None:
            print("NEW CTXT:  ",curProc.getPid()," at ",systemTime)
        else:
            print("NEW CTXT:   0  at ",systemTime)
        procTime = 0

    # simulated user space execution
    if curProc is not None:
        print("EXEC:      ",curProc.getPid()," at ",systemTime)
        status = curProc.run(systemTime)
        procTime += 1
    else:
        print("IDLE:      ",systemTime)
        procTime += 1

    # increment simulated hardware counters
    systemTime += 1
