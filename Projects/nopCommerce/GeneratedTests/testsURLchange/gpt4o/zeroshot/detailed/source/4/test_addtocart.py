from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver

        # Step 1: Navigate to the homepage
        try:
            driver.find_element(By.LINK_TEXT, "Home page")
        except:
            self.fail("Home page link is missing")

        # Step 2: Click on "Search" from the main menu
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except:
            self.fail("Search link is missing or not clickable")

        # Step 3: Type the search term "book" into the search field
        try:
            search_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_field.send_keys("book")
        except:
            self.fail("Search input field is missing")

        # Step 4: Submit the search
        try:
            search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-button")
            search_button.click()
        except:
            self.fail("Search button is missing")

        # Step 5: Wait for the product grid to load
        try:
            first_product = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-item"))
            )
        except:
            self.fail("Product grid did not load or first product is missing")

        # Step 6: Locate the first product result and click "Add to cart"
        try:
            add_to_cart_button = first_product.find_element(By.CSS_SELECTOR, "button.product-box-add-to-cart-button")
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button is missing on the first product")

        # Step 7: Wait for the notification bar
        try:
            notification = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.bar-notification.success"))
            )
            cart_link = notification.find_element(By.LINK_TEXT, "shopping cart")
        except:
            self.fail("Success notification or cart link is missing")

        # Step 8: Click the "shopping cart" link
        cart_link.click()

        # Step 9: Verify that the expected product is present in the cart
        try:
            cart_item = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.item.first"))
            )
            product_name = cart_item.find_element(By.CSS_SELECTOR, "div.product-name").text
            self.assertTrue(product_name, "Product name is empty, expected Book1")
        except:
            self.fail("Expected product 'Book1' is not present in the cart")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()