"""All single flight related functionalities and representations"""

from flight_genie.utils import get_numerical_value


class Flight(object):
    """Simple representation of a flight. Just containing properties"""

    def __init__(self, pairs_list):
        """Sets the flight properties from a list of pairs"""
        self.__pairs_list = pairs_list

    def get_attribute(self, attribute_name):
        """Gets the value of a atributed labels attribute_name"""
        pair = filter(lambda x: x[0] == attribute_name, self.__pairs_list)
        return next(pair)[1]

    def to_numerical_list(self, excluded_attributes=[]):
        """Return an array of values by a certain order."""
        return list(map(get_numerical_value,
                        [v[1] for v in self.__pairs_list
                         if v[0] not in excluded_attributes]))
