import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # 1. Open the homepage. (Done in setUp)

        # 2. Click on the "Search" link in the top navigation.
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except Exception as e:
            self.fail(f"Failed to click search link: {e}")

        # 3. Enter "book" in the search field and submit the search.
        try:
            search_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_field.send_keys("book")

            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-button"))
            )
            search_button.click()
        except Exception as e:
            self.fail(f"Failed to enter search term and submit: {e}")

        # 4. On the search results page, locate the first product and click "Add to cart".
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Failed to click add to cart button: {e}")

        # 5. Wait for the success notification to appear.
        try:
            notification = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "bar-notification"))
            )
            self.assertTrue(notification.is_displayed(), "Notification is not displayed")
        except Exception as e:
            self.fail(f"Failed to find success notification: {e}")

        # 6. Click the "shopping cart" link inside the notification.
        try:
            cart_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='bar-notification']//a[text()='shopping cart']"))
            )
            cart_link.click()
        except Exception as e:
            self.fail(f"Failed to click shopping cart link in notification: {e}")

        # 7. Confirm success by checking that the cart page contains the added product.
        try:
            cart_table = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "cart"))
            )
            self.assertTrue(cart_table.is_displayed(), "Cart table is not displayed")

            cart_items = driver.find_elements(By.XPATH, "//table[@class='cart']/tbody/tr")
            self.assertTrue(len(cart_items) > 0, "No items found in the cart")
        except Exception as e:
            self.fail(f"Failed to verify cart contents: {e}")

if __name__ == "__main__":
    unittest.main()