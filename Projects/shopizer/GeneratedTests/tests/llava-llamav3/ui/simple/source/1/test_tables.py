```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys

class TestShopifier(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver")

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        self.driver.get("http://localhost/")
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements(["header", "button"]))
            self.assertTrue(self.driver.current_url == "http://localhost/")
            self.assertTrue(self.driver.find_element_by_css_selector("header"))
            self.assertTrue(self.driver.find_element_by_css_selector("button"))
        except Exception as e:
            print("Test failed: Home page")
            self.fail(e)

    def test_tables_page(self):
        self.driver.get("http://localhost/category/tables")
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements(["header", "button"]))
            self.assertTrue(self.driver.current_url == "http://localhost/category/tables")
            self.assertTrue(self.driver.find_element_by_css_selector("header"))
            self.assertTrue(self.driver.find_element_by_css_selector("button"))
        except Exception as e:
            print("Test failed: Tables page")
            self.fail(e)

    def test_chairs_page(self):
        self.driver.get("http://localhost/category/chairs")
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements(["header", "button"]))
            self.assertTrue(self.driver.current_url == "http://localhost/category/chairs")
            self.assertTrue(self.driver.find_element_by_css_selector("header"))
            self.assertTrue(self.driver.find_element_by_css_selector("button"))
        except Exception as e:
            print("Test failed: Chairs page")
            self.fail(e)

    def test_login_page(self):
        self.driver.get("http://localhost/login")
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements(["header", "form"]))
            self.assertTrue(self.driver.current_url == "http://localhost/login")
            self.assertTrue(self.driver.find_element_by_css_selector("header"))
            self.assertTrue(self.driver.find_element_by_css_selector("form"))
        except Exception as e:
            print("Test failed: Login page")
            self.fail(e)

    def test_register_page(self):
        self.driver.get("http://localhost/register")
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements(["header", "form"]))
            self.assertTrue(self.driver.current_url == "http://localhost/register")
            self.assertTrue(self.driver.find_element_by_css_selector("header"))
            self.assertTrue(self.driver.find_element_by_css_selector("form"))
        except Exception as e:
            print("Test failed: Register page")
            self.fail(e)

if __name__ == '__main__':
    unittest.main()
```