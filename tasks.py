import sys
from invoke import task

from flight_genie.main import (
    main,
    plot_data
)


@task(help={'method': "Name of the person to say hi to.",
            'training_csv': "Training csv values"})
def run(training_csv='training_data.csv',
        testing_csv='test_data.csv',
        nearest_neighbour=False,
        linear_regression=False,
        random_forrest=False,
        time_series=False):
    """Run the app by providing csv files with flights"""
    main(training_csv, testing_csv)
    if nearest_neighbour:
        pass
    elif linear_regression:
        pass
    elif random_forrest:
        pass
    elif time_series:
        pass
