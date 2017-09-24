
from checkbrady import checkbrady

def test_Brady():

    ''' Test CheckBrady with different HR conditions
    1 is Tachy 2 is Brady 3 is healthy'''
    assert checkbrady(160) == 1
    assert checkbrady(180) == 1
    assert checkbrady(40) == 2
    assert checkbrady(20) == 2
    assert checkbrady(80) == 3
    assert checkbrady(90) == 3