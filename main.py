from scipy import spatial
import numpy
import csv


def flight_to_array(f, indexes, names):
    index = 0
    array = []
    for c in f:
        if type(c) == int:
            array.append(c)
        else:
            array.append(indexes[names[index]][c])
        index += 1
    return array

if __name__ == '__main__':
    with open('sample_exits.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        rows = [r for r in csv_reader]
        names = rows[0]
        flights = rows[1:]

    indexes = {}

    for i, r in enumerate(zip(*flights)):
        if type(r[0]) != int:
            index = 0
            for rr in r:
                if names[i] not in indexes:
                    indexes[names[i]] = {}
                indexes[names[i]][rr] = index
                index += 1

    flights_array = [flight_to_array(f, indexes, names) for f in flights]

    our_array = numpy.array(flights_array)

    our_tree = spatial.cKDTree(our_array)

    item = [
        '2016-03-69',
        '9',
        '4',
        '2016-03-80',
        '20',
        '1  ',
        '2016-03-73',
        '',
        '7  ',
        'ABQ',
        'ABE',
        'US',
        'GSP',
        'GSP',
        'US',
        'AA',
        'B',
        '1',
        '0',
        '1',
        '11',
        '2',
        'USD',
        '370.0367302',
        '581.6999999',
        'economy',
        'website',
        '0',
        'O Fallon',
        'US',
        'NM',
    ]
    ar = flight_to_array(item, indexes, names)
    print our_tree.query(ar, k=1, distance_upper_bound=10)
