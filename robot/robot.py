import urllib.robotparser
import re


class RobotFileChecker:
    """A class that takes in a website base address
    Property check_fetch_page return true if robots.txt allows the page to be scrapped. """
    def __init__(self, page):
        self.page = page
        self.rp = urllib.robotparser.RobotFileParser()

        url = self.page
        result = re.sub(r'(.*://)?([^/?]+).*', '\g<1>\g<2>', url)
        self.rp.set_url(result + r"/robots.txt")

        self.rp.read()

    @property
    def check_fetch_page(self):
        """Check if the page is allowed to be scrapped"""
        return self.rp.can_fetch("*", self.page)
