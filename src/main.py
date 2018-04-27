""" This is the main entrypoint for the pinetable backend.  It contains basic
routing information for querying. This should _only_ contain basic routing
information and wrappers for functions in other files and must be as minimal
as possible.
"""

from flask import Flask
from scraper import get_raw_http, parse_raw_table
import pandas as pd
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

app = Flask(__name__)
data_cache: pd.DataFrame = None
scheduler = BackgroundScheduler()


@app.route("/")
def class_table():
    """ Returns the full course table in a JSON file format
    """
    global data_cache
    if data_cache is not None:
        return str(data_cache.to_json())
    return ""


def refresh_data():
    """ pulls data from webpage using scraper, then updates global variable
    """
    global data_cache
    print("Retrieving HTTP...")
    txt = get_raw_http()
    print("...retrieved.")
    print("Parsing...")
    data_cache = parse_raw_table(txt)
    print("...parsed.")


def init():
    """ Wrapper initialization function

    Initially parse the data and store it in the data cache variable. Set up
    timed background daemon to refresh the data at a given interval.
    """
    scheduler.start()
    scheduler.add_job(
        func=refresh_data,
        trigger=IntervalTrigger(days=1),
        id="refresh_data_job",
        name="pull data from course academic timetable",
        replace_existing=True,
    )
    atexit.register(lambda: scheduler.shutdown())
    # delay launching the app until there is some data available
    refresh_data()


if __name__ == "__main__":
    init()
    app.run()
