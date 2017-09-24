from getAverage import getAverage

def test_getAverage():

    ''' Test get average function with different HR conditions'''
    mV = [0,1,0,2,4,1,-2,0,1,0,2,3,-2,0,1,0,2,4,3,2,1,-2,0,1,0,1,0,2,4,1,-2,0,1,0,2,3,-2,0,1,0,2,4,3,2,1,-2,0,1]

    assert getAverage(mV,  0,48,2) == 1/8.
    assert getAverage(mV,  5.0,12.0,2) == 1/7
    assert getAverage(mV,  29.0,42.0,2) == 1/13
    assert getAverage(mV,  8.0,10.0,2) == 0

