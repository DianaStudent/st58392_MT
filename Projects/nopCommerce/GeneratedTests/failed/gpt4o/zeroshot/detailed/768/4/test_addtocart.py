from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = self.wait

        # Click on 'Search' from the main menu
        search_menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_menu.click()

        # Type the search term 'book' into the search field
        search_input = wait.until(EC.element_to_be_clickable((By.ID, "q")))
        search_input.send_keys("book")

        # Submit the search
        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button-1.search-button")))
        search_button.click()

        # Wait for the product grid to load
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))

        # Locate the first product result and click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Wait for the notification bar to appear
        notification = wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))

        # Check if the notification bar contains the message and link to the shopping cart
        notification_text = notification.text
        self.assertIn("The product has been added to your shopping cart", notification_text)

        cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # On the cart page, verify that the expected product is present
        cart_count = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "count"))).text
        self.assertIn("1 item(s)", cart_count)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()