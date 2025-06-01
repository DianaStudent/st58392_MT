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
        # 1. Open home page. Already done in setUp

        # 2. Click the menu button ("Menu").
        menu_button_locator = (By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")
        try:
            menu_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(menu_button_locator))
            menu_button.click()
        except Exception as e:
            self.fail(f"Could not click the menu button: {e}")

        # 3. Click the "Store" link.
        store_link_locator = (By.CSS_SELECTOR, "a[data-testid='store-link']")
        try:
            store_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(store_link_locator))
            store_link.click()
        except Exception as e:
            self.fail(f"Could not click the store link: {e}")

        # 4. Click on a product image (Thumbnail) - first product.
        product_wrapper_locator = (By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']")
        try:
            product_wrapper = WebDriverWait(driver, 20).until(EC.presence_of_element_located(product_wrapper_locator))
            product_wrapper.click()
        except Exception as e:
            self.fail(f"Could not click the first product: {e}")

        # 5. Select size by clicking the size button "L".
        size_button_locator = (By.CSS_SELECTOR, "button[data-testid='option-button']:nth-child(1)")
        try:
            size_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(size_button_locator))
            size_button.click()
        except Exception as e:
            self.fail(f"Could not select size L: {e}")

        # 6. Add the product to the cart.
        add_to_cart_button_locator = (By.CSS_SELECTOR, "button[data-testid='add-product-button']")
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(add_to_cart_button_locator))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not add product to cart: {e}")

        # 7. Explicitly click the cart button to open the cart.
        nav_cart_link_locator = (By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")
        try:
            nav_cart_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(nav_cart_link_locator))
            nav_cart_link.click()
        except Exception as e:
            self.fail(f"Could not click the cart button: {e}")

        # 8. Verify that the "GO TO CHECKOUT" button is present.
        go_to_checkout_button_locator = (By.CSS_SELECTOR, "a[data-testid='checkout-button']")
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(go_to_checkout_button_locator))
            self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not displayed")
        except Exception as e:
            self.fail(f"GO TO CHECKOUT button is not present: {e}")

if __name__ == "__main__":
    unittest.main()