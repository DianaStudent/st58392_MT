import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # Step 1: Open the homepage
        driver.get("data:text/html;charset=utf8," + html_data['home'])
        
        # Step 2: Click on the "Search" link in the top navigation
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except:
            self.fail("Search link not found or failed to click.")
        
        # Step 3: Enter "book" in the search field and submit the search
        try:
            driver.get("data:text/html;charset=utf8," + html_data['search_page'])
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_box.send_keys("book")
            search_button = driver.find_element(By.CLASS_NAME, "search-button")
            search_button.click()
        except:
            self.fail("Search interaction failed.")
        
        # Step 4: On the search results page, locate the first product and click "Add to cart"
        try:
            driver.get("data:text/html;charset=utf8," + html_data['search_results'])
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart interaction failed.")

        # Step 5: Wait for the success notification to appear
        try:
            driver.get("data:text/html;charset=utf8," + html_data['after_add_to_cart'])
            success_notification = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "bar-notification"))
            )
            self.assertIn("shopping cart", success_notification.text)
        except:
            self.fail("Success notification not found or incorrect.")

        # Step 6: Click the "shopping cart" link inside the notification
        try:
            cart_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "shopping cart"))
            )
            cart_link.click()
        except:
            self.fail("Shopping cart link in notification not found or failed to click.")
        
        # Step 7: Confirm success by checking that the cart page contains the added product
        try:
            driver.get("data:text/html;charset=utf8," + html_data['cart_page'])
            cart_items = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "cart"))
            )
            self.assertGreater(len(cart_items.find_elements(By.CLASS_NAME, "item")), 0)
        except:
            self.fail("Cart does not contain any items or cart page interaction failed.")

if __name__ == "__main__":
    unittest.main()