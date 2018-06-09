import matplotlib
matplotlib.use("AGG")

import matplotlib.pyplot as plotter
from pprint import pprint
import pandas as pd
import itertools
from numpy import arange
from statistics import mean
from collections import OrderedDict

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
	plotter.ylabel('Processes')

	plotter.xlabel('Time')
	plotter.title(title)
	figure.savefig("static/" + title + ".png",dpi=80,facecolor='0.75',edgecolor='white')

def scheduler_plot(sched, title):
	scheduler = pd.read_csv(sched)
	processes = scheduler.pid.unique()
	proc = generateProcTable(processes)
	buildPlot(scheduler, proc, title)

def average():
	def averagePlot(d, title):
		X = arange(len(d))
		max_value = max(d.values())

		plotter.clf()
		ax = plotter.subplot(111)
		bar1 = ax.bar(X, d.values(), width=0.25, color='b', align='center')

		plotter.xticks(X, d.keys())
		plotter.ylim(ymax=max_value + 100)
		plotter.ylabel("Time")
		plotter.title("Average Times for " + title, fontsize=17)

		# Code below was found at: https://stackoverflow.com/questions/40489821/how-to-write-text-above-the-bars-on-a-bar-plot-python
		for rect in bar1:
			height = rect.get_height()
			plotter.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

		plotter.savefig("static/" + title + "_all.png",dpi=80,facecolor='0.75',edgecolor='white')

	fifo = OrderedDict()
	rr = OrderedDict()
	cfs1 = OrderedDict()
	cfs2 = OrderedDict()

	for i in range(4):
		if i == 0:
			sched = 'FIFO_all.csv'
		elif i == 1:
			sched = 'RR_all.csv'
		elif i == 2:
			sched = 'CFS_all.csv'
		elif i == 3:
			sched = 'CFS2_all.csv'

		scheduler = pd.read_csv(sched)

		turnaroundTimes = []
		waitTimes = []
		responseTimes = []

		for index, row in scheduler.iterrows():
			turnaroundTimes.append(row['turnaround'])
			waitTimes.append(row['wait'])
			responseTimes.append(row['response'])

		if i == 0:
			fifo['Wait Time'] = mean(waitTimes)
			fifo['Turnaround Time'] = mean(turnaroundTimes)
			fifo['Response Time'] = mean(responseTimes)
			averagePlot(fifo, 'FIFO')
		elif i == 1:
			rr['Wait Time'] = mean(waitTimes)
			rr['Turnaround Time'] = mean(turnaroundTimes)
			rr['Response Time'] = mean(responseTimes)
			averagePlot(rr, 'Round-Robin')
		elif i == 2:
			cfs1['Wait Time'] = mean(waitTimes)
			cfs1['Turnaround Time'] = mean(turnaroundTimes)
			cfs1['Response Time'] = mean(responseTimes)
			averagePlot(cfs1, 'CFS_1')
		elif i == 3:
			cfs2['Wait Time'] = mean(waitTimes)
			cfs2['Turnaround Time'] = mean(turnaroundTimes)
			cfs2['Response Time'] = mean(responseTimes)
			averagePlot(cfs2, 'CFS_2')

def main():
	scheduler_plot('fifo.csv', 'FIFO')
	scheduler_plot('rr.csv', 'Round-Robin')
	scheduler_plot('cfs.csv', 'CFS_1')
	scheduler_plot('cfs2.csv', 'CFS_2')
	average()

if __name__ == '__main__':
	main()
