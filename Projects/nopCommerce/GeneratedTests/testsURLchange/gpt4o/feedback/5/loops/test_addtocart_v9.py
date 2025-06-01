import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver

        try:
            # Step 1: Navigate to the homepage
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "header"))
            )

            # Step 2: Click on "Search" from the main menu
            search_menu = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Search"))
            )
            search_menu.click()

            # Step 3: Type the search term "book" into the search field
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_input.send_keys("book")

            # Step 4: Submit the search
            search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-button")
            search_button.click()

            # Step 5: Wait for the product grid to load
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )

            # Step 6: Locate the first product result and click the "Add to cart" button
            add_to_cart_buttons = driver.find_elements(By.CSS_SELECTOR, "button.button-2.product-box-add-to-cart-button")
            if not add_to_cart_buttons:
                self.fail("Add to cart buttons not found")
            add_to_cart_buttons[0].click()

            # Step 7: Wait for the notification bar to appear
            notification_bar = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "bar-notification"))
            )
            content_elements = notification_bar.find_elements(By.CLASS_NAME, "content")
            if not content_elements:
                self.fail("Notification content not found")
            
            notification_text = content_elements[0].text
            if "The product has been added to your shopping cart" not in notification_text:
                self.fail("Success notification not found or incorrect")

            # Step 8: From the notification, click the "shopping cart" link
            cart_link = notification_bar.find_element(By.LINK_TEXT, "shopping cart")
            cart_link.click()

            # Step 9: On the cart page, verify that the expected product is present
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "shopping-cart-page"))
            )

            cart_items = driver.find_elements(By.CLASS_NAME, "product-name")
            if not cart_items:
                self.fail("Cart is empty, expected at least one item.")
            self.assertIn("Book1", cart_items[0].text, "Expected product 'Book1' not found in cart.")

        except Exception as e:
            self.fail(f"Test failed due to exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()