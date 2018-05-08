class Process (object):

	def __init__(self, pid, priority, addressSpace):

		self.id = pid
		self.priority = priority

		# flags
		self.ready = False
		self.blocked = False
		self.running = False


	def getPid(self):
		return self.pid

	def setPid(self, pid):
		self.pid = pid

	def getPriority(self):
		return self.priority

	def setPriority(self, p):
		self.priority = p

	def getAddrSpace(self):
		return self.addressSpace

	# def setAddrSpace(self, addrSpace):
	# 	self.addressSpace = addrSpace


