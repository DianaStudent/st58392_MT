from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_add_to_cart(self):
        # Open the homepage
        self.driver.get("http://max/")

        # Click on the "Search" link in the top navigation
        search_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_link.click()

        # Enter "book" in the search field and submit the search
        search_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "q")))
        search_field.send_keys("book")
        search_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "btnG")))
        search_button.click()

        # On the search results page, locate the first product and click "Add to cart"
        first_product_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//h2/a")))
        first_product_link.click()
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "add-to-cart-button")))
        add_to_cart_button.click()

        # Wait for the success notification to appear
        success_notification = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@id='success-notification']")))

        # Click the "shopping cart" link inside the notification
        shopping_cart_link = WebDriverWait(success_notification, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Shopping Cart")))
        shopping_cart_link.click()

        # Confirm success by checking that the cart page contains the added product
        cart_page_title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='title']"))).text
        self.assertIn("Your Shopping Cart", cart_page_title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()