import serial
import time
import pandas as pd


LEFT_MEANS = []
RIGHT_MEANS = []
SPEEDS = []

def main(value):
    with serial.Serial('COM6', 9600, timeout=10) as alpha_bot:
#time.sleep(5)
        SPEEDS.append(value)
        
    
        print('Started serial port with ' + value)
        data = bytes(str(value) + '\n', 'utf-8')
        
        measurements = []
        

        
        for n in range(5):
            time.sleep(6)
            alpha_bot.write(data)
            line = alpha_bot.readline()
            line = line.decode('utf-8')
            line = line.rstrip()[1:-1]
            
            print("Measurement " + str(n))            
            left, right = map(int, line.split())
            print(f'Left motor speed = {left}')
            print(f'Right motor speed = {right}')
            print()
            
            measurements.append(left)
            measurements.append(right)
            
        leftTmp = 0
        rightTmp = 0
        for k in range(10):
            if (k % 2 == 0):
                leftTmp += measurements[k]
            else:
                rightTmp += measurements[k]
        
        
        leftTmp /= 5
        rightTmp /= 5
        
        LEFT_MEANS.append(leftTmp)
        RIGHT_MEANS.append(rightTmp)
                
        
        print("Iteration with value = " + value + " L: " + str(leftTmp) + " R: " + str(rightTmp))
    
for i in range(50, 250, 10):
    main(str(i))
    data_dict = {'Speed': SPEEDS, 'Left':LEFT_MEANS, 'Right':RIGHT_MEANS}
    dataframe = pd.DataFrame(data_dict)
    
    dataframe.to_csv("m1.csv", index=False, sep=';')