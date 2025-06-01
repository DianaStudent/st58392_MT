from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Navigate to the "Search" page
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Type "book" in the search field and submit
        search_field = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_field.send_keys("book")
        search_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-button")))
        search_button.click()

        # Wait for the product grid to load
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))

        # Locate the first product and click "Add to cart"
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # Wait for the notification bar
        notification_bar = wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))

        # Verify the notification contains a link to the cart
        shopping_cart_link = notification_bar.find_element(By.LINK_TEXT, "shopping cart")
        if not shopping_cart_link:
            self.fail("The success notification did not contain a link to the shopping cart.")

        # Click the "shopping cart" link in the notification
        shopping_cart_link.click()

        # Verify the cart page contains the expected product
        cart_count = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".count a")))
        self.assertIn("1 item(s)", cart_count.text, "The cart does not contain the expected number of items.")

        # Check the product name in the cart
        product_name = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-name")))
        self.assertIn("Book1", product_name.text, "The expected product is not present in the cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()