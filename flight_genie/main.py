from scipy import spatial
from sklearn.neighbors import NearestNeighbors
import numpy

from flight_genie.flight import Flight
from flight_genie.utils import (
    get_names_values_from_csv,
    get_pairs_list_from_names_values
)


PRICE_USD = 'priceusd'


def main(csv_file):
    """Run the app passing in a file"""
    names, values = get_names_values_from_csv(csv_file)
    pairs_list = get_pairs_list_from_names_values(names, values)
    flights = [Flight(p) for p in pairs_list]
    flights_dataset = [f.to_numerical_list(excluded_attributes=[PRICE_USD])
                       for f in flights]
    neigh = NearestNeighbors(1)
    neigh.fit(list(flights_dataset))
    predicted_id = neigh.kneighbors([flights_dataset[12391]], 1,
                                    return_distance=False)[0][0]
    predicted_flight_list = flights_dataset[predicted_id]
    predicted_flight = filter(
        lambda f: f.to_numerical_list([PRICE_USD]) == predicted_flight_list,
        flights
    )
    print(next(predicted_flight).get_attribute(PRICE_USD))
