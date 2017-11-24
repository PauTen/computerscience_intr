from math import pi, tan

def polysum(n,s):
    area = (0.25*n*s**2)/tan(pi/n)
    length = n*s
    
    return round((area+length**2),4)