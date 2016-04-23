"""All single flight related functionalities and representations"""

from flight_genie.utils import (
    get_value_by_key_in_pairs_list,
    get_numerical_value,
    month_day_from_date,
    weekday_from_date,
    country_from_airport,
    city_code_from_airport,
    days_in_range,
)


class Flight(object):
    """Simple representation of a flight. Just containing properties"""

    PARAMETERS = (
        'date',
        'dayofmonth',
        'weekday',
        'outbounddate',
        'outbounddayofmonth',
        'outboundweekday',
        'inbounddate',
        'inbounddayofmonth',
        'inboundweekday',
        'originairport',
        'origincitycode',
        'origincountry',
        'destinationairport',
        'destinationcitycode',
        'destinationcountry',
        'carriercode',
        'carriertype',
        'adults',
        'children',
        'daystodeparture',
        'dayslengthofstay',
        'platform',
        'isota'
    )

    def __init__(self, pairs_list):
        """Sets the flight properties from a list of pairs"""
        self.__pairs_list = pairs_list

    @classmethod
    def get_from_core_data(cls, pairs_list):
        """Get a full flight from the core data

        Infers the values of some parameters. See README for more details
        """
        full_pairs_list = []
        current_parameters = [p[0] for p in pairs_list]
        for param in cls.PARAMETERS:
            if param in current_parameters:
                param_val = get_value_by_key_in_pairs_list(pairs_list, param)
            else:
                inferring_dict = cls.INFERRING_FUNCTIONS[param]
                core_vals = (get_value_by_key_in_pairs_list(pairs_list, c)
                             for c in inferring_dict['core'])
                param_val = inferring_dict['function'](*[v for v in core_vals])
            full_pairs_list.append((param, param_val))
        return cls(full_pairs_list)

    def get_attribute(self, attr_name):
        """Gets the value of a atributed labels attr_name"""
        return get_value_by_key_in_pairs_list(self.__pairs_list, attr_name)

    def to_numerical_list(self, excluded_attributes=[]):
        """Return an array of values by a certain order."""
        return list(map(get_numerical_value,
                        [v[1] for v in self.__pairs_list
                         if v[0] not in excluded_attributes]))

    def __str__(self):
        """A good representation as a string"""
        return 'FROM: {}, TO: {}, ON: {}'.format(self.get_attribute('originairport'),
                                                 self.get_attribute('destinationairport'),
                                                 self.get_attribute('outbounddate'))

    INFERRING_FUNCTIONS = {
        'dayofmonth': {
            'core': ['date'],
            'function': month_day_from_date
        },
        'weekday': {
            'core': ['date'],
            'function': weekday_from_date
        },
        'outbounddayofmonth': {
            'core': ['outbounddate'],
            'function': month_day_from_date
        },
        'outboundweekday': {
            'core': ['outbounddate'],
            'function': weekday_from_date
        },
        'inbounddayofmonth': {
            'core': ['inbounddate'],
            'function': month_day_from_date
        },
        'inboundweekday': {
            'core': ['inbounddate'],
            'function': weekday_from_date
        },
        'origincitycode': {
            'core': ['originairport'],
            'function': city_code_from_airport
        },
        'origincountry': {
            'core': ['originairport'],
            'function': country_from_airport
        },
        'destinationcitycode': {
            'core': ['destinationairport'],
            'function': city_code_from_airport
        },
        'destinationcountry': {
            'core': ['destinationairport'],
            'function': country_from_airport
        },
        'daystodeparture': {
            'core': ['date', 'outbounddate'],
            'function': days_in_range
        },
        'dayslengthofstay': {
            'core': ['outbounddate', 'inbounddate'],
            'function': days_in_range
        },
    }
