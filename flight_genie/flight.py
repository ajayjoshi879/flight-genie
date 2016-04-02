"""All single flight related functionalities and representations"""


class Flight(object):
    """Simple representation of a flight. Just containing properties"""

    def __init__(self, **params):
        """Sets the flight properties from a dict

        For now it just does __setattr__ for all.
        """
        for name, val in params.iteritems():
            self.__setattr__(name, val)

    def to_array(self):
        """Return an array of values by a certain order."""
        return [val for name, val in enumerate(self.__dict__)]

    def to_array_without_price(self):
        """Return an array of values missing the price"""
        return Flight.to_array()
