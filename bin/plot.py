"""

Module plot.py

Generate the html file with the heatmap plotted over Google Map.

Module creates the html map given parsed gps files. Can be given
a single file representation of a list of file representations.

--------------------------------------------------------------

Arguments:
 *  data: one or list of read.gs objects.
 *  fname: str giving file path to save generated file as
 *  height: zoom level of the resulting map
 *  radius: Marker radius for the final map

Raises:
 *  No forced exceptions; will raise exceptions if they are encountered

Returns:
 *  The file path to the created file
"""

import os

import numpy as np
import gmplot

from . import distance
from . import labels

def draw(data, fname, height, radius):

    if hasattr(data, '__iter__'):
        # Center map of mean latitude and mean longitude
        c = (np.mean(data[0].latitudes), np.mean(data[0].longitudes))

        # Create map instance
        map = gmplot.GoogleMapPlotter(c[0],c[1], height)

        for logfile in data:
            # Plot heatmap of latitudes and longitudes
            map.heatmap(logfile.latitudes, logfile.longitudes, radius = radius)

            label = map.marker(logfile.latitudes[0],
                        logfile.longitudes[0], title = logfile.marker)

        map.draw(fname)

    else:
        draw([data], fname, height, radius)

    return os.path.abspath(fname)
