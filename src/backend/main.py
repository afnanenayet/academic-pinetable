""" This is the main entrypoint for the pinetable backend.  It contains basic
routing information for querying. This should _only_ contain basic routing
information and wrappers for functions in other files and must be as minimal
as possible.
"""

from flask import Flask
app = Flask(__name__)


@app.route("/")
def class_table():
    """ Returns the full course table
    """
    # TODO
    return "TODO"


if __name__ == "__main__":
    app.run()
