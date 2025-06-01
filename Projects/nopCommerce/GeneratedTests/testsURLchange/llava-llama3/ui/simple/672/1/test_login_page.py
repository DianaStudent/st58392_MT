import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class TestEcomerceLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_login_page(self):
        self.driver.get("http://max/login")
        self.assertTrue(".header-links .cart-qty" in self.driver.page_source)
        self.assertTrue(".block  .title" in self.driver.page_source)

    def test_register_page(self):
        self.driver.get("http://max/register")
        self.assertTrue(".block  .title" in self.driver.page_source)

    def test_search_page(self):
        self.driver.get("http://max/search")
        self.assertTrue(".block  .title" in self.driver.page_source)

if __name__ == "__main__":
    unittest.main()