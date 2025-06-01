import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_add_to_cart_process(self):
        driver = self.driver

        # Wait for search box, search for 'book', and submit search
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_box.send_keys("book")
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
            search_button.click()
        except Exception as e:
            self.fail(f"Search box interact failed: {str(e)}")

        # Wait for search result and add first book to the cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart failed: {str(e)}")

        # Check success notification and cart link
        try:
            success_notification = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "bar-notification.success"))
            )
            cart_link = success_notification.find_element(By.TAG_NAME, "a")
            self.assertIn("/cart", cart_link.get_attribute("href"))
        except Exception as e:
            self.fail(f"Success notification check failed: {str(e)}")

        # Go to cart and verify items
        try:
            cart_link.click()
            cart_count = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "mini-shopping-cart"))
            )
            self.assertIn("1 item(s)", cart_count.text)
        except Exception as e:
            self.fail(f"Cart verification failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()