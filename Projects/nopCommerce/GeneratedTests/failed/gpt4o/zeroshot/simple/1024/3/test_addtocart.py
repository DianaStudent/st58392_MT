from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver

        # Search for a book using the search box and submit the search
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_box.send_keys("book")
        except Exception as e:
            self.fail(f"Search box not found: {str(e)}")

        try:
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
            search_button.click()
        except Exception as e:
            self.fail(f"Search button not found: {str(e)}")

        # Wait for the search results to be visible
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-item"))
            )
        except Exception as e:
            self.fail(f"Search results not loaded: {str(e)}")

        # Add the first book to the cart
        try:
            add_to_cart_button = driver.find_elements(By.CLASS_NAME, "product-box-add-to-cart-button")[0]
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart button not found: {str(e)}")

        # Verify that the success notification is visible and contains a link to the cart
        try:
            success_notification = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "bar-notification"))
            )
            cart_link = success_notification.find_element(By.TAG_NAME, "a")
            self.assertIn("shopping cart", cart_link.get_attribute("href"))
        except Exception as e:
            self.fail(f"Success notification not found or incorrect: {str(e)}")

        # Confirm that the cart contains at least one item
        try:
            cart_count = WebDriverWait(driver, 20).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "count"), "1 item(s)")
            )
            self.assertTrue(cart_count)
        except Exception as e:
            self.fail(f"Cart does not contain the expected number of items: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()