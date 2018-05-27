import matplotlib.pyplot as plotter
from pprint import pprint
import pandas as pd
import itertools


colors = itertools.cycle(5 * ["red", "green", "cyan", "blue", "black"])


def generateProcTable(processes):
	proc = dict()
	for process in processes:
		proc[process] = next(colors)
	return proc

def buildPlot(dataframe, procDict):
	for index, row in dataframe.iterrows():
		if not row['pid'] == 0:
			p = procDict.get(row['pid'])
			plotter.plot(row['pid'], row['time'], color = p, marker= 'o', linewidth = '3')
	plotter.show()

def main():
	fifo = pd.read_csv('cfs.txt')
	processes = fifo.pid.unique()
	proc = generateProcTable(processes)
	buildPlot(fifo, proc)


if __name__ == '__main__':
	main()