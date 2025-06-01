import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # 1. Open the homepage. (Done in setUp)

        # 2. Click on the "Search" link in the top navigation.
        search_link_locator = (By.LINK_TEXT, "Search")
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(search_link_locator)
            )
            search_link.click()
        except Exception as e:
            self.fail(f"Search link not found or not clickable: {e}")

        # 3. Enter "book" in the search field and submit the search.
        search_field_locator = (By.ID, "small-searchterms")
        search_button_locator = (By.CLASS_NAME, "button-1.search-box-button")
        try:
            search_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(search_field_locator)
            )
            search_field.send_keys("book")
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(search_button_locator)
            )
            search_button.click()
        except Exception as e:
            self.fail(f"Search field or button not found: {e}")

        # 4. On the search results page, locate the first product and click "Add to cart".
        add_to_cart_button_locator = (By.CLASS_NAME, "button-2.product-box-add-to-cart-button")
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(add_to_cart_button_locator)
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart button not found or not clickable: {e}")

        # 5. Wait for the success notification to appear.
        success_notification_locator = (By.ID, "bar-notification")
        try:
            success_notification = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(success_notification_locator)
            )
            self.assertTrue(success_notification.is_displayed(), "Success notification is not displayed.")
        except Exception as e:
            self.fail(f"Success notification not found: {e}")

        # 6. Click the "shopping cart" link inside the notification.
        shopping_cart_link_locator = (By.XPATH, "//div[@id='bar-notification']//a[contains(@href, '/cart')]")
        try:
            shopping_cart_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(shopping_cart_link_locator)
            )
            shopping_cart_link.click()
        except Exception as e:
            self.fail(f"Shopping cart link in notification not found or not clickable: {e}")

        # 7. Confirm success by checking that the cart page contains the added product.
        cart_table_locator = (By.CLASS_NAME, "cart")
        try:
            cart_table = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(cart_table_locator)
            )
            self.assertTrue(cart_table.is_displayed(), "Cart table is not displayed.")
            cart_items = driver.find_elements(By.XPATH, "//table[@class='cart']/tbody/tr")
            self.assertTrue(len(cart_items) > 0, "No items found in the cart.")
        except Exception as e:
            self.fail(f"Cart table not found or empty: {e}")


if __name__ == "__main__":
    unittest.main()