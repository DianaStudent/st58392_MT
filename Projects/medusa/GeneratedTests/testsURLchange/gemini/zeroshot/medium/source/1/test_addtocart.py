import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8000/dk")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # 1. Click on the menu button.
        menu_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']"))
        )
        if menu_button:
            menu_button.click()
        else:
            self.fail("Menu button not found")

        # 2. Click on the "Store" link.
        store_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']"))
        )
        if store_link:
            store_link.click()
        else:
            self.fail("Store link not found")

        # 3. Click on a product image (thumbnail).
        product_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']"))
        )
        if product_link:
            product_link.click()
        else:
            self.fail("Product link not found")

        # 4. Select a size.
        size_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='option-button'][text()='L']"))
        )

        if size_button:
            size_button.click()
        else:
            self.fail("Size button not found")

        # 5. Click the "Add to Cart" button.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
        )
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found")

        # 6. Click the cart button to open the cart.
        cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='headlessui-popover-button-:Rrmdtt7:']"))
        )
        if cart_button:
            cart_button.click()
        else:
            self.fail("Cart button not found")

        # 7. Verify that the "GO TO CHECKOUT" button is present.
        go_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='go-to-cart-button'] button[data-testid='go-to-cart-button']"))
        )

        if go_to_checkout_button:
            print("GO TO CHECKOUT button is present")
        else:
            self.fail("GO TO CHECKOUT button is not present")

if __name__ == "__main__":
    unittest.main()