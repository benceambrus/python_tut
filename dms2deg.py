import math

def dms2rad(dms):
    dmsSplit = [float(x) for x in dms.split('-')]
    return (dmsSplit[0] + dmsSplit[1]/60 + dmsSplit[2]/3600) * math.pi/180