"""
#====================================================================
Process Simulator

Command Line: 
    usage: simulator.py [-g] [-h] interrupt

    Required Arguments:
    interrupt         Timer Interrupt Value

    Optional Arguments:
    -g , --generate   Number of processes to generate for scheduler
    -h, --help        Show this help message.
#====================================================================
"""
import sys
import random
import process
from schedulers import fifo, round_robin as rr, cfs, cfs2
from collections import deque
from defines import START_TIME_START, START_TIME_END, BURST_TIME_START, BURST_TIME_END
import argparse
import copy
from utils.procPlot import main as mn
#==============================================
#This function randomly generates a specified 
#number of processes
#Params:
#   num = the number of processes to create.
#         Default is 100
#Return:
#   processQ = the deque of processes sorted by
#              process start time
#==============================================
def generateProcess(num):
    #Start the process queue as a list
    processQ = list()
    priorities = ["High", "Low"]

    #Create random processes
    for i in range(1, num + 1):
        processQ.append(process.Process(i, random.choice(priorities), 
                                           random.randint(BURST_TIME_START, BURST_TIME_END), 
                                           random.randint(START_TIME_START, START_TIME_END)))

    #Sort the process queue by start time in ascending order
    processQ = sorted(processQ, key=lambda process: process.get_startTime())

    #Convert the sorted process list into a process queue before returning it
    return deque(processQ)

#==============================================
#This function starts the scheduler simulation.
#The outputs of each of the scheuders are
#written to a CSV file, specifically:
#   FIFO = fifo.csv
#   RR = rr.csv
#   CFS = cfs.csv
#Params:
#   timerInterrupt = Allows scheduler to check
#                    on running process and to
#                    make decisions
#   processNum = the number of processes to 
#                create. Default is 100
#Return:
#   None
#==============================================
def start_simulation(timerInterrupt, processNum):
    #Generate random processes
    cfsQ = generateProcess(processNum)

    #Set system output to fifo.csv for FIFO scheduler
    sys.stdout = open('fifo.csv', 'w+')
    print("status,pid,time")
    #Make deep copy of the process queue
    fifoQ = copy.deepcopy(cfsQ)
    #Initialize FIFO class object and run the scheduler
    fifo_sched = fifo.FIFO(fifoQ, timerInterrupt)
    fifo_sched.run()

    #Set system output to rr.csv for RR scheduler
    sys.stdout = open('rr.csv', 'w+')
    print("status,pid,time")
    #Make deep copy of the process queue
    rrQ = copy.deepcopy(cfsQ)
    #Initialize RR class object and run the scheduler
    rr_sched = rr.RR(rrQ, timerInterrupt)
    rr_sched.run()

    #Set system output to cfs.csv for CFS scheduler
    sys.stdout = open('cfs.csv', 'w+')
    print("status,pid,time")
    #Make deep copy of the process queue
    cfs2Q = copy.deepcopy(cfsQ)
    #Initialize CFS class object and run the scheduler
    cfs_sched = cfs.CFS(cfsQ, timerInterrupt)
    cfs_sched.run()

    #Set system output to cfs2.csv for CFS2 scheduler
    sys.stdout = open('cfs2.csv', 'w+')
    print("status,pid,time")
    #Initialize CFS class object and run the scheduler
    cfs2_sched = cfs2.CFS2(cfs2Q, timerInterrupt)
    cfs2_sched.run()

    sys.stdout = sys.__stdout__
    
#==============================================
#This function handles to command line argument
#parsing for the simulation using argparse and
#starts the simulation based on the input 
#given.
#Params:
#   None
#Return:
#   None
#==============================================
def main():
    #Initialize argparse object
    parser = argparse.ArgumentParser(add_help=False)

    #Custom titles for required and optional arguments
    parser._positionals.title = 'Required Arguments'
    parser._optionals.title = 'Optional Arguments'

    #This argument is for specifying the timer interrup
    parser.add_argument('interrupt', help="Timer Interrupt Value", type=int)

    #This argument is for specifying the number of process to generate for the schedulers.
    #The default value is 100 processes
    parser.add_argument("-g", "--generate", metavar="", help="Number of processes to generate for scheduler", type=int, default=100)

    #This argument is the custom help message
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Show this help message.')

    #Get the values from the command line arguments
    args = parser.parse_args()

    #Start the simulation
    start_simulation(args.interrupt, args.generate)
    
    #Process data and generate graphs in the static folder
    mn()
    
if __name__ == "__main__":
    main()
