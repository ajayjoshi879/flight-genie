from scipy import spatial
import numpy


airports = ['paris',
            'sofia',
            'moscow',
            'prague',
            'frankfurt',
            'london',
            'amsterdam']

flights = [
    {
        'duration': 5,
        'from': 'london',
        'to': 'paris',
        'price': 400
    },
    {
        'duration': 4,
        'from': 'amsterdam',
        'to': 'paris',
        'price': 409
    },
    {
        'duration': 6,
        'from': 'london',
        'to': 'sofia',
        'price': 500
    },
    {
        'duration': 5,
        'from': 'prague',
        'to': 'paris',
        'price': 900
    },
    {
        'duration': 3,
        'from': 'frankfurt',
        'to': 'paris',
        'price': 1400
    },
    {
        'duration': 9,
        'from': 'london',
        'to': 'moscow',
        'price': 4001
    }
]

def flight_to_array(f):
    return [f['duration'], airports.index(f['from']), airports.index(f['to'])]


if __name__ == '__main__':
    our_array = numpy.array(map(flight_to_array, flights))
    our_tree = spatial.cKDTree(our_array)
    item = {
        'duration': 4,
        'from': 'moscow',
        'to': 'paris'
    }
    print flights[our_tree.query(flight_to_array(item), k=1, distance_upper_bound=10)[1]]['price']
