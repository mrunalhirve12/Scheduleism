import copy
from defines import INCOMPLETE
from defines import COMPLETE
from defines import BLOCKED

class Process (object):
    def __init__(self, pid, priority, burst_time, start_time):

        self.pid = pid
        self.priority = priority
        self.start_time = start_time
        self.burst_time = burst_time
        self.counter = 0
        self.arrival_time = -1
        self.turnaround_time = -1
        self.waiting_time = -1
        self.completion_time = -1
        self.status = INCOMPLETE

    def __repr__(self):
        return '{pid} {priority} {start} {end}'.format(pid=self.pid, priority=self.priority, start=self.start_time, end=self.burst_time)

    def getPid(self):
        return self.pid

    def setPid(self, pid):
        self.pid = pid

    def getPriority(self):
        return self.priority

    def setPriority(self, p):
        self.priority = p

    def get_startTime(self):
        return self.start_time

    def set_startTime(self, time):
        self.start_time = time

    def getProcessRuntime (self):
        return self.counter

    def set_status(self, s):
        self.status = s

    def get_status(self):
        return self.status

    def set_arrivalTime(self, time):
        self.arrival_time = time

    def get_arrivalTime(self):
        return self.arrival_time

    def print_status(self, time):
        print("time: ",time," status: ",self.status," pid: ",self.pid," priority: ",self.priority," arrival_time: ",self.arrival_time,\
              " start_time: ",self.start_time," burst_time: ",self.burst_time," counter: ",self.counter," completion_time: ",self.completion_time,\
              " turnaround_time: ",self.turnaround_time," waiting_time: ",self.waiting_time)

    def run(self, sysTime):
        if self.counter == 0:
            self.start_time = sysTime

        self.counter += 1
        if self.counter == self.burst_time:
            print("COMPLETED: ",self.getPid()," at ",sysTime)
            self.status = COMPLETE
            self.completion_time = sysTime
            self.turnaround_time = self.completion_time - self.arrival_time
            self.waiting_time = self.turnaround_time - self.burst_time
            return COMPLETE
        else:
            self.status = INCOMPLETE
            return INCOMPLETE
