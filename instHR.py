import sys, os, string
# from bme590_main import readFile


def getPeaks(vs, ts, threshV=1):
    """This function loops through lists of Voltage and Time and returns one array
    containing the voltage peaks, and one with their respective time points."""

    PeakTs = []
    threshPassedBool = False

    for i in range(0,len(vs)):
        inV = vs[i]
        inT = ts[i]
        if inV > threshV and not threshPassedBool:
            threshPassedBool = True
            # PeakVs.append(inV)
            PeakTs.append(inT)
        if inV < threshV:
            threshPassedBool = False

    return PeakTs


def instHR(pTs, instT=0):
    """This function takes in a time array of PEAKS (len>1; output from getPeaks) and
    the desired instantaneous timepoint. If the timepoint lies between two peaks, the
    time difference between the two peaks will be calculated. This time difference
    represents the bpm once divided by 60."""

    if len(pTs) < 2:
        print("ERROR: Input must have more than one peak!")
        return 0

    prevT = pTs[0]
    if instT < pTs[1]:  # set index to second peak if before the second time point
        instT = pTs[1]
    elif instT >= pTs[len(pTs)-1]:  # set index to last peak if after the last time point
        instT = pTs[len(pTs)-1]
        prevT = pTs[len(pTs)-2]
    else:
        lastT = pTs[0]
        for peakT in pTs:
            if instT <= peakT and instT > lastT:
                instT = peakT
                prevT = lastT
            else:
                lastT = peakT
    # compute instantaneous BPM using previous time and current time
    timeDiff = instT - prevT
    return 60.0/timeDiff


if __name__ == '__main__':
    # mV, time = readFile(test1.csv)
    mV = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
    time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    PeakTs = getPeaks(mV, time, 2)
    print(PeakTs)
    print(instHR([6, 10, 13], 3))
    print(instHR(PeakTs, 11))
