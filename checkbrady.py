def checkbrady(heartrate):


    if (heartrate > 100):
        print('There is tachucardia detected')
        return 1

    elif (heartrate < 60):
        print('There is brady detected')
        return 2

    else:
        return 3
