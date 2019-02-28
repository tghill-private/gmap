"""

module read.py

Parses gps files into a standardized class to represent the data

"""

import csv

import numpy as np

from . import dtime
from . import distance

class gs:
    """Simple class to represent data from a file.

    This simple class is used so that all file types
    return the same type of object.
    """
    def __init__(self, times, lats, lons, altitudes):
        self.times = times
        self.latitudes = lats
        self.longitudes = lons
        self.altitudes = altitudes

        self.path_length = distance.path_length(self.latitudes, self.longitudes)

        self.total_time = times[-1] - times[0]

        self.marker = r"%s\nDistance: %.3f km\nTotal Time: %s" %(
                        times[0], self.path_length/1000., self.total_time)

def gps(fname):
    """Parses csv files into a gs class"""
    times = np.array([])
    lats = np.array([])
    lons = np.array([])
    altitudes = np.array([])

    with open(fname, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)

        for row in csvreader:
            times = np.append(times, dtime.strptime(row[0]))
            lats = np.append(lats, float(row[1]))
            lons = np.append(lons, float(row[2]))
            alt = 0 if row[3]=='' else float(row[3])
            altitudes = np.append(altitudes, alt)

    data = gs(times, lats, lons, altitudes)

    return data
