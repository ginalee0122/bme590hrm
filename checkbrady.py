def checkbrady(heartrate):
    """This function checks whether the heart is beating so fast or too slow, 
       if the heart rate is above 100, tachycardia is detected. If the heart
       rate is below 60, bradycardia is detected."""

    if (heartrate > 100):
        print('There is tachycardia detected')
        return 1

    elif (heartrate < 60):
        print('There is bradycardia detected')
        return 2

    else:
        return 3
