# from pinetable.scraper import *
from scraper import *


class TestScraper(object):
    def test_get_raw_http(self):
        """ Test the `get_raw_http` method by seeing if the HTTP can be
        pulled from the page.
        """
        txt = get_raw_http()
        assert len(txt > 0)

    def parse_raw_table(self):
        pass
