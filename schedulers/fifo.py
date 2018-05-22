from collections import deque
from defines import COMPLETE
from defines import INCOMPLETE
from defines import BLOCKED

"""
#==================================================
First In First Out

The idea behind this scheduling algorithm is that
tasks are scheduled in the order that they are
added in the queue. The process is executed till it
is completed or it's given up the CPU. The downside
with this is that this algorithm is nonpreemptive,
which means that short processes which are in the 
back of queue will have to wait for long process at
front to finish. 
#==================================================
"""
class FIFO():
    #==============================================
    #Intialize the run queue for FIFO
    #Params:
    #   None
    #Return:
    #   None
    #==============================================
    def __init__(self):
        self.readyList = deque([])
        self.blockedList = deque([])

    # reorders process list based on arrival time for the scheduler
    # to pick up a single process. 

    #==============================================
    #Add a process to the end of the run queue
    #Param:
    #   1) process = the process to be added
    #Return:
    #   None
    #==============================================
    def addProcess(self, process):
        self.readyList.append(process)
    
    #==============================================
    #Get the next process on the queue
    #Params:
    #   None
    #Return:
    #   Next process on the queue
    #   None if no process in queue
    #==============================================
    def getNextProcess(self):
        try:
            return self.readyList.popleft()
        except IndexError:
            return None
    
    #==============================================
    #Run the scheduler through all the processes
    #Params:
    #   None
    #Return:
    #   None
    #==============================================
    def get_next(self, curProc):
        if curProc is not None and curProc.get_status() == INCOMPLETE:
            return curProc
        #elif curProc is not None and curProc.get_status() == BLOCKED:
        #    self.blockedList.append(curProc)
        elif curProc is not None and curProc.get_status() == COMPLETE:
            curProc = None
        proc = self.getNextProcess()
        return proc

    # true if all lists empty
    def empty(self):
        if len(self.readyList) == 0 and len(self.blockedList) == 0:
            return True
        return False

    # move everything from blocked list to ready list
    def check_blocked(self):
        while len(self.blockedList) > 0:
            proc = self.blockedList.popleft()
            proc.set_status(INCOMPLETE)
            self.readyList.append(proc)
