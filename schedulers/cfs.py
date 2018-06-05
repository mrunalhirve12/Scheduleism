from collections import deque
from schedulers import base
from defines import COMPLETE
from defines import INCOMPLETE
from rbt import RedBlackTree
import math

"""
#==================================================
Completely Fair Scheduler

The idea behind this scheduler is to be fair in 
providing processor time to tasks. To determine 
fairness, CFS utilizes virtual runtime, which means
that the smaller amount of time a task has been 
allowed to use the processor, the higher its needs
for the processor. 

CFS also utilize a time-ordered red-black tree 
instead of regular queues for 2 reasons: it's self-
balancing and operations on tree occur in O(log n)
time.

More information can be found here:
https://www.ibm.com/developerworks/linux/library/l-completely-fair-scheduler/
#==================================================
"""

class CFS(base.BaseScheduler):
    #==============================================
    #Intialize the red black tree for CFS
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
        self.targetBound = timerInterrupt
        self.readyTree = RedBlackTree()
    
    #==============================================
    #Checks to see if the tree is empty
    #Params:
    #   None
    #Return:
    #   Boolean indiciating if tree is empty or
    #   not
    #==============================================
    def empty(self):
        return self.readyTree.getProcessesCount() == 0

    #==============================================
    #Add a process to the red black tree
    #Param:
    #   1) process = the process to be added
    #Return:
    #   None
    #==============================================
    def addProcess(self, process):
        self.readyTree.addProcess(process)

    #==============================================
    #Get the next process to run from the tree
    #Params:
    #   None
    #Return:
    #   Next process on the queue
    #   None if no process in queue
    #==============================================
    def removeProcess(self):
        return self.readyTree.getProcess()
    
    #==============================================
    #Get the next process for the scheduler to run.
    #This implements the scheduler heuristics
    #Params:
    #   curProc = Current process that's running on
    #             scheduler
    #Return:
    #   Next process in the queue via call to 
    #   removeProcess()
    #==============================================
    def getNext(self, curProc):
        if curProc is not None and curProc.get_status() == INCOMPLETE:
            self.addProcess(curProc)
        elif curProc is not None and curProc.get_status() == COMPLETE:
            curProc = None
        
        processCount = self.readyTree.getProcessesCount()
       
        if processCount > 0:
            self.timerInterrupt = math.ceil(self.targetBound / processCount)
        
        nextProc = self.removeProcess()
        return nextProc
