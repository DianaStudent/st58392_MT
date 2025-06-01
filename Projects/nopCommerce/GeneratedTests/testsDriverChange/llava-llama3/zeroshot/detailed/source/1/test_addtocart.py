```
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.element import By
from selenium.webdriver.support.assertions import Assert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class TestBookSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://max/"
        self.search_term = "book"
        self.wait_time = 20

    def tearDown(self):
        self.driver.quit()

    def test_search_book(self):
        # Navigate to the homepage.
        self.driver.get(self.url)

        # Click on  "Search" from the main menu.
        search_button = WebDriverWait(self.driver, self.wait_time).until \
            (By.XPATH, "//button[contains(text(), 'Search')]"))
        search_button.click()

        # Type the search term  "book" into the search field.
        search_field = WebDriverWait(self.driver, self.wait_time).until \
            (By.XPATH, "//input[contains(@name,'query_string'])][1]")
        self.driver.find_element_by_name("query_string").send_keys(self.search_term)

        # Submit the search.
        submit_button = WebDriverWait(self.driver, self.wait_time).until \
            (By.XPATH, "//button[contains(text(), 'Search')])[2]")
        submit_button.click()

        # Wait for the product grid to load.
        WebDriverWait(self.driver, self.wait_time).until \
            (lambda x: len(x.find_elements_by_tag_name("li")) > 0)

        # Locate the first product result and click the  "Add to cart" button.
        product_result = WebDriverWait(self.driver, self.wait_time).until \
            (By.XPATH, "//a[contains(text(),'{self.search_term}')][2]")
        add_to_cart_button = product_result.find_element_by_tag_name("button")
        add_to_cart_button.click()

        # Wait for the notification bar to appear  "The product has been added to your shopping cart".
        WebDriverWait(self.driver, self.wait_time).until \
            (By.XPATH, "//div[contains(text(),'{self.search_term}')][1]")

        # From the notification, click the  "shopping cart" link.
        shopping_cart_link = WebDriverWait(self.driver, self.wait_time).until \
            (By.XPATH, "//a[contains(text(),'The product has been added to your shopping cart')][2]")
        shopping_cart_link.click()

        # On the cart page, verify that the expected product is present.
        product_in_cart = WebDriverWait(self.driver, self.wait_time).until \
            (By.XPATH, "//div[contains(@class,'product-item')][1]")

        assert product_in_cart, "The first product is not in the shopping cart."

if __name__ == '__main__':
    unittest.main()
```