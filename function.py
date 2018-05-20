"""
Complex functions to run in a scheduler
"""

import numpy

def matmult():
    # Function to multiply  two matrix and store results
    X = [[2, 8, 3], [5, 9, 6], [7, 8, 9]]
    Y = [[5, 6, 1, 3], [6, 4, 3, 5], [4, 5, 11, 1]]
    result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    for r in result:
        print(r)


def readandwrite():
    # Function to read and write in file
    in_file = open("in_file.txt", "r")
    data = in_file.read()
    in_file.close()

    out_file = open("out_file.txt", "w")
    out_file.write(data)
    out_file.close()


""" 
Simple functions to run in a scheduler 
"""
def sum():
    x, y = numpy.random.randint(10), numpy.random.randint(1000)
    # Function to add two numbers and print them
    sum = x + y
    sentence = 'The sum of {} and {} is {}.'.format(x, y, sum)
    print(sentence)


def printline():
    # Function to print in loops
    for x in range (1, 10):
        print("")
        print("Hello World")


if __name__ == "__main__":
    # Main function
    matmult()
    printline()
    readandwrite()
    sum(2, 10)





