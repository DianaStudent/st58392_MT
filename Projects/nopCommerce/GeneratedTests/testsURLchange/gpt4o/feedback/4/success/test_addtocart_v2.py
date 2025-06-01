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
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        try:
            # Navigate to search page
            search_menu = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
            self.assertIsNotNone(search_menu)
            search_menu.click()

            # Type search term and submit
            search_input = self.wait.until(EC.presence_of_element_located((By.ID, "q")))
            self.assertIsNotNone(search_input)
            search_input.send_keys("book")

            search_button = self.driver.find_element(By.CSS_SELECTOR, "button.button-1.search-button")
            self.assertIsNotNone(search_button)
            search_button.click()

            # Wait for product results
            product_grid = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-grid")))
            self.assertIsNotNone(product_grid)

            # Locate and add first product to cart
            add_to_cart_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button.button-2.product-box-add-to-cart-button")
            self.assertTrue(len(add_to_cart_buttons) > 0)
            add_to_cart_buttons[0].click()

            # Wait for the success notification
            notification = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.bar-notification.success"))
            )
            self.assertIn("The product has been added to your shopping cart", notification.text)

            # Click on the shopping cart link in the notification
            cart_link = notification.find_element(By.LINK_TEXT, "shopping cart")
            self.assertIsNotNone(cart_link)
            cart_link.click()

            # Verify the presence of the expected product in the cart
            cart_items = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table.cart tbody tr")))
            self.assertTrue(any("Book1" in item.find_element(By.CSS_SELECTOR, "a.product-name").text for item in cart_items))

        except Exception as e:
            self.fail(f"Test failed due to exception: {e}")

if __name__ == "__main__":
    unittest.main()