import csv, pytest

#import checkbrady #Blake's function

# import numpy as np; skiprows() to skip header; numpy.load for loading numbers; numpy.loadtxt automatically outputs into an array format
# travis: create .travis.yml ---- what language, what version of python,
# protected branches - sets criteria on what it takes to get pushed to that branch, pull request reviews, there is a way to force the team to communicate before pushing so that master branch wouldn't be broken


time = []
mV = []
def readFile(directory):
    f = open(directory, 'rt')
    data = csv.reader(f)
    next(data)
    for line in data:  
        #print(line)
        time.append(float(line[0]))
        mV.append(float(line[1]))
    #print(time)
    #print(mV)
    f.close()
        
def getAverage(mV, time, starttime, endtime, threshold):
    count = 0
    flag = 0
    averageHR = 0
    for idx, val in enumerate(time):
        if val == starttime:
            startidx = idx
        if val == endtime:
            endidx = idx
    for voltage in mV[startidx:endidx+1]:
        if voltage >= threshold and flag == 0:
            count += 1
            flag = 1
        if voltage < threshold:
            flag = 0
    print(count)
    averageHR = count/(endtime-starttime)
    return averageHR


if __name__ == "__main__":
    readFile('/Users/sylee/bme590hrm/testdata.csv')
    threshold = float(input("Enter threshold: ") or '2')
    starttime = float(input("Enter start time for average calculation: ") or time[0])
    endtime = float(input("Enter end time for average calculation: ") or time[len(time)-1])
    print(getAverage(mV, time, starttime, endtime, threshold))
