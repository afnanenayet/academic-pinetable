""" scraper.py contains the logic and procedure for retrieving data from the
academic timetable and parsing the table.
"""

from bs4 import BeautifulSoup
from tqdm import tqdm
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

    # find the right table
    final_table = None

    divs = soup.find_all("div", {"class": "data-table"})
    print(f"len divs: {len(divs)}")

    div = divs[0]
    table = div.find("table")
    ltable = []
    children = div.contents
    print(f"len div->children: {len(children)}")
    row = []

    for child in table:
        print(f"child name: {child.name}")
        if child.name == "td" and child != "[]":
            row.append(str(child.contents))

        # finish row, reset temp row variable
        if child.name == "tr":
            ltable.append(row)
            row = []

    ltable.append(row)
    # print(ltable)
    return ltable
