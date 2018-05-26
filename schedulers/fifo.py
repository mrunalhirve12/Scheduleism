from collections import deque
from schedulers import base
from defines import COMPLETE
from defines import INCOMPLETE

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

class FIFO(base.BaseScheduler):
    #==============================================
    #Intialize the run queue for FIFO
    #Params:
    #   processQ = Deque of processes to run
    #   timerInterrupt = Allows scheduler to check
    #                    on running process and to
    #                    make decisions
    #Return:
    #   None
    #==============================================
    def __init__(self, processQ, timerInterrupt):
        super().__init__(processQ, timerInterrupt)
        self.readyList = deque([])

    #==============================================
    #Checks to see if the queue is empty
    #Params:
    #   None
    #Return:
    #   Boolean indiciating if queue is empty or
    #   not
    #==============================================
    def empty(self):
        return len(self.readyList) == 0
    
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
    def removeProcess(self):
        try:
            return self.readyList.popleft()
        except IndexError:
            return None
    
    #==============================================
    #Get the next process for the scheduler to run.
    #This implements the scheduler heuristics
    #Params:
    #   curProc = Current process that's running on
    #             scheduler
    #Return:
    #   curProc = see Params section
    #   OR
    #   Next process in the queue via call to 
    #   removeProcess()
    #==============================================
    def getNext(self, curProc):
        if curProc is not None and curProc.get_status() == INCOMPLETE:
            return curProc
        elif curProc is not None and curProc.get_status() == COMPLETE:
            curProc = None
        return self.removeProcess()
