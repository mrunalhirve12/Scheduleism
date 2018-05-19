from collections import deque

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

class RR():
    #==============================================
    #Intialize the run queue and quantum for RR
    #Params:
    #   1) quantum = time slice for each process
    #                default = 3 cycles
    #Return:
    #   None
    #==============================================
    def __init__(self, quantum=3):
        self.runQueue = deque([])
        self.quantum = quantum

    #==============================================
    #Add a process to the end of the run queue
    #Param:
    #   1) process = the process to be added
    #Return:
    #   None
    #==============================================
    def addProcess(self, process):
        self.runQueue.append(process)

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
            return self.runQueue.popleft()
        except IndexError:
            return None
    
    #==============================================

    #==============================================
    #Run the scheduler through all the processes
    #Params:
    #   None
    #Return:
    #   None
    #==============================================
    def run(self):
        #While there's process in the queue
        while self.runQueue:
            #Get process to run
            toRun = self.getNextProcess()

            #TODO: Run process and save context

            


        