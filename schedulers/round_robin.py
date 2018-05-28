from collections import deque
from schedulers import base
from defines import COMPLETE
from defines import INCOMPLETE

"""
#==================================================
Round Robin Scheduler

The idea behind this scheduler is to assign a fixed
time slot for each process, called a quantum. The 
processes are executed in a cyclic way. Once a 
process is executed for a given time period, it's 
preempted and the next process executes for its 
time period. Context switching is used to save the
states of preempted processes.
#==================================================
"""

class RR(base.BaseScheduler):
    #==============================================
    #Intialize the run queue for RR
    #Params:
    #   processQ = Deque of processes to run
    #   timerInterrupt = Allows scheduler to check
    #                    on running process and to
    #                    make decisions
    #Return:
    #   None
    #==============================================
    def __init__(self, processQ, quantum):
        super().__init__(processQ, quantum)
        self.readyList = deque([])
        self.quantum = quantum

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
    #   Next process in the queue via call to 
    #   removeProcess()
    #==============================================
    def getNext(self, curProc):
        if curProc is not None and curProc.get_status() == INCOMPLETE:
            self.addProcess(curProc)
        elif curProc is not None and curProc.get_status() == COMPLETE:
            curProc = None
        return self.removeProcess()

    # ==============================================
    # This function actually runs the scheduler using
    # the heuristics that's implemented in the
    # getNext function
    # Params:
    #   None
    # Return:
    #   None
    # ==============================================
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
                print("NEW PROC:  ",proc.getPid()," at ",self.systemTime)
                proc.set_arrivalTime(self.quantum)
                self.addProcess(proc)

        prevProc = None
        curProc = None
        while True:
            # Check to see if scheduler is finished
            if curProc is None and len(self.processQ) == 0 and self.empty():
                print("FINISHED:  ",self.systemTime)
                break

            check_add_new_proc()
            # Simulated kernel space execution
            # Entered via timer interrupt or no user process running
            if self.procTime == self.timerInterrupt or curProc is None or \
                (curProc is not None and curProc.get_status() == COMPLETE):
                print("EXEC:       0  at ", self.systemTime)
                # Run the scheduler
                # Impose extra time cost when switching to a new user process
                curProc = self.getNext(curProc)
                if prevProc != curProc and curProc is not None:
                    self.systemTime += 1
                    print("CTXT SWTCH:",curProc.getPid()," at ", self.systemTime)
                    prevProc = curProc
                self.procTime = 0

            # Simulated user space execution
            elif curProc is not None:
                print("EXEC:      ",curProc.getPid()," at ", self.systemTime)
                curProc.run(self.systemTime)
                self.procTime += 1

            # Increment simulated hardware counter
            self.systemTime += 1