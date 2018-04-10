import pandas as pd
import math
from point import Point

def dms2rad(dms):
    dmsSplit = [float(x) for x in dms.split('-')]
    return (dmsSplit[0] + dmsSplit[1]/60 + dmsSplit[2]/3600) * math.pi/180

def rad2dms(rad, p=0):
    deg = rad * 180/math.pi
    d = math.floor(deg)
    m = math.floor((deg - d) * 60)
    s = round(((deg - d) * 60 - m) * 60, p)

    return "{:.0f}-{:02.0f}-{:02.0f}".format(d, m, s)

# orientation
# read coordinates
df = pd.read_csv('coo.csv')

pnts = {}  # new dictionary for points
# convert data to dictionary of Point objects
for i in range(df.shape[0]):
    pnts[df['id'][i]] = Point(df['x'][i], df['y'][i])

# read station target and mean direction from csv file
meas = pd.read_csv('meas.csv', dtype={'station': str, 'target': str})

# calculate orientation angles
ori = []
for i in range(meas.shape[0]):
    ang = (pnts[meas['target'][i]] - pnts[meas['station'][i]]).bearing() - dms2rad(meas['direction'][i])
    if ang < 0:
        ang += 2*math.pi
    ori.append(ang)

dist = [abs(pnts[meas['target'][i]] - pnts[meas['station'][i]]) for i in range(meas.shape[0])]

meanOri = sum([o * d for (o, d) in zip(ori, dist)]) / sum(dist)
print("Mean orientation angle: {:s}".format(rad2dms(meanOri)))