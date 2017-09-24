
from checkbrady import checkbrady

def test_checkbrady():

    ''' Test CheckBrady with different HR conditions
    1 is Tachy 2 is Brady 3 is healthy'''
    assert checkbrady(160,100,60) == 1
    assert checkbrady(180,100,60) == 1
    assert checkbrady(40,100,60) == 2
    assert checkbrady(20,100,60) == 2
    assert checkbrady(80,100,60) == 3
    assert checkbrady(90,100,60) == 3
