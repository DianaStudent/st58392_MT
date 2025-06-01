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

    def tearDown(self):
        self.driver.quit()

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
        search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-button")
        search_button.click()

        # Step 4: Locate the first product and click "Add to cart".
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.button-2.product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # Step 5: Wait for the success notification to appear.
        notification = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.bar-notification.success"))
        )

        # Step 6: Click the "shopping cart" link inside the notification.
        cart_link = notification.find_element(By.LINK_TEXT, "shopping cart")
        cart_link.click()

        # Step 7: Confirm success by checking that the cart contains at least one item.
        cart_items = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.count"))
        )

        self.assertIsNotNone(cart_items, "Cart items element not found.")
        item_count_text = cart_items.text
        self.assertIn("1 item(s)", item_count_text, "Cart does not contain the expected number of items.")

if __name__ == "__main__":
    unittest.main()