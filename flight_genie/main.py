from sklearn.neighbors import NearestNeighbors

from flight_genie.flight import Flight
from flight_genie.utils import (
    get_names_values_from_csv,
    get_pairs_list_from_names_values
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


def main(training_csv, testing_csv):
    """Run the app passing in a training and testing file"""
    flights = get_flights_list_from_csv(training_csv,
                                        Flight)
    flights_dataset = [f.to_numerical_list([PRICE_USD])
                       for f in flights]
    neigh_tree = get_KD_tree(flights_dataset)

    testing_flights = get_flights_list_from_csv(testing_csv,
                                                Flight.get_from_core_data)
    testing_flights_dataset = [f.to_numerical_list()
                               for f in testing_flights]
    for i, flight in enumerate(testing_flights_dataset):
        predicted_id = neigh_tree.kneighbors([flight],
                                             1,
                                             return_distance=False)[0][0]
        predicted_flight_list = flights_dataset[predicted_id]
        predicted_flight = filter(
            lambda f: f.to_numerical_list([PRICE_USD]) == predicted_flight_list,
            flights
        )
        print(testing_flights[i], end=' $')
        print(next(predicted_flight).get_attribute(PRICE_USD))
