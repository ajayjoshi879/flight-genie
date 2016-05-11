import itertools
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
from flight_genie.flight import Flight
from flight_genie.utils import (
    get_names_values_from_csv,
    get_pairs_list_from_names_values,
    get_relative_error
)


PRICE_USD = 'priceusd'


def get_flights_list_from_csv(data_csv,
                              flight_constructor):
    """Get a list of flights from csv file"""
    names, values = get_names_values_from_csv(data_csv)
    pairs_list = get_pairs_list_from_names_values(names, values)
    flights = [flight_constructor(p) for p in pairs_list]
    return flights


def get_KD_tree(flights_dataset):
    """Get the KD tree from the csv

    Used mostly with training_csv
    """
    neigh = NearestNeighbors(1)
    neigh.fit(list(flights_dataset))
    return neigh


def parse_csv(training_csv, testing_csv):
    """Return a tuple of lists - train flights, test flights"""
    training_flights = get_flights_list_from_csv(training_csv,
                                                 Flight)
    testing_flights = get_flights_list_from_csv(testing_csv,
                                                Flight.get_from_core_data)
    return training_flights, testing_flights


def predicted_and_real_flights_prices(training_flights, testing_flights):
    training_flights_dataset = [f.to_numerical_list([PRICE_USD])
                                for f in training_flights]
    neigh_tree = get_KD_tree(training_flights_dataset)
    testing_flights_dataset = [f.to_numerical_list([PRICE_USD])
                               for f in testing_flights]
    for i, flight in enumerate(testing_flights_dataset):
        predicted_id = neigh_tree.kneighbors([flight],
                                             1,
                                             return_distance=False)[0][0]
        predicted_flight_list = training_flights_dataset[predicted_id]
        predicted_flight = filter(
            lambda f:
                f.to_numerical_list([PRICE_USD]) == predicted_flight_list,
            training_flights
        )
        predicted_price = next(predicted_flight).get_attribute(PRICE_USD)
        real_price = testing_flights[i].get_attribute(PRICE_USD)
        yield predicted_price, real_price


def plot(training_csv, testing_csv):
    training_flights, testing_flights = parse_csv(training_csv,
                                                  testing_csv)
    first_100_prices = []
    first_100_errors = []
    prices_pair = predicted_and_real_flights_prices(training_flights,
                                                    testing_flights)
    for i in range(100):
        predicted_price, real_price = next(prices_pair)
        first_100_prices.append(float(predicted_price))
        relative_error = get_relative_error(float(predicted_price),
                                            float(real_price))
        first_100_errors.append(relative_error)
    plt.hist(first_100_errors, bins=100)
    plt.show()


def main(training_csv, testing_csv):
        plot(training_csv, testing_csv)


# def main(training_csv, testing_csv):
#     """Run the app passing in a training and testing file"""
#     training_flights = get_flights_list_from_csv(training_csv,
#                                                  Flight)
#     training_flights_dataset = [f.to_numerical_list([PRICE_USD])
#                                 for f in training_flights]
#     neigh_tree = get_KD_tree(training_flights_dataset)
#
#     testing_flights = get_flights_list_from_csv(testing_csv,
#                                                 Flight.get_from_core_data)
#     testing_flights_dataset = [f.to_numerical_list([PRICE_USD])
#                                for f in testing_flights]
#     for i, flight in enumerate(testing_flights_dataset):
#         predicted_id = neigh_tree.kneighbors([flight],
#                                              1,
#                                              return_distance=False)[0][0]
#         predicted_flight_list = training_flights_dataset[predicted_id]
#         predicted_flight = filter(
#             lambda f:
#                 f.to_numerical_list([PRICE_USD]) == predicted_flight_list,
#             training_flights
#         )
#         predicted_price = next(predicted_flight).get_attribute(PRICE_USD)
#         real_price = testing_flights[i].get_attribute(PRICE_USD)
#
#         print(testing_flights[i], end=' ')
#         print('Predicted: ${} '.format(predicted_price), end=' ')
#         print('Real: ${}'.format(real_price))
#

def plot_data():
    raise NotImplemented()


def linear_regression():
    raise NotImplemented()


def random_forest():
    raise NotImplemented()


def nearest_neighbour():
    raise NotImplemented()


def time_series():
    raise NotImplemented()
