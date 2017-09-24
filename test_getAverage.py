from getAverage import getAverage

def test_getAverage():

    ''' Test get average function with different HR conditions'''
    mV = [0,1,0,2,4,1,-2,0,1,0,2,3,-2,0,1,0,2,4,3,2,1,-2,0,1,0,1,0,2,4,1,-2,0,1,0,2,3,-2,0,1,0,2,4,3,2,1,-2,0,1]
    time=[]
    for x in range(1,49):
        time.append(x)

    assert getAverage(mV, time, 1, 48, 2) == 6./47.
    assert getAverage(mV, time, 5,12,2) == 2.0/7.0
    assert getAverage(mV, time, 29,42,2) == 3.0/13.
    assert getAverage(mV, time, 8,10,2) == 0.
    assert getAverage(mV, time, 10, 14, 2) == 0.25

