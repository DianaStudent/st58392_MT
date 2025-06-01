import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

class TestSelenium(unittest.TestCase):
```
    def setUp(self):
        driver = webdriver.Chrome()
        self.driver = driver
        self.driver.implicitly_wait(20, "seconds")
    
    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        self.driver.get("http://localhost:8080/en/")
        self.assertEqual(self.driver.title, "PrestaShop - The World's No 1 e-Commerce Solution")
        self.assertTrue(self.driver.find_element_by_name("search_query"))
        self.assertTrue(self.driver.find_element_by_name("submit-search"))
```
}

if \_\_name\_\_ == "\_\_main\_\_":
unittest.main()