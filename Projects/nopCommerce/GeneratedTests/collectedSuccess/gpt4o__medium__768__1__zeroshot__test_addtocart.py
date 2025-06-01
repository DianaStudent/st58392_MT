import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the homepage
        driver.get("http://max/")
        
        # Step 2: Click on the "Search" link in the top navigation
        search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        if not search_link:
            self.fail("Search link not found.")
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        if not search_input:
            self.fail("Search input field not found.")
        search_input.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        if not search_button:
            self.fail("Search button not found.")
        search_button.click()

        # Step 4: On the search results page, locate the first product and click "Add to cart"
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button")))
        if not add_to_cart_button:
            self.fail("Add to cart button not found.")
        add_to_cart_button.click()

        # Step 5: Wait for the success notification to appear
        success_notification = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success")))
        if not success_notification:
            self.fail("Success notification not found.")
        
        # Step 6: Click the "shopping cart" link inside the notification
        cart_link = driver.find_element(By.LINK_TEXT, "shopping cart")
        if not cart_link:
            self.fail("Shopping cart link in notification not found.")
        cart_link.click()

        # Step 7: Confirm success by checking that the cart page contains the added product
        cart_item_count = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart tbody tr")))
        if not cart_item_count:
            self.fail("Cart does not contain any item.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()