"""Common utils for the project"""

import csv
from datetime import datetime
from functools import wraps


AIRPORTS = {
    'AMS': {
        'city_code': 'NL',
        'country': 'BKK'
    },
    'BKK': {
        'city_code': 'FRA',
        'country': 'DE'
    },
    'BUR': {
        'city_code': 'BUR',
        'country': 'US'
    },
    'CNX': {
        'city_code': 'BKK',
        'country': 'TH'
    },
    'CPT': {
        'city_code': 'CPT',
        'country': 'ZA'
    },
    'CGN': {
        'city_code': 'CGN',
        'country': 'DE'
    },
    'CHQ': {
        'city_code': 'HER',
        'country': 'GR'
    },
    'CUN': {
        'city_code': 'CUN',
        'country': 'MX'
    },
    'DMK': {
        'city_code': 'BKK',
        'country': 'TH'
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
    'HAV': {
        'city_code': 'HAV',
        'country': 'CU'
    },
    'HER': {
        'city_code': 'HER',
        'country': 'GR'
    },
    'HHN': {
        'city_code': 'FRA',
        'country': 'DE'
    },
    'HKT': {
        'city_code': 'HKT',
        'country': 'TH'
    },
    'LAS': {
        'city_code': 'LAS',
        'country': 'US'
    },
    'LIS': {
        'city_code': 'BKK',
        'country': 'TH'
    },
    'LPA': {
        'city_code': 'LPA',
        'country': 'ES'
    },
    'MAD': {
        'city_code': 'MAD',
        'country': 'ES'
    },
    'MAN': {
        'city_code': 'MAN',
        'country': 'UK'
    },
    'MRU': {
        'city_code': 'MRU',
        'country': 'MU'
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
    'PMI': {
        'city_code': 'PMI',
        'country': 'ES'
    },
    'SJO': {
        'city_code': 'SJO',
        'country': 'CR'
    },
    'STR': {
        'city_code': 'STR',
        'country': 'DE'
    },
    'SYQ': {
        'city_code': 'SJO',
        'country': 'CR'
    },
    'WDH': {
        'city_code': 'WDH',
        'country': 'NA'
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
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
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
    if is_date(value):
        return timestamp_from_date(value)
    return hash(value)


def is_date(value):
    """Return if the string value is a date"""
    try:
        datetime_from_csv_col(value)
        return True
    except:
        return False


def timestamp_from_date(value):
    """Get timestamp from a string date value"""
    return datetime_from_csv_col(value).timestamp()


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
    raise ValueError('Attribute not found: {}'.format(key))


def empty_string_on_empty_input(func):
    """Decorator to return '' on empty string input

    Used for columns where data might be missing
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg.strip() == '':
                return ''
        return func(*args, **kwargs)
    return wrapper


@empty_string_on_empty_input
def month_day_from_date(date):
    """Get the day of month from a date in the csv"""
    dt = datetime_from_csv_col(date)
    return str(dt.month)


@empty_string_on_empty_input
def weekday_from_date(date):
    """Get the weekday (number from 1 to 7) from a date in the csv"""
    dt = datetime_from_csv_col(date)
    return str(dt.weekday())


@empty_string_on_empty_input
def city_code_from_airport(airport):
    """Get the city code of airport code"""
    return AIRPORTS[airport]['city_code']


@empty_string_on_empty_input
def country_from_airport(airport):
    """Get the country code from airport code"""
    return AIRPORTS[airport]['country']


@empty_string_on_empty_input
def days_in_range(start_date, end_date):
    """Get the number of days between two columns in the csv"""
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


def get_relative_error(approximation, real):
    """Return the relative error of two values"""
    return abs(approximation - real) / real


def get_relative_error_success_count(relative_errors, threshold=0.05):
    """Return the count of the errors below a threshold"""
    return len(list(filter(lambda x: x <= threshold, relative_errors)))


def get_median_of_list(lst):
    """Return the median element of a sorted list"""
    ln = len(lst)
    div_by_2 = int(ln / 2)
    if ln % 2 == 0:
        return (lst[div_by_2 - 1] + lst[div_by_2]) / 2
    return lst[div_by_2]


def get_avg_of_list(lst):
    """Return the average of a list"""
    return sum(lst) / len(lst)
