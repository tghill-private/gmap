"""

    read.py

    Parse gpx files to retrieve lat, lon coordinates. Compute distance along path

"""

from xml.etree import ElementTree
import numpy as np

import distance
import _template




def write(datafile, outfile):
    tree = ElementTree.parse(datafile)
    root = tree.getroot()
    trk = root[1]
    trkseg = root[1][1]

    times = ""
    coords = ""
    lats = []
    lons = []
    alts = []
    for point in trkseg:
        lat = float(point.get('lat'))
        lon = float(point.get('lon'))
        lats.append(lat)
        lons.append(lon)

        alt = float(point[0].text)
        alts.append(alt)

        time = point[1].text

        timestr = _template.time.format(dtime=time)
        times += timestr

        coordstr = _template.coord.format(lat=lat, lon=lon, alt=alt)
        coords += coordstr

    alts = np.array(alts)
    print(alts)
    dalt = alts[1:] - alts[:-1]
    up = np.sum(dalt[dalt>0])
    down = np.sum(dalt[dalt<0])

    dist = distance.path_length(lats, lons)
    description = "Path length: %.3f km\nElevation change: %.1f m" % ((dist/1.e3), up)
    kmlstring = _template.document.format(times=times, coords=coords, desc=description)

    with open(outfile, 'w') as out:
        out.write(kmlstring)

if __name__ == '__main__':
    datafile = '../data/sample_file.gpx'
    write(datafile, '../data/sample_out.kml')
