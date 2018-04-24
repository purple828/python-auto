import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):
    #在所有用例执行时，只打开一次浏览器
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://www.jd.com/")

    def test_search_by_category(self):
        #找到搜索框并输入要搜索的内容  phones
        self.searchEle = self.driver.find_element_by_id("key")
        self.searchEle.clear()
        self.searchEle.send_keys("phones")
        #找到搜索按钮
        searchXpath = '//div[@id="search"]/div/div[2]/button'
        self.searchButton = self.driver.find_element_by_xpath(searchXpath)
        self.searchButton.click()

        # 获取页面所有商品的 <a>标签ַ
        products = self.driver.find_elements_by_xpath("//div[@class='p-img']/a")
        self.assertGreater(len(products), 3, "more than 3~~")


    def test_search_by_name(self):
        #找到搜索框并输入要搜索的内容  phones
        self.searchEle = self.driver.find_element_by_id("key")
        self.searchEle.clear()
        self.searchEle.send_keys("android")
        #找到搜索按钮
        searchXpath = '//div[@id="search"]/div/div[2]/button'
        self.searchButton = self.driver.find_element_by_xpath(searchXpath)
        self.searchButton.click()

        # 获取页面所有商品的 <a>标签ַ
        products = self.driver.find_elements_by_xpath("//div[@class='p-img']/a")
        self.assertGreater(len(products), 3, "more than 3~~")


    @classmethod
    def tearDownClass(cls):
        # close
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)




