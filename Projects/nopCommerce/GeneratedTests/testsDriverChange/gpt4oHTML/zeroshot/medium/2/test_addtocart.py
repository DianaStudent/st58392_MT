import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # Use the actual homepage URL

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage - already done in setUp

        # Step 2: Click on the "Search" link in the top navigation
        search_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
        )
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search
        search_input = wait.until(
            EC.presence_of_element_located((By.ID, "q"))
        )
        search_input.send_keys("book")
        search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-button")
        search_button.click()

        # Step 4: On the search results page, locate the first product and click "Add to cart"
        add_to_cart_buttons = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.button-2.product-box-add-to-cart-button"))
        )
        if not add_to_cart_buttons:
            self.fail("No 'Add to cart' buttons found on the search results page.")
        first_add_to_cart_button = add_to_cart_buttons[0]
        first_add_to_cart_button.click()

        # Step 5: Wait for the success notification to appear
        notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.bar-notification.success"))
        )
        notification_text = notification.find_element(By.CSS_SELECTOR, "p.content")
        if not notification_text or "shopping cart" not in notification_text.text:
            self.fail("Success notification is not visible or does not contain expected text.")

        # Step 6: Click the "shopping cart" link inside the notification
        cart_link = notification_text.find_element(By.LINK_TEXT, "shopping cart")
        cart_link.click()

        # Step 7: Confirm success by checking that the cart page contains the added product
        cart_count = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.mini-shopping-cart .count"))
        )
        if not cart_count or "1 item(s)" not in cart_count.text:
            self.fail("Cart does not contain the expected product after adding to cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()