from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestShopiper(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())

    def tearDown(self):
        self.driver.quit()

    def test_home(self):
        self.driver.get("http://localhost/")
        WebDriverWait(self.driver, 20).until(EC.presence_of_elements_located(["header", "footer"]))
        for el in ["header", "footer", "navigation"]:
            self.assertTrue(el in [x.name.lower() for x in self.driver.find_elements_by_tag_name("div")])

    def test_tables(self):
        self.driver.get("http://localhost/category/tables")
        WebDriverWait(self.driver, 20).until(EC.presence_of_elements_located(["header", "table"]])
        for el in ["header", "table"]:
            self.assertTrue(el in [x.name.lower() for x in self.driver.find_elements_by_tag_name("div")])

    def test_chairs(self):
        self.driver.get("http://localhost/category/chairs")
        WebDriverWait(self.driver, 20).until(EC.presence_of_elements_located(["header", "table"]])
        for el in ["header", "table"]:
            self.assertTrue(el in [x.name.lower() for x in self.driver.find_elements_by_tag_name("div")])

    def test_login(self):
        self.driver.get("http://localhost/login")
        WebDriverWait(self.driver, 20).until(EC.presence_of_elements_located(["header", "form"])
```