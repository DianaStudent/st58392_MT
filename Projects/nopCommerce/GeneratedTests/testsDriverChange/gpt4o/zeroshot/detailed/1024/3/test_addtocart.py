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
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Step 1: Navigate to the homepage
        driver.get("http://max/")

        # Step 2: Click on "Search" from the main menu
        search_menu_item = self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Search"))
        )
        search_menu_item.click()

        # Step 3: Type the search term "book" into the search field
        search_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        self.assertTrue(search_input.is_displayed())
        search_input.send_keys("book")

        # Step 4: Submit the search
        search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-box-button")
        search_button.click()

        # Step 5: Wait for the product grid to load
        product_grid = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-grid div.item-grid"))
        )

        # Check that the product grid is displayed and not empty
        products = product_grid.find_elements(By.CSS_SELECTOR, "div.product-item")
        self.assertGreater(len(products), 0)

        # Step 6: Locate the first product result and click the "Add to cart" button
        first_product_add_to_cart = products[0].find_element(By.CSS_SELECTOR, "button.button-2.product-box-add-to-cart-button")
        first_product_add_to_cart.click()

        # Step 7: Wait for the notification bar to appear "The product has been added to your shopping cart"
        notification = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.bar-notification.success"))
        )
        self.assertIn("The product has been added to your shopping cart", notification.text)

        # Step 8: From the notification, click the "shopping cart" link
        cart_link = notification.find_element(By.LINK_TEXT, "shopping cart")
        cart_link.click()

        # Step 9: On the cart page, verify that the expected product is present
        cart_items = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table.cart tbody tr"))
        )
        self.assertTrue(cart_items.is_displayed())
        self.assertGreater(len(driver.find_elements(By.CSS_SELECTOR, "td.product")), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()