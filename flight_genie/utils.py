"""Common utils for the project"""

import csv
from datetime import datetime


AIRPORTS = {
    'AMS': {
        'city_code': 'NL',
        'country': 'BKK'
    },
    'BKK': {
        'city_code': 'FRA',
        'country': 'DE'
    },
    'CGN': {
        'city_code': 'CGN',
        'country': 'DE'
    },
    'DUS': {
        'city_code': 'DUS',
        'country': 'DE'
    },
    'FRA': {
        'city_code': 'FRA',
        'country': 'DE'
    },
    'HAJ': {
        'city_code': 'HAJ',
        'country': 'DE'
    },
    'HAM': {
        'city_code': 'HAM',
        'country': 'DE'
    },
    'HHN': {
        'city_code': 'FRA',
        'country': 'DE'
    },
    'MAD': {
        'city_code': 'MAD',
        'country': 'ES'
    },
    'MAN': {
        'city_code': 'MAN',
        'country': 'UK'
    },
    'MUC': {
        'city_code': 'MUC',
        'country': 'DE'
    },
    'NRN': {
        'city_code': 'DUS',
        'country': 'DE'
    },
    'OAK': {
        'city_code': 'OAK',
        'country': 'US'
    },
    'STR': {
        'city_code': 'STR',
        'country': 'DE'
    }
}


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
    dt = datetime_from_csv_col(date)
    return str(dt.month)


def weekday_from_date(date):
    dt = datetime_from_csv_col(date)
    return str(dt.weekday)


def city_code_from_airport(airport):
    return AIRPORTS[airport]['city_code']


def country_from_airport(airport):
    return AIRPORTS[airport]['country']


def days_in_range(start_date, end_date):
    start_datetime = datetime_from_csv_col(start_date)
    end_datetime = datetime_from_csv_col(end_date)
    delta = end_datetime - start_datetime
    return str(delta.days)


def datetime_from_csv_col(col):
    """Return datetime from passed csv col in format  MM/DD/YY """
    date_fields = col.split('/')
    month = int(date_fields[0])
    day = int(date_fields[1])
    year = int("20" + date_fields[2])
    return datetime(year, month, day)
