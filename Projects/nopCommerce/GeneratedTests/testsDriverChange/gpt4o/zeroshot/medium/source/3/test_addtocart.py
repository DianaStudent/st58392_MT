import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        driver.get("http://max/")

        # Step 2: Click on the "Search" link in the top navigation
        search_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Search"))
        )
        self.assertTrue(search_link, "Search link not found")
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search
        search_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "q"))
        )
        self.assertTrue(search_field, "Search field not found")
        search_field.send_keys("book")

        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        self.assertTrue(search_button, "Search button not found")
        search_button.click()

        # Step 4: Locate the first product and click "Add to cart"
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".item-box:first-child .product-box-add-to-cart-button"))
        )
        self.assertTrue(add_to_cart_button, "Add to cart button not found")
        add_to_cart_button.click()

        # Step 5: Wait for the success notification to appear
        success_notification = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#bar-notification .success"))
        )
        self.assertTrue(success_notification, "Success notification not displayed")

        # Step 6: Click the "shopping cart" link inside the notification
        cart_link = success_notification.find_element(By.LINK_TEXT, "shopping cart")
        self.assertTrue(cart_link, "Shopping cart link not found inside the notification")
        cart_link.click()

        # Step 7: Confirm success by checking that the cart page contains the added product
        cart_item = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart .product-name"))
        )
        self.assertTrue(cart_item, "No items found in the cart")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()