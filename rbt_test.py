from process import Process
from rbt import RedBlackTree

Process1 = Process(1, "High", 20, 0)
Process2 = Process(2, "Low", 20, 4)
Process3 = Process(3, "High", 25, 10)
Process4 = Process(4, "High", 40, 20)
Process5 = Process(5, "High", 80, 30)
Process6 = Process(6, "High", 90, 40)

rbt = RedBlackTree()
rbt.addProcess(Process1)
rbt.addProcess(Process2)
rbt.addProcess(Process3)
rbt.addProcess(Process4)
rbt.addProcess(Process5)
rbt.addProcess(Process6)

#print("Number of Processes: " + str(rbt.getProcessesCount()))
#print("Number of Nodes: " + str(rbt.count))


#print("MINUMUM: " + str(rbt.getMinimum()))

rbt.display()
process = rbt.getProcess()
print("First Process to Run: " + process.__repr__())
print("Number of Processes: " + str(rbt.getProcessesCount()))
rbt.display()

"""
process = rbt.getProcess()
print("Second Process to Run: " + process.__repr__())
print("Number of Processes: " + str(rbt.getProcessesCount()))

process = rbt.getProcess()
print("Third Process to Run: " + process.__repr__())
print("Number of Processes: " + str(rbt.getProcessesCount()))

process = rbt.getProcess()
print("Fourth Process to Run: " + process.__repr__())
print("Number of Processes: " + str(rbt.getProcessesCount()))

process = rbt.getProcess()
print("Fifth Process to Run: " + process.__repr__())
print("Number of Processes: " + str(rbt.getProcessesCount()))

process = rbt.getProcess()
print("Sixth Process to Run: " + process.__repr__())
print("Number of Processes: " + str(rbt.getProcessesCount()))

print("Number of Nodes: " + str(rbt.count))
"""