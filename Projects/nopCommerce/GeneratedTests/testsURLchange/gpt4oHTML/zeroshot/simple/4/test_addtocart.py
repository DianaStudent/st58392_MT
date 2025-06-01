import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # Replace with the actual base URL

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Search for a book
        try:
            search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
            search_box.send_keys("book")
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
            search_button.click()
        except Exception as e:
            self.fail(f"Failed at searching for a product: {e}")

        # Add the first search result to the cart
        try:
            add_to_cart_buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-box-add-to-cart-button")))
            add_to_cart_buttons[0].click()
        except Exception as e:
            self.fail(f"Failed at adding a product to cart: {e}")

        # Verify success notification and link
        try:
            success_notification = wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))
            self.assertIn("The product has been added to your", success_notification.text)
            link_to_cart = success_notification.find_element(By.LINK_TEXT, "shopping cart")
            self.assertTrue(link_to_cart.is_displayed())
        except Exception as e:
            self.fail(f"Success notification or cart link is not visible: {e}")

        # Confirm the cart contains at least one item
        try:
            driver.get(link_to_cart.get_attribute('href'))
            mini_cart_count = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".count a")))
            cart_items_count_text = mini_cart_count.text
            self.assertTrue(int(cart_items_count_text.split()[0]) > 0, "Cart should contain at least one item.")
        except Exception as e:
            self.fail(f"Verification of items in the cart failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()