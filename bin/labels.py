"""

Module labels.py

Contains marker class to format path labels.

Formats the markers for each path with the start time, total length,
and total time.

"""

class marker:
    """
    Formats the markers for a single path from a gs object

    Arguments:
    *  data: gs instance, the path we are intersted in creating a marker
            label for
    """
    def __init__(self, data):
        self.distance = data.total_distance
        self.time = time
        self.first_time = first_time

        label = r"%s\nDistance: %.3f km\nTotal Time: %s" %(
        self.first_time, self.distance/1000., self.time)

        self.label = label

    def __repr__(self):
        return "marker(self.distance, self.time)"

    def __str__(self):
        return self.label
