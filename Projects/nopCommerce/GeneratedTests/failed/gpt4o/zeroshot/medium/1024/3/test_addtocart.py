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
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage - Already performed in setUp()

        # Step 2: Click on the "Search" link in the top navigation
        search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search
        search_field = wait.until(EC.element_to_be_clickable((By.ID, "q")))
        search_field.send_keys("book")

        search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.search-button")))
        search_button.click()

        # Step 4: Locate the first product and click "Add to cart"
        add_to_cart_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.button-2.product-box-add-to-cart-button")
        ))
        add_to_cart_button.click()

        # Step 5: Wait for the success notification
        success_notification = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.bar-notification.success")
        ))
        self.assertIn("The product has been added to your", success_notification.text)

        # Step 6: Click the "shopping cart" link inside the notification
        cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # Step 7: Confirm success by checking that the cart page contains the added product
        item_count = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='count']"))
        )
        self.assertIsNotNone(item_count)
        self.assertNotEqual(item_count.text.strip(), "")
        self.assertIn("1 item(s)", item_count.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()