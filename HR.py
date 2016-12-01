import matplotlib.pyplot as plt
import numpy as np

# load information about a bunch of stars
try:
    data = np.loadtxt('hipparcos.txt')
except IOError:
    data = np.loadtxt('/home/zabe0091/astr2600/hipparcos.txt')

# this module comes from Dan Foreman-Mackey et al.,
# at the github repo https://github.com/dfm/corner.py

import corner
corner.corner(data,
              labels=['V-I (color)',
                      'V (absolute)',
                      'RA (deg)',
                      'Dec (deg)',
                      'distance (pc)'],
              plot_density=False,
              plot_contours=False)

plt.show()
