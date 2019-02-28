"""

Module dtime.py

Parses time strings into datetime.datetime instances and write strings
in KML format

"""

import datetime as dt

_read_fmt = '%Y-%m-%dT%H:%M:%S:%f'
_write_fmt = '%Y-%m-%dT%H:%M:%SZ'
def parsetime(t):
    """
    Parses a time string into a datetime object
    """
    t_processed = t[:-5] + ':' + t[-4:-1] + '000'
    return dt.datetime.strptime(t_processed, _read_fmt)

def writetime(t):
    """
    Write datetime object to time string
    """
    return dt.datetime.strftime(t, _write_fmt)
