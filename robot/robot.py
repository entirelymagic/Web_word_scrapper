import urllib.robotparser, requests
import re


class RobotFileChecker:
    """A class that takes in a website base address
    Property check_fetch_page return true if robots.txt allows the page to be scrapped. """
    def __init__(self, page):
        self.page = page
        self.rp = urllib.robotparser.RobotFileParser()

        url = self.page
        self.__result = re.sub(r'(.*://)?([^/?]+).*', '\g<1>\g<2>', url)
        self.rp.set_url(self.__result + r"/robots.txt")
        self.rp.read()

    @property
    def check_fetch_page(self):
        """Check if the page is allowed to be scrapped or if the robots.txt page exits.
        If the robots.txt page does not exits it will considered as allowed"""
        request = requests.get(self.__result + r"/robots.txt")
        if request.status_code == 200:
            return self.rp.can_fetch("*", self.page)
        else:
            return True
