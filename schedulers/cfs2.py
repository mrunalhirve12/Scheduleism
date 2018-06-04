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

Additionally, it utilizes priority levels for a 
process to determine how long the next process will
run before an interrupt is encountered. To determine
the amount of time a process will run, first a
bounded taret amount is found based on its priority.
Then that amount is divided by the total number of
runnable tasks.

process runtime = priority weight / size of readyList

Once this is found, the simulator interrupt value is
changed, guaranteeing the process will not run for
too long.

https://tampub.uta.fi/bitstream/handle/10024/96864/GRADU-1428493916.pdf
#====================================================
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
        self.readyList = [] 
        self.time_minimum = 5
        self.time_high = timerInterrupt
        self.time_low = math.floor(timerInterrupt / 2)

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


    def readyListPop(self):
        try:
            return self.readyList.pop()
        except IndexError:
            return None

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
        extraProc = 1
        if curProc is not None:
            extraProc = 2
        # get the next process to run
        nextProc = self.removeProcess()
    
        #if no new process to add, then use current process
        if nextProc is None and curProc is not None:
            nextProc = curProc
            curProc = None

        # calculate time new proc can run
        if nextProc is not None:
            time = self.systemTime - self.last_time_run[str(nextProc.getPid())]
            print("nextProc=",nextProc.getPid()," last run=:",self.last_time_run[str(nextProc.getPid())]," num_proc=",len(self.readyList)+extraProc)
            # set interrupt using this time
            time = time / (len(self.readyList)+extraProc)

            if time < self.time_minimum:
                self.timerInterrupt = self.time_minimum
            else:
                self.timerInterrupt = math.floor(time)
            print("slice=",math.floor(time))
        if curProc is not None and curProc.get_status() != COMPLETE:
            self.readyList.append(curProc)
            self.last_time_run[str(curProc.getPid())] = self.systemTime
        return nextProc

