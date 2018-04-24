from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class HomePageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://www.jd.com/")


    def test_search_field(self):
        #检查在页面中是否存在指定的元素
        self.assertTrue(self.is_element_present(By.ID,'key'))


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def is_element_present(self,how,what):
        try:
            self.driver.find_element(by=how,value=what)
        except NoSuchElementException:
            return False
        return True


if __name__ =="__main__":
    unittest.main(verbosity=2)