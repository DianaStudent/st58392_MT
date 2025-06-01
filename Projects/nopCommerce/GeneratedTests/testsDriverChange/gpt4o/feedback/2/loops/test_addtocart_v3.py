import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.base_url = "http://max/"
        self.driver.get(self.base_url)

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click on "Search" from the main menu.
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 3: Type the search term "book" into the search field.
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book")

        # Step 4: Submit the search.
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        search_button.click()

        # Step 5: Wait for the product grid to load.
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))

        # Step 6: Locate the first product result and click the "Add to cart" button.
        first_product = product_grid.find_elements(By.CLASS_NAME, "item-box")[0]
        first_add_to_cart_button = first_product.find_element(By.CLASS_NAME, "product-box-add-to-cart-button")
        first_add_to_cart_button.click()

        # Step 7: Wait for the notification bar to appear.
        notification = wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))
        notification_text = notification.text.strip()

        # Check if notification text contains the expected message
        self.assertIn("The product has been added to your shopping cart", notification_text,
                      "Add to cart notification not found.")

        # Step 8: From the notification, click the "shopping cart" link.
        cart_link = notification.find_element(By.LINK_TEXT, "shopping cart")
        cart_link.click()

        # Step 9: On the cart page, verify that the expected product is present.
        cart_table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart")))
        product_rows = cart_table.find_elements(By.CLASS_NAME, "product-name")

        if not product_rows:
            self.fail("No product rows found in the cart.")
        
        product_row = product_rows[0]
        self.assertIn("Book1", product_row.text, "Expected product is not in the cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()