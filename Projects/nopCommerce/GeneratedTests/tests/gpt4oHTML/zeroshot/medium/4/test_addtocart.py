import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage
        driver.get("http://max/")
        try:
            home_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header-logo a img")))
            self.assertIsNotNone(home_page, "Home page logo not found.")
        except:
            self.fail("Failed to open homepage or element not found.")

        # Step 2: Click on the "Search" link in the top navigation
        try:
            search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
            search_link.click()
        except:
            self.fail("Failed to find or click the search link.")

        # Step 3: Enter "book" in the search field and submit the search
        try:
            search_box = wait.until(EC.presence_of_element_located((By.ID, "q")))
            search_box.clear()
            search_box.send_keys("book")
            search_button = driver.find_element(By.CSS_SELECTOR, ".button-1.search-button")
            search_button.click()
        except:
            self.fail("Failed to perform search or elements not found.")

        # Step 4: On the search results page, locate the first product and click "Add to cart"
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".item-box:first-child .product-box-add-to-cart-button")))
            add_to_cart_button.click()
        except:
            self.fail("Failed to find Add to cart button or element not clickable.")

        # Step 5: Wait for the success notification to appear
        try:
            success_notification = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".bar-notification.success .content")))
            self.assertIsNotNone(success_notification, "Success notification not found.")
        except:
            self.fail("Failed to receive success notification.")

        # Step 6: Click the "shopping cart" link inside the notification
        try:
            cart_link = driver.find_element(By.LINK_TEXT, "shopping cart")
            cart_link.click()
        except:
            self.fail("Failed to click shopping cart link in notification.")

        # Step 7: Confirm success by checking that the cart page contains the added product
        try:
            cart_items = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart .product-name a")))
            self.assertIsNotNone(cart_items, "Cart does not contain any items.")
        except:
            self.fail("Failed to verify cart contains the added product or elements missing.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()