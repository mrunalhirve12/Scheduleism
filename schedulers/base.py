from abc import ABC, abstractmethod

import sys
import process
from defines import COMPLETE
from defines import INCOMPLETE

class BaseScheduler(ABC):
    #==============================================
    #Intialize the scheduler
    #Params:
    #   processQ = Deque of processes to run
    #   timerInterrupt = Allows scheduler to check
    #                    on running process and to
    #                    make decisions
    #Return:
    #   None
    #==============================================
    def __init__(self, processQ, timerInterrupt):
        self.processQ = processQ
        self.completedQ = []
        self.timerInterrupt = timerInterrupt
        self.systemTime = 0
        self.procTime = 0
    
    #==============================================
    #Abstract method for check to see if scheduler
    #process data structure is empty
    #Params:
    #   None
    #Return:
    #   Boolean indiciating if queue is empty or
    #   not
    #==============================================
    @abstractmethod
    def empty(self):
        pass

    #==============================================
    #Add a process to the scheduler process data
    #structure
    #Param:
    #   1) process = the process to be added
    #Return:
    #   None
    #==============================================
    @abstractmethod
    def addProcess(self, process):
        pass
    
    #==============================================
    #Get the next process from the scheduler process
    #data structure
    #Params:
    #   None
    #Return:
    #   Next process on the queue
    #   None if no process in queue
    #==============================================
    @abstractmethod
    def removeProcess(self):
        pass
    
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
    @abstractmethod
    def getNext(self, curProc):
        pass
    
    #==============================================
    #This function actually runs the scheduler using
    #the heuristics that's implemented in the
    #getNext function
    #Params:
    #   None
    #Return:
    #   None
    #==============================================
    def run(self):
        #Checks if it's time to add a new process to simulation
        def check_add_new_proc():
            addProcTime = self.systemTime + 1
            if len(self.processQ) > 0:
                nextProc = self.processQ.popleft()
                addProcTime = nextProc.get_startTime()
                self.processQ.appendleft(nextProc)
            if addProcTime <= self.systemTime:
                proc = self.processQ.popleft()
                print("NEW_PROC," + str(proc.getPid()) + "," + str(self.systemTime))
                proc.set_arrivalTime(self.systemTime)
                self.addProcess(proc)

        prevProc = None
        curProc = None
        while True:
            # Check to see if scheduler is finished
            if curProc is None and len(self.processQ) == 0 and self.empty():
                print("FINISHED,," + str(self.systemTime))
                break

            check_add_new_proc() 
            # Simulated kernel space execution
            # Entered via timer interrupt, no user process running,
            # or process has completed
            if self.procTime == self.timerInterrupt or curProc is None or \
                (curProc is not None and curProc.get_status() == COMPLETE):
                print("EXEC,0," + str(self.systemTime))
                # Add completed proces to completedQ
                if curProc is not None and curProc.get_status() == COMPLETE:
                    self.completedQ.append(curProc)
                    curProc = None
                # Run the scheduler
                # Impose extra time cost when switching to a new user process
                curProc = self.getNext(curProc)
                if prevProc != curProc and curProc is not None:
                    self.systemTime += 1        
                    print("CTXT_SWTCH," + str(curProc.getPid()) + "," + str(self.systemTime))
                    prevProc = curProc
                self.procTime = 0

            # Simulated user space execution
            elif curProc is not None:
                print("EXEC," + str(curProc.getPid()) + "," + str(self.systemTime))
                curProc.run(self.systemTime)
                self.procTime += 1

            # Increment simulated hardware counter
            self.systemTime += 1
        newFile = str(self.__class__.__name__)+'_all.csv'
        sys.stdout = open(newFile, 'w+')
        print("pid,priority,arrival,start,end,burst,turnaround,wait,response")
        # Dump all process info
        for i in range (0,len(self.completedQ)):
            print(self.completedQ[i])
