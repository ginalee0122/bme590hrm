import sys, os, string
import instHR
from instHR import getPeaks
from instHR import instHR


def test_getPeaks():
    """This test will check for proper returns from the getPeak algorithm"""
    mV = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
    time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    threshV = 2
    assert getPeaks(mV,time,threshV) == [3, 3, 3, 3, 7, 11]
    mV2 = [0, 1, 2, 4, 0, 1, 2.5, 3.1, 0, 1, 2, 3]
    time2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert getPeaks(mV2,time2,threshV) == [4, 2.5, 3, 3, 6, 11]
    mV3 = [0, 1, 2, 4, 0, 1, 2.5, 3.1, 0, 1, 2, 3]
    time3 = [0, 2, 4, 6, 8, 9, 10, 11, 12, 13]
    assert getPeaks(mV2, time2, threshV) == [4, 2.5, 3, 6, 10, 13]


def test_instHR():
    """This test will check for properly working instantaneous heart rate detection."""
    pTs = [6, 10, 13]
    assert instHR(pTs, 0) == 15
    assert instHR(pTs, 3) == 20
    pTs2 = [1, 2, 3, 4, 5]
    assert instHR(pTs2, -2) == 60
    assert instHR(pTs2, 4) == 60
