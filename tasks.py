from invoke import task

from flight_genie.main import (
    main,
    generate_plots
)

@task(help={
    'training_csv': 'Training csv values',
    'test_csv': 'Testing csv values'
})
def run(training_csv='training_data.csv',
        testing_csv='test_data.csv',
        nearest_neighbour=False,
        linear_regression=False,
        random_forrest=False,
        time_series=False):
    """Run the app by providing csv files with flights"""
    main(training_csv, testing_csv)
    if nearest_neighbour:
        raise NotImplemented()
    elif linear_regression:
        raise NotImplemented()
    elif random_forrest:
        raise NotImplemented()
    elif time_series:
        raise NotImplemented()


@task(help={
    'training_csv': 'Training csv values',
    'test_csv': 'Testing csv values'
})
def plot(training_csv='training_data.csv',
         testing_csv='test_data.csv'):
    """Task to generate all plots for method introspection"""
    generate_plots(training_csv, testing_csv)
