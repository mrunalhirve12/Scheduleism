import random

def generator(k):
    l = []
    start = []
    end = []
    run = []
    priority = []


    t = ()
    tx = ()

    for j in range(k):
        for i in range(3):
            lx = [[0, 0, 0, 0, 0]]

            start.insert(i, random.randint(1, 1000))
            priority.insert(i, random.randint(1, 4))
            end.insert(i, random.randint(1, 1000))
            run.insert(i, end[i] - start[i])
            if run[i] < 0:
                start[i], end[i] = end[i], start[i]
            run.insert(i, end[i] - start[i])

            lx[0][0] = j+1
            lx[0][1] = start[i]
            lx[0][2] = end[i]
            lx[0][3] = run[i]
            lx[0][4] = priority[i]

            l.append(lx)

            tx = tuple(lx)

            lx.clear()
        t = t + tx

    return t


if __name__ == '__main__':
    print("process id, start time,end time, run time, priority")
    processes=generator(4)
    print(processes)
