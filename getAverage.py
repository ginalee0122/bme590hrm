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