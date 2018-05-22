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

# process queue in the order in which to add
processQ = deque([])

# Add a process to processQ with a process id, priority, time for completion,
# and time to start the process relative to systemTime
# Note: must add processes in sorted order by start time
processQ.append(process.Process(1, "High", 20, 0))
processQ.append(process.Process(2, "Low", 20, 11))

curProc = None

while True:
    # detect conclusion of simulation
    if curProc is None and len(processQ) == 0 and scheduler.empty():
        print("FINISHED:  ",systemTime)
        break

    # simulated kernel space execution
    # entered via timer interrupt, process blocking, or no user process running
    elif procTime == timerInterrupt or curProc is None or \
        (curProc is not None and curProc.get_status() == COMPLETE):

        # TODO: add function that determines if it's time to add a new process
        # check if it's time to add a new process to simulation
        addProcTime = systemTime+1
        if len(processQ) > 0:
            nextProc = processQ.popleft()
            addProcTime = nextProc.get_startTime()
            processQ.appendleft(nextProc)
        if addProcTime <= systemTime:
            proc = processQ.popleft()
            print("NEW PROC:  ",proc.getPid()," at ",systemTime)
            scheduler.addProcess(proc)

        # run the scheduler
        curProc = scheduler.get_next(curProc)

        procTime = 0

    # simulated user space execution
    if curProc is not None:
        print("EXEC:      ",curProc.getPid()," at ",systemTime)
        curProc.run(systemTime)
        procTime += 1
    else:
        print("EXEC:       0  at ",systemTime)
        procTime += 1

    # increment simulated hardware counters
    systemTime += 1
