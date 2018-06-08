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

def buildPlot(dataframe, procDict, title):
	figure = plotter.figure(figsize=(6,6))
	for index, row in dataframe.iterrows():
		if not row['pid'] == 0:
			p = procDict.get(row['pid'])
			plotter.plot(row['time'], row['pid'], color = p, marker= 'o', linewidth = '3')
	plotter.ylabel('processes')
	plotter.xlabel('time')
	plotter.title(title)
	#plotter.show()
	figure.savefig(title+'.png',dpi=80,facecolor='0.75',edgecolor='white')

def scheduler_plot(sched, title):
	scheduler = pd.read_csv(sched)
	processes = scheduler.pid.unique()
	proc = generateProcTable(processes)
	buildPlot(scheduler, proc, title)

def main():
        scheduler_plot('../fifo.csv', 'FIFO')
        scheduler_plot('../rr.csv', 'Round-Robin')
        scheduler_plot('../cfs.csv', 'CFS #1')
        scheduler_plot('../cfs2.csv', 'CFS #2')

if __name__ == '__main__':
	main()
