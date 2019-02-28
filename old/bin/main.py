"""

Module main.py

Create a heatmap using Google Map interface for a set of GPS coordinates.

The path is labelled using a marker giving the starting time of the path,
the total length of the path, and the total time of the path.

Multiple source files can be plotted on the sample map, making a heatmap
showing different routes and their relative popularity.

Inspired by the Strava Global Heatmaps.

Behaviour:
 * If given a directory, will create a heatmap and marker label for all
    files ending in ".gs"

 * If given a single file, it will create a map and marker for just the
    data in that file

------------------------------------------------------------------------
Command Line Interface:

Required:
 *  file: absolute or relative path to a file or directory containing map files
 *  map_name: absolute or relative path to the save location for the map
        html file

Optional:
 *  height (-H): Change the zoom level on the resulting map (default: 14)
 *  width (-w): Change the radius of the heatmap markers (default: 5)

"""

import argparse
import os

from . import read
from . import plot

_mod_description = """
    Generate Google Map html file for a path of gps coordinates.

    Calculates distance travelled
    """

_file_help = "File path to the gps csv file"
_map_help = "File path to output file"

_def_height = 14
_def_width = 5

def main():
    parser = argparse.ArgumentParser(description=_mod_description)

    parser.add_argument('file', help=_file_help)
    parser.add_argument('map_name', help=_map_help)
    parser.add_argument('-H', '--height', default = _def_height, type=float)
    parser.add_argument('-w', '--width', default = _def_width, type=int)

    args = parser.parse_args()

    if os.path.isdir(args.file):
        log_files = [os.path.abspath(os.path.join(args.file, f)) for f in os.listdir(args.file) if os.path.splitext(f)[1] == '.gs']
        data = [read.gps(f) for f in log_files]

        if data == []:
            raise IOError("No '.gs' files were found. Try again")
    else:
        log_files = args.file
        data = read.gps(log_files)
    html_map = plot.draw(data, args.map_name, args.height, args.width)
    print("Map saved as %s" % html_map)

if __name__ == '__main__':
    main()
