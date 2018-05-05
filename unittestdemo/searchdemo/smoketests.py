import unittest
from SearchTests import SearchTests
from homepagetests import HomePageTest
import HTMLTestRunner

search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

unittest.TextTestRunner(verbosity=2).run(smoke_tests)









