from selenium import webdriver
import unittest
import time
from selenium.webdriver.support import expected_conditions as EC


class Login(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("https://passport.cnblogs.com/user/signin")

    def test_login(self):
        try:
            account_ele =self.driver.find_element_by_id("input1")
            account_ele.send_keys("purplefang")
            psw_ele = self.driver.find_element_by_id("input2")
            psw_ele.send_keys("juan0828..")

            submit_ele = self.driver.find_element_by_id("signin")
            submit_ele.click()

            time.sleep(3)

            locator = ("id","lnk_current_user")
            result = EC.text_to_be_present_in_element(locator,"purplefang")(self.driver)
            self.assertFalse(result)
        except Exception as msg:
            print ("异常原因%s"%msg)

