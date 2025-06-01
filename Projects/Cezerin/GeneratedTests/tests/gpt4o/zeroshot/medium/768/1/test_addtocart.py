from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver

        # Step 1: Open home page (already done in setUp)
        
        # Step 2: Click on product category
        category_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cat-parent a[href='/category-a']"))
        )
        if not category_link:
            self.fail("Category link not found.")

        category_link.click()

        # Step 3: Select the first product
        first_product_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']"))
        )
        if not first_product_link:
            self.fail("First product link not found.")

        first_product_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".button-addtocart button"))
        )
        if not add_to_cart_button:
            self.fail("Add to cart button not found.")

        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button"))
        )
        if not cart_button:
            self.fail("Cart button not found.")

        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']"))
        )
        if not go_to_checkout_button:
            self.fail("Go to checkout button not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()