from scipy import spatial
import numpy

from flight_genie.flight import Flight
from flight_genie.utils import get_names_values_from_csv


def main(csv_file):
    """Run the app passing in a file"""
    csv_file = 'flights-data.csv'

    names, values = get_names_values_from_csv(csv_file)

    #
    # indexes = {}
    #
    # for i, r in enumerate(zip(*flights)):
    #     if type(r[0]) != int:
    #         index = 0
    #         for rr in r:
    #             if names[i] not in indexes:
    #                 indexes[names[i]] = {}
    #             indexes[names[i]][rr] = index
    #             index += 1
    #
    # flights_array = [flight_to_array(f, indexes, names) for f in flights]
    #
    # our_array = numpy.array(flights_array)
    #
    # our_tree = spatial.cKDTree(our_array)
    #
    # item = [
    #     '2016-03-69',
    #     '9',
    #     '4',
    #     '2016-03-80',
    #     '20',
    #     '1  ',
    #     '2016-03-73',
    #     '',
    #     '7  ',
    #     'ABQ',
    #     'ABE',
    #     'US',
    #     'GSP',
    #     'GSP',
    #     'US',
    #     'AA',
    #     'B',
    #     '1',
    #     '0',
    #     '1',
    #     '11',
    #     '2',
    #     'USD',
    #     '370.0367302',
    #     '581.6999999',
    #     'economy',
    #     'website',
    #     '0',
    #     'O Fallon',
    #     'US',
    #     'NM',
    # ]
    # ar = flight_to_array(item, indexes, names)
    # print our_tree.query(ar, k=1, distance_upper_bound=10)
