import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # 1. Open Menu
        try:
            menu_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']"))
            )
            menu_button.click()
        except Exception as e:
            self.fail(f"Failed to click menu button: {e}")

        # 2. Go to Store
        try:
            store_link = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']"))
            )
            store_link.click()
        except Exception as e:
            self.fail(f"Failed to click store link: {e}")

        # 3. Open Product Page
        try:
            product_link = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']"))
            )
            product_link.click()
        except Exception as e:
            self.fail(f"Failed to click product link: {e}")

        # 4. Select Size
        try:
            size_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='option-button']"))
            )
            size_button.click()
        except Exception as e:
            self.fail(f"Failed to click size button: {e}")

        # 5. Add to Cart
        try:
            add_to_cart_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Failed to click add to cart button: {e}")

        # 6. Click Cart Button
        try:
            cart_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='headlessui-popover-button-:Rrmdtt7:']"))
            )
            cart_button.click()
        except Exception as e:
            self.fail(f"Failed to click cart button: {e}")

        # 7. Wait for "GO TO CHECKOUT" Button
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']"))
            )
        except Exception as e:
            self.fail(f"Failed to find 'GO TO CHECKOUT' button: {e}")

if __name__ == "__main__":
    unittest.main()