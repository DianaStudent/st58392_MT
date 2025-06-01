import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")

    def test_add_to_cart_process(self):
        driver = self.driver
        
        # Step 1: Open home page
        driver.get("http://localhost:3000/")
        
        # Step 2: Click on product category
        try:
            category_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']"))
            )
            category_link.click()
        except Exception:
            self.fail("Category link not found or not clickable.")
        
        # Step 3: Select the first product
        try:
            product_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']"))
            )
            product_link.click()
        except Exception:
            self.fail("Product link not found or not clickable.")

        # Step 4: Click the "Add to cart" button
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'button-addtocart')]"))
            )
            add_to_cart_button.click()
        except Exception:
            self.fail("Add to Cart button not found or not clickable.")

        # Step 5: Click the cart icon/button to open the shopping bag
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'cart-button')]"))
            )
            cart_button.click()
        except Exception:
            self.fail("Cart button not found or not clickable.")

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/checkout']"))
            )
            assert go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not displayed."
        except Exception:
            self.fail("GO TO CHECKOUT button not present in the cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()