import function as functions
import pdb, re


class Process (object):

	def __init__(self, pid, priority, start_time, end_time, timer, functionTodo):

		self.id = pid
		self.priority = priority

		# flags state dictionary
		self.state = {'ready': False, 'blocked': False, 'running': False}

		# metrics 
		self.start_time = 0
		self.end_time = 0
		self.counter = 0

		self.functionality = functionTodo
		# result from executing the above function
		self.results = None

	# overriding the object printer for ease. Just do print(object) it spits out everything associated :)
	def __str__(self):
		return "Process ID - {}, Process priority - {}, Process State - {}, Start time - {}, End time - {}".format(self.id, self.priority, self.state, self.start_time, self.end_time)

	# Getters and setters for the process object. 

	def getPid(self):
		return self.pid

	def setPid(self, pid):
		self.pid = pid

	def getPriority(self):
		return self.priority

	def setPriority(self, p):
		self.priority = p

	def set_startTime(self, time):
		self.start_time = time

	def set_endTime(self, time):
		self.end_time = time

	def set_state(self, state):
		self.state[state] = True

	def incrementCounter(self):
		self.counter += 1
	def getProcessRuntime (self):
		return self.counter

	def launchProcess(self):
		return self.functionality()



# an example usage, it can be substituted with other function calls. - NEEDS END TO END TESTING. 
processMM = Process(1, "High", 0, 5, 0, functions.matmult)
processAdd = Process(2, "Low", 2, 5, 0, functions.sum)


procQueue = list() 		# waiting list
procQueue.extend((processMM, processAdd)) 	# adding processes to the waiting list



