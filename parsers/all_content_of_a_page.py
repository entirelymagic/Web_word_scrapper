import re
import requests
from collections import Counter
from bs4 import BeautifulSoup


class WebPage:
    """A class that take the HTML page or content and find the properties in it"""

    def __init__(self, page):
        if page[0:4] == 'http':
            self.page_content = requests.get(page).content
        else:
            self.page_content = page
        self.soup = BeautifulSoup(self.page_content, 'html.parser')

    @property
    def grab_title(self):
        title = self.soup.find('title')
        return title.string

    @property
    def content(self):
        return self.soup

    def _get_text_content(self):
        # kill all script and style elements
        for script in self.soup(["script", "style"]):
            script.extract()  # rip it out

        # get the entire text
        text = self.soup.get_text(separator=' ')

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())

        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text

    @property
    def get_all_words(self):
        expression = r'[a-zA-Z_]*'
        _matches = [w for w in re.findall(expression, self._get_text_content()) if w != '' and len(w) > 1]
        return _matches

    def _counter_object_of_words(self):
        _words_Counted = Counter(self.get_all_words)  # create a Counter Object
        return _words_Counted

    @property
    def most_common_words(self):
        _each_word_counted = self._counter_object_of_words().most_common()
        return _each_word_counted  # return list of words as tuple [(word1, 5), (ward2,3)

    @property
    def total_number_of_words(self):
        _number_of_words = sum(self._counter_object_of_words().values())
        return _number_of_words

    @property
    def unique_elements(self):
        _elements = sorted(self._counter_object_of_words())
        return _elements

    @property
    def significance_of_words(self):
        _significance = [t[1] / self.total_number_of_words for t in self.most_common_words]
        # will return a list of tuples, each tuple is the word, number of appearances and significance
        return _significance

    def _words_count_significance(self):
        words_count_and_significance = [
            i for i in zip(
                [a[0] for a in self.most_common_words],
                [b[1] for b in self.most_common_words],
                self.significance_of_words
            )]
        result = [w for w in words_count_and_significance]
        return result

