import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.alert import Alert
from selenium.webdriver.support.ui import Alerts

class TestWebsiteTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20, "time")

    def tearDown(self):
        self.driver.quit()

    def test_website(self):
        try:
            self.driver.get("http://localhost/")
            self.assertEqual(self.driver.title, "shopper")
            self.assertTrue(self.driver.find_element_by_name("shopper"))
            self.assertTrue(self.driver.find_element_by_name("tables"))
            self.assertTrue(self.driver.find_element_by_name("chairs"))
            self.assertTrue(self.driver.find_element_by_name("login"))
            self.assertTrue(self.driver.find_element_by_name("register"))

        except Exception as e:
            print(e)
            self.fail(e)

if __name__ == "__main__":
    unittest.main()