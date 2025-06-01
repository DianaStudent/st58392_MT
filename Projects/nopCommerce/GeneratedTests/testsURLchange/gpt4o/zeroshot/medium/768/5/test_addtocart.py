import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        driver.get("http://max/")

        # Step 2: Click on "Search" link in the top navigation.
        search_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Search"))
        )
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search.
        search_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "q"))
        )
        search_field.send_keys("book")
        search_field.submit()

        # Step 4: On the search results page, locate the first product and click "Add to cart".
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # Step 5: Wait for the success notification to appear.
        success_notification = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success"))
        )
        
        notification_text = success_notification.text
        self.assertIn("The product has been added to your shopping cart", notification_text, 
                      "Success notification not found in the expected format")

        # Step 6: Click the "shopping cart" link inside the notification.
        cart_link = success_notification.find_element(By.LINK_TEXT, "shopping cart")
        if cart_link:
            cart_link.click()
        else:
            self.fail("Shopping cart link is not present in the notification")

        # Step 7: Confirm success by checking that the cart page contains the added product.
        cart_item = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-name"))
        )
        if not cart_item:
            self.fail("Cart item is not present on the cart page")

        # Check if there is any product listed in the cart
        cart_count = driver.find_elements(By.CLASS_NAME, "product-name")
        self.assertTrue(len(cart_count) > 0, "Cart does not contain any items")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()