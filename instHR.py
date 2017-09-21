import sys, os, string
# from bme590_main import readFile


def getPeaks(vs, ts, threshV=1):
    """This function loops through lists of Voltage and Time and returns two arrays,
    one containing the voltage peaks, and one with their respective time points."""
    # PeakVs = []
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


def instHR(pTs, instT=1):
    if instT < 1:
        instT = 1
    if instT > len(pTs):
        instT = len(pTs)-1
    # compute instantaneous BPM using previous time and current time
    timeDiff = pTs[instT] - pTs[instT-1]
    return 60.0/timeDiff


if __name__ == '__main__':
    # mV, time = readFile(test1.csv)
    mV = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
    time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    PeakTs = getPeaks(mV, time, 2)
    print(PeakTs)
    print(instHR([1,2,3,4,5],7))
    print(instHR(PeakTs,1))