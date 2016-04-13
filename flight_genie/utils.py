"""Common utils for the project"""

import csv


def get_names_values_from_csv(csv_path):
    """Return a tuple of two elements - names and values of csv"""
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        rows = [r for r in csv_reader]
        names = rows[0]
        values = rows[1:]
    return names, values


def get_pairs_list_from_names_values(names, values):
    """Return a list of pairs from list of keys and list of lists of params

    e.g. names = ['a', 'b', 'c']
    values =
    return: [('a', 1), ('b', 2), ('c', 3),
             ('a', 4), ('b', 5), ('c', 6),
             ('a', 7), ('b', 8), ('c', 9)]
    """
    zipped_values = [zip(names, v) for v in values]
    return [list(v) for v in zipped_values]


def get_numerical_value(value):
    """Return a numerical value for value.

    If the passed value is a number return it.
    Otherwise return a hash over the value.
    """
    if is_number(value):
        return float(value)
    return hash(value)


def is_number(value):
    """Return if the passed value can be parsed to float."""
    try:
        float(value)
        return True
    except ValueError:
        return False


def get_value_by_key_in_pairs_list(pairs_list, key):
    """e.g. [('a': 4), ('b': 3)], 'b' -> 3"""
    for pair in pairs_list:
        if pair[0] == key:
            return pair[1]


def month_day_from_date(date):
    pass


def weekday_from_date(date):
    pass


def city_code_from_airport(airport):
    pass


def country_from_airport(airport):
    pass


def days_in_range(startdate, enddate):
    pass
