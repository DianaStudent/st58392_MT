from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestSearchBook(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_search_book(self):
        # Open the homepage
        self.driver.get("http://max/")

        # Click on the "Search" link in the top navigation
        search_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Search']")))
        search_link.click()

        # Enter "book" in the search field and submit the search
        search_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "search_query")))
        search_field.send_keys("book")
        search_field.send_keys(Keys.RETURN)

        # On the search results page, locate the first product and click "Add to cart"
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']")))
        add_to_cart_button.click()

        # Wait for the success notification to appear
        success_notification = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Success')]")))

        # Click the "shopping cart" link inside the notification
        cart_link = WebDriverWait(success_notification, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Shopping Cart']")))
        cart_link.click()

        # Confirm success by checking that the cart page contains the added product
        cart_page = self.driver.current_url
        cart_contents = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='cart-contents']")))

        if not cart_contents.text:
            self.fail("Cart contents is empty")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()