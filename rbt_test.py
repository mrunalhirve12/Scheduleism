from process import Process
from rbt import RedBlackTree

Process1 = Process(1, "High", 20, 0)
Process2 = Process(2, "Low", 20, 4)
Process3 = Process(3, "High", 25, 10)
Process4 = Process(4, "High", 40, 20)

rbt = RedBlackTree()
rbt.addProcess(Process1)
rbt.addProcess(Process2)
rbt.addProcess(Process3)
rbt.addProcess(Process4)

print("Number of Nodes: " + str(rbt.count))
rbt.display()
