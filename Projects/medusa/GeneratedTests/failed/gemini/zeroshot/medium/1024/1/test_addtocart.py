from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("http://localhost:8000/dk")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # 1. Open home page. (Done in setUp)

        # 2. Click on the menu button.
        try:
            menu_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']"))
            )
            menu_button.click()
        except Exception as e:
            self.fail(f"Menu button not found or not clickable: {e}")

        # 3. Click on the "Store" link.
        try:
            store_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']"))
            )
            store_link.click()
        except Exception as e:
            self.fail(f"Store link not found or not clickable: {e}")

        # 4. Click on a product image (thumbnail).
        try:
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt'] div[data-testid='product-wrapper'] div img"))
            )
            product_link.click()
        except Exception as e:
            self.fail(f"Product link not found or not clickable: {e}")

        # 5. Select a size.
        try:
            size_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='option-button']"))
            )
            size_button.click()
        except Exception as e:
            self.fail(f"Size button not found or not clickable: {e}")

        # 6. Click the "Add to Cart" button.
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart button not found or not clickable: {e}")

        # 7. Click the cart button to open the cart.
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='headlessui-popover-button-:Rrmdtt7:'] a[data-testid='nav-cart-link']"))
            )
            cart_button.click()
        except Exception as e:
            self.fail(f"Cart button not found or not clickable: {e}")

        # 8. Verify that the "GO TO CHECKOUT" button is present.
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='checkout-button'] button"))
            )
            self.assertTrue(go_to_checkout_button.is_displayed(), "Go to checkout button is not displayed")
        except Exception as e:
            self.fail(f"Go to checkout button not found: {e}")

if __name__ == "__main__":
    unittest.main()