from invoke import run, task

from flight_genie.main import main


@task
def run(csv_file):
    """Run the app by providing a csv file with flights"""
    main(csv_file)
