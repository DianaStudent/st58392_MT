import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        driver.get("http://max/")

        # Step 2: Click on the "Search" link in the top navigation
        search_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Search"))
        )
        self.assertIsNotNone(search_link, "Search link is not available")
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search
        search_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "q"))
        )
        self.assertIsNotNone(search_input, "Search input is not available")
        search_input.clear()
        search_input.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "button-1.search-button")
        search_button.click()

        # Step 4: Locate the first product and click "Add to cart"
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-box-add-to-cart-button"))
        )
        self.assertIsNotNone(add_to_cart_button, "Add to cart button is not available")
        add_to_cart_button.click()

        # Step 5: Wait for the success notification to appear
        success_notification = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success"))
        )
        self.assertIsNotNone(success_notification, "Success notification is not available")

        # Step 6: Click the "shopping cart" link inside the notification
        shopping_cart_link = success_notification.find_element(By.LINK_TEXT, "shopping cart")
        self.assertIsNotNone(shopping_cart_link, "Shopping cart link in notification is missing")
        shopping_cart_link.click()

        # Step 7: Confirm success by checking that the cart page contains the added product
        cart_item = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product"))
        )
        self.assertIsNotNone(cart_item, "Cart does not contain any items")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()