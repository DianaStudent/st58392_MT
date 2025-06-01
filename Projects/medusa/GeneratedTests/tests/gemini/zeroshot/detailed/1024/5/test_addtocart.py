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
        wait = WebDriverWait(driver, 20)

        # 1. Open home page. (Done in setUp)

        # 2. Click the menu button ("Menu").
        menu_button_locator = (By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")
        menu_button = wait.until(EC.presence_of_element_located(menu_button_locator))
        menu_button.click()

        # 3. Click the "Store" link.
        store_link_locator = (By.CSS_SELECTOR, "a[data-testid='store-link']")
        store_link = wait.until(EC.presence_of_element_located(store_link_locator))
        store_link.click()

        # 4. Click on a product image (Thumbnail) - first product.
        product_wrapper_locator = (By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt'] div[data-testid='product-wrapper'] div img[alt='Thumbnail']")
        product_wrapper = wait.until(EC.presence_of_element_located(product_wrapper_locator))
        product_wrapper.click()

        # 5. Select size by clicking the size button "L".
        size_button_locator = (By.CSS_SELECTOR, "button[data-testid='option-button']:nth-child(1)")
        size_button = wait.until(EC.presence_of_element_located(size_button_locator))
        size_button.click()

        # 6. Add the product to the cart.
        add_to_cart_button_locator = (By.CSS_SELECTOR, "button[data-testid='add-product-button']")
        add_to_cart_button = wait.until(EC.presence_of_element_located(add_to_cart_button_locator))
        add_to_cart_button.click()

        # 7. Explicitly click the cart button to open the cart.
        cart_button_locator = (By.CSS_SELECTOR, "button[id='headlessui-popover-button-:Rrmdtt7:']")
        cart_button = wait.until(EC.presence_of_element_located(cart_button_locator))
        cart_button.click()

        # 8. Verify that the "GO TO CHECKOUT" button is present.
        go_to_checkout_button_locator = (By.CSS_SELECTOR, "a[data-testid='go-to-cart-button'] button[data-testid='go-to-cart-button']")
        go_to_checkout_button = wait.until(EC.presence_of_element_located(go_to_checkout_button_locator))

        if go_to_checkout_button:
            print("Go to checkout button found")
        else:
            self.fail("Go to checkout button not found")

if __name__ == "__main__":
    unittest.main()