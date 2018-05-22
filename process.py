import copy
from defines import INCOMPLETE
from defines import COMPLETE
from defines import BLOCKED

class Process (object):
    def __init__(self, pid, priority, completion_time, blockList):

        self.pid = pid
        self.priority = priority
        self.start_time = -1
        self.completion_time = completion_time
        self.counter = 0
        self.status = INCOMPLETE

        self.blockList = copy.deepcopy(blockList)
        self.block_idx = 0

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

    def print_status(self, time):
        print("time: ",time," pid: ",self.pid," priority: ",self.priority," start_time: ",self.start_time," completion_time: ",self.completion_time," counter: ",self.counter," status: ",self.status," block_idx: ",self.block_idx)

    def run(self, sysTime):
        self.counter += 1

        if self.start_time == -1:
            self.start_time = sysTime

#BLOCKED        if self.block_idx < len(self.blockList) and self.blockList[self.block_idx] <= self.counter:
#BLOCKED            self.block_idx += 1
#BLOCKED            self.status = BLOCKED
#BLOCKED            print("BLOCKED:   ",self.getPid()," at ",sysTime)
#BLOCKED            return BLOCKED
        if self.counter == self.completion_time:
            print("COMPLETED: ",self.getPid()," at ",sysTime)
            self.status = COMPLETE
            return COMPLETE
        else:
            self.status = INCOMPLETE
            return INCOMPLETE
