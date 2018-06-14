from collections import deque
from schedulers import base
from defines import COMPLETE
from defines import INCOMPLETE
from rbt import RedBlackTree
import sys
import math

"""
#====================================================
Completely Fair Scheduler #2

Similar to the first CFS using the RBT, this aims
to select processes that have a low virtual-
runtime (process.counter). This implementation
simply uses a single deque collection to store
processes.

Each time an interrupt occurs, a new process is
retrieved from the ready list having the lowest 
runtime.

The idea is to give a process time to execute commensurate
with the amount of time it would have been running on an
ideal processor since it last executed. An ideal processor being 
one that allows all processes to run concurrently, dividing CPU 
power evenly. Consequently, when a process is chosen to run, it 
runs for the time it woud have run on that ideal processor
with the other processes concurrently.

process runtime = time waiting to run / # runnable processes

Once this is found, the simulator interrupt value is
changed, guaranteeing the process will not run beyond its
fair share.

#====================================================
"""

class CFS2(base.BaseScheduler):
    #==============================================
    #Intialize the deque and dictionary for CFS 2
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
        self.readyList = [] 
        self.target_bound = timerInterrupt

        self.last_time_run = {} #empty dictionary
    
    #==============================================
    #Checks to see if the tree is empty
    #Params:
    #   None
    #Return:
    #   Boolean indiciating if tree is empty or
    #   not
    #==============================================
    def empty(self):
        return len(self.readyList) == 0

    #==============================================
    #Add a process to the red black tree
    #Param:
    #   1) process = the process to be added
    #Return:
    #   None
    #==============================================
    def addProcess(self, process):
        if process is not None:
            self.readyList.append(process)
            self.last_time_run[str(process.getPid())] = self.systemTime

    #==============================================
    #Get the next process to run from the list with
    #the lowest runtime (process.counter)
    #Params:
    #   None
    #Return:
    #   Process with shortest runtime
    #   None if no process in queue
    #==============================================
    def removeProcess(self):
        vruntime = sys.maxsize
        nextProc = None
        for x in self.readyList:
            if x.getProcessRuntime() < vruntime:
                vruntime = x.getProcessRuntime()
                nextProc = x
        if nextProc is not None:
            self.readyList.pop(self.readyList.index(nextProc))
        return nextProc
  
    #==============================================
    #Get the next process for the scheduler to run.
    #Using the process's priority and the number of
    #runnable processes, determine how long this
    #process will run.
    #This implements the scheduler heuristics.
    #Params:
    #   curProc = Current process that's running on
    #             scheduler
    #Return:
    #   Next process in the queue via call to 
    #   removeProcess()
    #==============================================
    def getNext(self, curProc):
        #Later calculation needs to accound for processes not
        #on the readyList (nextProc and possibly curProc)
        extraProc = 1
        if curProc is not None:
            extraProc = 2
        #Get the next process to run
        nextProc = self.removeProcess()
        #If no new process to add, then use current process
        if nextProc is None and curProc is not None:
            nextProc = curProc
            curProc = None
        #Calculate time new proc can run
        if nextProc is not None:
            time = self.systemTime - self.last_time_run[str(nextProc.getPid())]
            #Set interrupt using this time
            self.timerInterrupt = math.ceil(time / (len(self.readyList)+extraProc))
        #Add current process back into readyList
        if curProc is not None and curProc.get_status() != COMPLETE:
            self.readyList.append(curProc)
            self.last_time_run[str(curProc.getPid())] = self.systemTime
        return nextProc

