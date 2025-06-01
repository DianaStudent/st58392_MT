import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Click on the "Search" link in the top navigation
        search_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Search")))
        self.assertTrue(search_link, "Search link is not found.")
        search_link.click()

        # Step 2: Enter "book" in the search field and submit the search
        search_input = wait.until(EC.visibility_of_element_located((By.ID, "q")))
        self.assertTrue(search_input, "Search input is not found.")
        search_input.send_keys("book")

        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-button")))
        self.assertTrue(search_button, "Search button is not found.")
        search_button.click()

        # Step 3: On the search results page, locate the first product and click "Add to cart"
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        self.assertTrue(add_to_cart_button, "Add to cart button is not found.")
        add_to_cart_button.click()

        # Step 4: Wait for the success notification to appear
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success")))
        self.assertTrue(success_notification, "Success notification is not found.")

        # Step 5: Click the "shopping cart" link inside the notification
        cart_link = wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, "shopping cart")))
        self.assertTrue(cart_link, "Shopping cart link in the notification is not found.")
        cart_link.click()

        # Step 6: Confirm success by checking that the cart contains the added product
        cart_items = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".items")))
        self.assertTrue(cart_items, "Cart items are not displayed.")
        self.assertGreater(len(cart_items.find_elements(By.CLASS_NAME, "item")), 0, "No items in the cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()