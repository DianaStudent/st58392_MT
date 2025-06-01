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
        # 1. Open home page.
        self.assertEqual(driver.current_url, "http://localhost:8000/dk/")
        
        # 2. Click the menu button ("Menu").
        menu_button_locator = (By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")
        menu_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(menu_button_locator))
        menu_button.click()

        # 3. Click the "Store" link.
        store_link_locator = (By.CSS_SELECTOR, "a[data-testid='store-link']")
        store_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(store_link_locator))
        store_link.click()

        # 4. Click on a product image (Thumbnail) - first product.
        product_wrapper_locator = (By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']")
        product_wrapper = WebDriverWait(driver, 20).until(EC.presence_of_element_located(product_wrapper_locator))
        product_wrapper.click()

        # 5. Select size by clicking the size button "L".
        size_button_locator = (By.XPATH, "//button[@data-testid='option-button'][text()='L']")
        size_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(size_button_locator))
        size_button.click()

        # 6. Add the product to the cart.
        add_to_cart_button_locator = (By.CSS_SELECTOR, "button[data-testid='add-product-button']")
        add_to_cart_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(add_to_cart_button_locator))
        add_to_cart_button.click()

        # 7. Explicitly click the cart button to open the cart.
        cart_button_locator = (By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")
        cart_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(cart_button_locator))
        cart_button.click()

        # 8. Verify that the "GO TO CHECKOUT" button is present.
        go_to_checkout_button_locator = (By.CSS_SELECTOR, "a[data-testid='checkout-button']")
        go_to_checkout_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(go_to_checkout_button_locator))
        self.assertTrue(go_to_checkout_button.is_displayed())

if __name__ == "__main__":
    unittest.main()