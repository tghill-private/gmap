"""

Module dtime.py

Parses time strings into datetime.datetime instances

"""

import datetime as dt

_fmt = '%Y-%m-%dT%H:%M:%S:%f'

def strptime(t):
    """
    Parses a time string into a datetime object
    """
    t_processed = t[:-5] + ':' + t[-4:-1] + '000'
    return dt.datetime.strptime(t_processed, _fmt)
