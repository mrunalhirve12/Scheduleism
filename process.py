import copy
from defines import INCOMPLETE
from defines import COMPLETE
from defines import BLOCKED

"""
#==================================================
Process

This class simulates a process running on a system.
#==================================================
"""

class Process (object):
    #==============================================
    #Initializes a process object
    #Params:
    #   pid = process identification number
    #   priority = "High" or "Low" priority
    #   burst_time = Time required by a process for 
    #                CPU execution
    #   start_time = Time when process starts
    #                executing on CPU
    #Return:
    #   None
    #==============================================
    def __init__(self, pid, priority, burst_time, start_time):

        #Process Identification Number
        self.pid = pid

        #Priority
        self.priority = priority

        #Start Time
        self.start_time = start_time

        #Burst TIme
        self.burst_time = burst_time

        #Counter = total time that process has been executing
        self.counter = 0

        #Arrival time = the time that the process arrived to the scheduler
        self.arrival_time = -1

        #Turn Around Time = Completion Time - Arrival Time
        self.turnaround_time = -1

        #Waiting time = Turn Around Time - Burst Time
        self.waiting_time = -1

        #Completion time = Time at which process completes its execution
        self.completion_time = -1

        #Status = Is the process done executing or not
        self.status = INCOMPLETE

    #==============================================
    #String representation of the Process class
    #Params:
    #   None
    #Return:
    #   string representation of process 
    #==============================================
    def __repr__(self):
        return '{pid},{priority},{arrival},{start},{end},{burst},{turnaround},{wait},{response}'.format(pid=self.pid, priority=self.priority, arrival=self.arrival_time, start=self.start_time, end=self.completion_time, burst=self.burst_time, wait=self.waiting_time, turnaround=self.turnaround_time, response=self.start_time-self.arrival_time)

    #==============================================
    #Get the process identification number (pid)
    #Params:
    #   None
    #Return:
    #   pid = process identification number
    #==============================================
    def getPid(self):
        return self.pid

    #==============================================
    #Set the process identification number (pid)
    #Params:
    #   pid = process identification number to set
    #         to
    #Return:
    #   None
    #==============================================
    def setPid(self, pid):
        self.pid = pid

    #==============================================
    #Get the process priority
    #Params:
    #   None
    #Return:
    #   priority = either "High" or "Low" as string
    #==============================================
    def getPriority(self):
        return self.priority

    #==============================================
    #Set the process priority
    #Params:
    #   p = either "High" or "Low" as string to set
    #       priority to
    #Return:
    #   None
    #==============================================
    def setPriority(self, p):
        self.priority = p

    #==============================================
    #Get the process start time
    #Params:
    #   None
    #Return:
    #   start_time
    #==============================================
    def get_startTime(self):
        return self.start_time

    #==============================================
    #Set the process start time
    #Params:
    #   time = the start time to set for the
    #          process
    #Return:
    #   None
    #==============================================
    def set_startTime(self, time):
        self.start_time = time

    #==============================================
    #Get the process execution time
    #Params:
    #   None
    #Return:
    #   counter = current process execution time
    #==============================================
    def getProcessRuntime (self):
        return self.counter

    #==============================================
    #Set the process status
    #Params:
    #   s = the new status to set to
    #Return:
    #   None
    #==============================================
    def set_status(self, s):
        self.status = s

    #==============================================
    #Get the process status
    #Params:
    #   None
    #Return:
    #   status = current status of the process
    #==============================================
    def get_status(self):
        return self.status

    #==============================================
    #Set the arrival time for a process
    #Params:
    #   time = the new arrival time to set to
    #Return:
    #   None
    #==============================================
    def set_arrivalTime(self, time):
        self.arrival_time = time

    #==============================================
    #Get the arrival time for a process
    #Params:
    #   None
    #Return:
    #   arrival_time = the arrival time of the
    #                  process
    #==============================================
    def get_arrivalTime(self):
        return self.arrival_time

    #==============================================
    #Get the turn around time for a process
    #Params:
    #   None
    #Return:
    #   turnaround_time 
    #==============================================
    def get_turnaround_time(self):
        return self.turnaround_time

    #==============================================
    #Get the waiting time for a process
    #Params:
    #   None
    #Return:
    #   waiting_time 
    #==============================================
    def get_waiting_time(self):
        return self.waiting_time

    #==============================================
    #Get the completion time for a process
    #Params:
    #   None
    #Return:
    #   completion_time 
    #==============================================
    def get_completion_time(self):
        return self.completion_time

    #==============================================
    #"Run" the process object by incrementing the
    #counter
    #Params:
    #   sysTime = the current system time
    #Return:
    #   status = either COMPLETE or INCOMPLETE 
    #==============================================
    def run(self, sysTime):
        if self.counter == 0:
            self.start_time = sysTime

        self.counter += 1
        if self.counter == self.burst_time:
            print("COMPLETED," + str(self.getPid()) + "," + str(sysTime))
            self.status = COMPLETE
            self.completion_time = sysTime
            self.turnaround_time = self.completion_time - self.arrival_time
            self.waiting_time = self.turnaround_time - self.burst_time
            return COMPLETE
        else:
            self.status = INCOMPLETE
            return INCOMPLETE
