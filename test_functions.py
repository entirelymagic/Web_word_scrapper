from app import *
from unittest import TestCase


class TestFunction(TestCase):
    def db_functionality(self):
        self.assertIsNone(create_table_webpages_if_not_exist('test_db'))
        self.assertIsNone(add_to_webpages('test_db', 'this_url', 'This title'))
        self.assertIsNone(create_table_keywords_if_not_exist('test_db'))
        self.assertIsNone(add_to_keywords('test_db', 1, 'puppet', 5, 55))

    def test_web_text(self):
        test_url = 'https://books.toscrape.com/'
        page_object = WebPage(test_url)
        self.assertTrue(page_object.content, str)

    def test_web_object(self):
        books = WebPage('https://books.toscrape.com/')
        aspected1 = len(books.significance_of_words)
        aspected2 = len(books.unique_elements)
        self.assertEqual(aspected1, aspected2, 139)
