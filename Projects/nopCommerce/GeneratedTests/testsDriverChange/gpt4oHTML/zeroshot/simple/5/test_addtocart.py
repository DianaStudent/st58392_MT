import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # Change this to the correct URL
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = self.wait

        # Search for a book
        try:
            search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
            search_box.send_keys("book")
            
            search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button-1")))
            search_button.click()
        except Exception as e:
            self.fail(f"Search box or button not found: {str(e)}")

        # Find and click add to cart button for the first product
        try:
            add_to_cart_buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-box-add-to-cart-button")))
            add_to_cart_buttons[0].click()
        except Exception as e:
            self.fail(f"Add to cart button not found: {str(e)}")

        # Check the success notification
        try:
            success_notification = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "bar-notification.success"))
            )
            self.assertIn("The product has been added to your shopping cart", success_notification.text)
            cart_link = success_notification.find_element(By.LINK_TEXT, "shopping cart")
            cart_link.click()
        except Exception as e:
            self.fail(f"Success notification or cart link not found: {str(e)}")

        # Verify cart contents
        try:
            cart_items_count = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".mini-shopping-cart .count a")))
            self.assertTrue(int(cart_items_count.text.split()[0]) > 0)
        except Exception as e:
            self.fail(f"Cart item count verification failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()