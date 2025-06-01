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

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # 1. Open home page.
        self.assertEqual(driver.current_url, "http://localhost:8000/dk/")

        # 2. Click on the menu button.
        menu_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']"))
        )
        if menu_button:
            menu_button.click()
        else:
            self.fail("Menu button not found")

        # 3. Click on the "Store" link.
        store_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']"))
        )
        if store_link:
            store_link.click()
        else:
            self.fail("Store link not found")

        # 4. Click on a product image (thumbnail).
        product_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']"))
        )
        if product_link:
            product_link.click()
        else:
            self.fail("Product link not found")

        # 5. Select a size.
        size_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='option-button']"))
        )
        if size_button:
            size_button.click()
        else:
            self.fail("Size button not found")

        # 6. Click the "Add to Cart" button.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
        )
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found")

        # 7. Click the cart button to open the cart.
        cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='headlessui-popover-button-:Rrmdtt7:']"))
        )
        if cart_button:
            cart_button.click()
        else:
            self.fail("Cart button not found")

        # 8. Verify that the "GO TO CHECKOUT" button is present.
        go_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']"))
        )
        if go_to_checkout_button:
            pass  # Success!
        else:
            self.fail("Go to checkout button not found")

if __name__ == "__main__":
    unittest.main()