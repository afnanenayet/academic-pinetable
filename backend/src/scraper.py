""" scraper.py contains the logic and procedure for retrieving data from the
academic timetable and parsing the table.
"""

from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd
import requests


def get_raw_http() -> str:
    """ retrieves the http source from the course website
    returns: raw http souce from timetable page
    """
    payload = "distribradio=alldistribs&depts=no_value&periods=no_value&distribs=no_value&distribs_i=no_value&distribs_wc=no_value&pmode=public&term=&levl=&fys=n&wrt=n&pe=n&review=n&crnl=no_value&classyear=2008&searchtype=Subject Area(s)&termradio=allterms&terms=no_value&subjectradio=allsubjects&hoursradio=allhours&sortorder=dept"
    req = requests.post(
        "http://oracle-www.dartmouth.edu/dart/groucho/" +
        "timetable.display_courses",
        data=payload)
    return req.text


def parse_raw_table(raw_txt: str) -> list:
    """ parses the raw HTTP into a pretty table
    """
    soup = BeautifulSoup(raw_txt, "lxml")
    divs = soup.find_all("div", {"class": "data-table"})
    div = divs[0]  # there should only be one div with this name
    table = div.find("table")

    # get length of each row so we can easily split rows
    # when parsing the table
    # header = table.find("tr")[0]
    ltable: list = []
    header_names = [th.contents[0] for th in table.find_all("th")]
    header_len = len(header_names)
    row: list = []

    for i, child in enumerate(table):
        # if child.name == "td" and child != "[]":
        #     row.append(str(child.contents))
        if i % header_len == 0 and i != 0:
            if len(row) != 19:
                print("error: row should have 19 elements, row has " +
                      f"{len(row)} elements")
            ltable.append(row)
            row = []

        # for now, put in blank placeholders to keep consistent with the
        # expected length of each row
        if child.name == "td":
            row.append(str(child.contents[0]))
        else:
            row.append("")

    df = pd.DataFrame(ltable, columns=header_names, dtype=object)
    return df
