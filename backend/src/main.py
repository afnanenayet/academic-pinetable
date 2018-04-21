""" This is the main entrypoint for the pinetable backend.  It contains basic
routing information for querying. This should _only_ contain basic routing
information and wrappers for functions in other files and must be as minimal
as possible.
"""

from flask import Flask
from scraper import get_raw_http, parse_raw_table
import pandas as pd

app = Flask(__name__)
data_cache: pd.DataFrame = None


@app.route("/")
def class_table():
    """ Returns the full course table in a JSON file format
    """
    print("retrieving http...")
    txt = get_raw_http()
    print("retrieved!")
    print("parsing table...")
    df = parse_raw_table(txt)
    print("parsed!")
    return str(df.to_json())


def init():
    """ Wrapper initialization function

    Initially parse the data and store it in the data cache variable. Set up
    timed background daemon to refresh the data at a given interval.
    """
    pass


if __name__ == "__main__":
    app.run()
