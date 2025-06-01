import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "http://localhost:3000/"
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        category_a_href = "/category-a"
        product_a_href = "/category-a/product-a"

        # 1. Open home page (already done in setUp)

        # 2. Click on product category
        try:
            category_a_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, f"//a[@href='{category_a_href}']"))
            )
            category_a_link.click()
        except Exception as e:
            self.fail(f"Could not click category A link: {e}")

        # 3. Select the first product
        try:
            product_a_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, f"//a[@href='{product_a_href}']"))
            )
            product_a_link.click()
        except Exception as e:
            self.fail(f"Could not click product A link: {e}")

        # 4. Click the "Add to cart" button
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'is-success') and contains(text(), 'Add to cart')]"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not click Add to cart button: {e}")

        # 5. Click the cart icon/button to open the shopping bag
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "cart-button"))
            )
            cart_button.click()
        except Exception as e:
            self.fail(f"Could not click cart button: {e}")

        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Go to checkout')]"))
            )
            self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not displayed")
        except Exception as e:
            self.fail(f"Could not find GO TO CHECKOUT button: {e}")

if __name__ == "__main__":
    unittest.main()