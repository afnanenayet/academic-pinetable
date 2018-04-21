""" This is the main entrypoint for the pinetable backend.  It contains basic
routing information for querying. This should _only_ contain basic routing
information and wrappers for functions in other files and must be as minimal
as possible.
"""

from flask import Flask
from scraper import get_raw_http, parse_raw_table
import pandas as pd

app = Flask(__name__)


@app.route("/")
def class_table():
    """ Returns the full course table
    """
    print("retrieving http...")
    txt = get_raw_http()
    print("retrieved!")
    print("parsing table...")
    table_txt = parse_raw_table(txt)
    print("parsed!")
    return str(table_txt)


if __name__ == "__main__":
    app.run()
