```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class TestProductSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_product_search(self):
        # Step 1: Open the home page
        driver = self.driver
        driver.get("https://www.example.com")

        # Step 2: Click on the "Search" link
        search_link = driver.find_element_by_name("search")
        action = ActionChains(driver)
        action.move_to_element(search_link).click().perform()

        # Step 3: Enter "book" in the search field and submit the search
        search_input = driver.find_element_by_name("search\_field")
        search_input.send_keys("book")
        WebDriverWait(driver, 20).until(EC.element\_to\_be\_visible(search\_input))
        driver.find\_element(by\_name("search\_button")).click()

        # Step 4: Wait for the search results to load
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
```