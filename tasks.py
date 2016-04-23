from invoke import task

from flight_genie.main import main


@task
def run(training_csv='training_data.csv',
        testing_csv='test_data.csv'):
    """Run the app by providing a csv file with flights"""
    main(training_csv, testing_csv)
