from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
from flight_genie.flight import Flight
from flight_genie.utils import (
    get_names_values_from_csv,
    get_pairs_list_from_names_values,
    get_relative_error,
    get_relative_error_success_count,
    get_median_of_list,
    get_avg_of_list
)


PRICE_USD = 'priceusd'
BIN_SIZE = 128
K_NEIGHBORS = 10


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
    neigh = NearestNeighbors(1,
                             algorithm='auto',
                             radius=1.0,
                             leaf_size=30,
                             p=1,
                             metric='cityblock')
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
    """Return generator over pairs of predicted and real prices for flights"""
    training_flights_dataset = [f.to_numerical_list([PRICE_USD])
                                for f in training_flights]
    neigh_tree = get_KD_tree(training_flights_dataset)
    testing_flights_dataset = [f.to_numerical_list([PRICE_USD])
                               for f in testing_flights]
    for i, flight in enumerate(testing_flights_dataset):
        predicted_ids = neigh_tree.kneighbors([flight],
                                              K_NEIGHBORS,
                                              return_distance=False)[0]
        predicted_prices = sorted([
            training_flights[i].get_price_per_ticket()
            for i in predicted_ids
        ])
        # TODO play with K_NEIGHBORS and median vs avg
        # predicted_price = get_median_of_list(predicted_prices)
        predicted_price = get_avg_of_list(predicted_prices)
        real_price = testing_flights[i].get_price_per_ticket()
        yield predicted_price, real_price


def generate_plots(training_csv, testing_csv):
    """Make all necessary plots from testing and training CSVs"""
    training_flights, testing_flights = parse_csv(training_csv,
                                                  testing_csv)
    relative_errors = []
    prices_pair = predicted_and_real_flights_prices(training_flights,
                                                    testing_flights)
    for predicted_price, real_price in prices_pair:
        relative_error = get_relative_error(float(predicted_price),
                                            float(real_price))
        relative_errors.append(relative_error * 100)
    plt.hist(relative_errors, bins=BIN_SIZE)
    plt.ylabel('Count')
    plt.xlabel('Relative error %')
    plt.show()


def main(training_csv, testing_csv):
    """Print all predicted, real prices and relative errors"""
    training_flights, testing_flights = parse_csv(training_csv,
                                                  testing_csv)
    prices_pair = predicted_and_real_flights_prices(training_flights,
                                                    testing_flights)
    relative_errors = []
    for predicted_price, real_price in prices_pair:
        relative_errors.append(get_relative_error(float(predicted_price),
                                                  float(real_price)))

    percentage_of_all = 0
    current_perc = 5
    while percentage_of_all < 100:
        success_count = get_relative_error_success_count(relative_errors,
                                                         current_perc / 100)
        print('Flights predicted below {}% err - {}'.format(current_perc,
                                                            success_count),
              end=' ')
        percentage_of_all = (success_count / len(relative_errors)) * 100
        print('This is {}% of all'.format(percentage_of_all))
        current_perc += 5


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


if __name__ == '__main__':
    main('training_data_reworked_prices.csv', 'test_data_reworked_prices.csv')
