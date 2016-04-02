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

def get_dicts_from_names_values(names, values):
    """Return a list of dicts from list of keys and list of lists of params

    TODO: Change to ordered dict.
    e.g. names = ['a', 'b', 'c']
    values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return: [{'a': 1, 'b': 2, 'c': 3},
             {'a': 4, 'b': 5, 'c': 6},
             {'a': 7, 'b': 8, 'c': 9}]
    """
    keys_values_pairs = [zip(names, v) for v in values]
    return [{f[0]: f[1] for f in v} for v in keys_values_pairs]
