'''This module makes a plot of some stars from the Hipparcos mission.'''

import matplotlib.pyplot as plt
import numpy as np

# load information about a bunch of stars
try:
    data = np.loadtxt('hipparcos.txt')
except IOError:
    data = np.loadtxt('/home/zabe0091/astr2600/hipparcos.txt')

# the Right Ascension is the third column in thetable
ra = data[:,2]

# the Declination is the fouth column in the table
dec = data[:,3]

# make a plot of the RA and Dec of the stars
plt.scatter(ra, dec, marker='.', s=1)
plt.xlabel('RA (degrees)')
plt.ylabel('Dec (degrees)')

# make the plot display to the screen
plt.show()
