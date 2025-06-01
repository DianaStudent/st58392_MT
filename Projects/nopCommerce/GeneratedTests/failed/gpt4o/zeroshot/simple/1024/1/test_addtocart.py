from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        try:
            # Search for a book using the search box and submit the search
            search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
            search_box.send_keys("book")
            search_box.submit()

            # Wait for search results to be displayed and add the first item to the cart
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()

            # Verify success notification is visible and contains a link to the cart
            success_message = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success"))
            )
            self.assertIn("The product has been added to your", success_message.text)

            # Confirm the cart contains at least one item
            cart_count = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#flyout-cart .count"))
            )
            self.assertIn("1 item(s)", cart_count.text)

        except TimeoutException:
            self.fail("Test failed due to TimeoutException.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()