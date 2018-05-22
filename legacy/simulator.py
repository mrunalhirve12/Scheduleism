"""
#====================================================================
Process Simulator

Create a list of process to run simulations of three different
schedulers.
#====================================================================
"""

import copy
import process
from schedulers import *

class Simulator:
    def __init__(self, procs, sched):
        # make a deep copy of all processes
        self.processList = copy.deepcopy(procs)
        if sched == "fifo":
            self.scheduler = fifo.FIFO()
        elif sched == "round-robin":
            self.scheduler = round_robin.RR()
        else:
            self.scheduler = cfs.CFS()
        # add processes to scheduler
        for i in self.processList:
            self.scheduler.addProcess(i)

    def run(self):
        self.scheduler.run()

# Create array of different processes to be used by each scheduler
processes = []
# TODO: create list of different processes
processes.append(process.Process(1, "High", 0, 5, 0, functions.matmult))
processes.append(process.Process(2, "Low", 2, 5, 0, functions.sum))
processes.append(process.Process(3, "Medium", 1, 5, 0, functions.sum))

# Create simulators for each scheduler
fifo = Simulator(processes, "fifo")
rr = Simulator(processes, "round-robin")
cfs = Simulator(processes, "cfs")

# Run each scheduler simulation
fifo.run()
rr.run()
cfs.run()
