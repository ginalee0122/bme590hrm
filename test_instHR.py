import sys, os, string
import instHR
from instHR import getPeak()

def test_instHR():
    """This test will check for properly working instantaneous heart rate detection."""
    assert instHR(test1.csv) == 60
    assert instHR(test2.csv) == 100

def test_getPeak():
    mV = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
    time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    threshV = 2
    assert getPeak(mV,time,threshV) == [3, 3, 3, 3, 7, 11]