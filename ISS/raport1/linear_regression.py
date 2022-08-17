import csv
import numpy as np
import pandas as pd
import polyfit as pf
import matplotlib.pyplot as plt

speeds = []
lefts = []
rights = []
with open("m1.csv") as csvfile:
    read = csv.reader(csvfile, delimiter=';')
    next(read, None)
    for row in read:
        speed, left, right = row
        speeds.append(float(speed))
        lefts.append(float(left))
        rights.append(float(right))

lspeeds, plefts = map(list, zip(*[(s, x) for s, x in zip(speeds, lefts) if x > 0]))
rspeeds, prights = map(list, zip(*[(s, x) for s, x in zip(speeds, rights) if x > 0]))

left = {
    'pwm': lspeeds,
    'interrupts': plefts
}
left_df = pd.DataFrame(data=left)

x = left_df.pwm
y = left_df.interrupts
model = np.polyfit(x, y, 1)
print("left:", model[0], model[1])

plt.scatter(x, y)
x = np.linspace(lspeeds[0], lspeeds[-1])
plt.plot(x, model[0] * x + model[1])
plt.show()

right = {
    'pwm': rspeeds,
    'interrupts': prights
}
right_df = pd.DataFrame(data=right)

x = right_df.pwm
y = right_df.interrupts
model = np.polyfit(x, y, 1)
print("right:", model[0], model[1])
plt.scatter(x, y)
x = np.linspace(rspeeds[0], rspeeds[-1])
plt.plot(x, model[0] * x + model[1])
plt.show()

