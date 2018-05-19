

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

"""
CFS uses Red-Black Trees. If we're sure that we won't have duplicate values, 
we can use: https://github.com/Enether/Red-Black-Tree/blob/master/rb_tree.py
"""
class CFS():
    def __init__(self):
        pass
    
    def addProcess(self, process):
        pass
    
    def getNextProcess(self):
        pass
    
    def run(self):
        pass
