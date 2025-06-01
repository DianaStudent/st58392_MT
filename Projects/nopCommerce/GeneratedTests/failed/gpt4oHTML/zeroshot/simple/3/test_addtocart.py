from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # Assuming the base URL is http://max

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Locate the search input box on the home page and enter 'book'
        try:
            search_box = wait.until(presence_of_element_located((By.ID, 'small-searchterms')))
            search_box.send_keys('book')
        except Exception as e:
            self.fail(f"Search box not found: {str(e)}")

        # Click search button
        try:
            search_button = wait.until(element_to_be_clickable((By.CSS_SELECTOR, 'button.button-1.search-box-button')))
            search_button.click()
        except Exception as e:
            self.fail(f"Search button not found: {str(e)}")

        # Wait for search results and click 'Add to cart' for the first product
        try:
            add_to_cart_button = wait.until(element_to_be_clickable((By.CSS_SELECTOR, '.product-box-add-to-cart-button')))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"'Add to cart' button not found: {str(e)}")

        # Check that the success notification is visible
        try:
            success_notification = wait.until(presence_of_element_located((By.CSS_SELECTOR, '.bar-notification.success')))
            self.assertIn("The product has been added to your", success_notification.text)
            cart_link = success_notification.find_element(By.TAG_NAME, 'a')
            cart_link.click()
        except Exception as e:
            self.fail(f"Success notification or cart link not found: {str(e)}")

        # Confirm success by checking the cart contains at least one item
        try:
            cart_count = wait.until(presence_of_element_located((By.CSS_SELECTOR, '.mini-shopping-cart .count a')))
            items_in_cart_text = cart_count.text.split()[0]  # Get number of items
            self.assertTrue(int(items_in_cart_text) > 0, "Cart contains no items.")
        except Exception as e:
            self.fail(f"Cart count not verified: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()