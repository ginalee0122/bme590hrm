import csv, pytest, sys
from instHR import*
from checkbrady import*

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
        time.append(float(line[0]))
        mV.append(float(line[1]))
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
        if voltage > threshold and flag == 0:
            count += 1
            flag = 1
        if voltage < threshold:
            flag = 0
    print(count)
    averageHR = count/(endtime-starttime)
    return averageHR*60

def writeFile(directory, instHR, avgHR, BCnum):
    f = open(directory,"w")
    f.write("Estimated instantaneous heart rate: "+str(instHR)+"\n")
    f.write("Estimated average heart rate: "+str(avgHR)+"\n")
    if (BCnum == 1):
        f.write("There is tachycardia detected")
    elif (BCnum == 2):
        f.write("There is bradycardia detected")
    else:
        f.write("ECG does not have any detection of tachy/brady-cardia")
    f.close()

if __name__ == "__main__":
    test_filename = str(sys.argv[1])
    readFile(test_filename)
    out_filename = str(sys.argv[2])
    threshold = float(input("Enter threshold: ") or '2')
    starttime = float(input("Enter start time for average calculation: ") or time[0])
    endtime = float(input("Enter end time for average calculation: ") or time[len(time)-1])
    instant_timepoint = float(input("Enter the specific time point for instantaneous heart rate: ") or time[0])
    instHR = instHR(getPeaks(mV, time, threshold), instant_timepoint)
    avgHR = getAverage(mV, time, starttime, endtime, threshold)
    BCnum = checkbrady(avgHR) 
    writeFile(out_filename, instHR, avgHR, BCnum) 
