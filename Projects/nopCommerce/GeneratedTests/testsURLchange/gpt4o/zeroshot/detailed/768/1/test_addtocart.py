import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://max/')
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click on "Search" from the main menu.
        search_menu = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        self.assertIsNotNone(search_menu, "Search menu is not present")
        search_menu.click()

        # Step 3: Type the search term "book" into the search field.
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        self.assertIsNotNone(search_input, "Search input is not present")
        search_input.send_keys("book")

        # Step 4: Submit the search.
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        self.assertTrue(search_button.is_enabled(), "Search button is not enabled")
        search_button.click()

        # Step 5: Wait for the product grid to load.
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))
        self.assertIsNotNone(product_grid, "Product grid is not present")

        # Step 6: Locate the first product result and click the "Add to cart" button.
        add_to_cart_button = product_grid.find_element(By.CLASS_NAME, "product-box-add-to-cart-button")
        self.assertTrue(add_to_cart_button.is_displayed(), "Add to cart button is not visible")
        add_to_cart_button.click()

        # Step 7: Wait for the notification bar to appear.
        notification_bar = wait.until(EC.presence_of_element_located((By.ID, "bar-notification")))
        self.assertTrue(notification_bar.is_displayed(), "Notification bar is not visible")

        # Step 8: From the notification, click the "shopping cart" link.
        cart_link = notification_bar.find_element(By.LINK_TEXT, "shopping cart")
        self.assertIsNotNone(cart_link, "Shopping cart link is not present")
        cart_link.click()

        # Step 9: On the cart page, verify that the expected product is present.
        cart_table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart")))
        self.assertIsNotNone(cart_table, "Cart table is not present")
        product_name = cart_table.find_element(By.CLASS_NAME, "product-name").text
        self.assertIn("Book1", product_name, "Expected product 'Book1' is not present in the cart")

if __name__ == "__main__":
    unittest.main()