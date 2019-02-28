"""

Module distance.py


Computes great-circle distance between two points (lat/lon), as
well as the total length of a path of lat/lon paris

"""

import numpy as np

# Radius of the Earth in meters
R_e = 6.371e6

def _distance_to(lat_0, lon_0, lat_1, lon_1):
    """distance_to calculates the great-circle distance between two points

    distance_to uses the haversine formula
        (https://en.wikipedia.org/wiki/Haversine_formula)
    to calculate the great-circle distance between the input
    lat/lon coordinates


    The input coordinates are in degrees; latitudes range from
    -90 to 90 degrees, and longitudes range from -180 to 180
    degrees.

    No checks are made to check the validity of the arguments.
    """
    degrees = (lat_0, lon_0, lat_1, lon_1)
    lat0, lon0, lat1, lon1 = np.radians(degrees)
    phi = 0.5 * (lat1 - lat0)
    lambd = 0.5 * (lon1 - lon0)

    h = (np.sin(phi))**2 + (np.cos(lat0) * np.cos(lat1) * (np.sin(lambd))**2)

    d = 2 * R_e * np.arcsin( np.sqrt(h) )

    return d

def path_length(lats, lons):
    """Computes the total path length for the set of latitude and longitudes"""
    distance = sum([_distance_to(lats[i], lons[i], lats[i+1], lons[i+1]) for i in range(len(lats)-1)])
    return distance
