import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dirver = webdriver.Chrome()
        cls.dirver.implicitly_wait(30)
        cls.dirver.maximize_window()
        cls.dirver.get("http://www.jd.com/")

    def test_search_by_category(self):
        print()


