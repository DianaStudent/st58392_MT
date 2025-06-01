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
        self.url = "http://localhost:8000/dk"
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open home page.
        self.assertEqual(driver.current_url, self.url)

        # 2. Click the menu button ("Menu").
        menu_button_locator = (By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")
        menu_button = wait.until(EC.presence_of_element_located(menu_button_locator))
        if menu_button:
            menu_button.click()
        else:
            self.fail("Menu button not found")

        # 3. Click the "Store" link.
        store_link_locator = (By.CSS_SELECTOR, "a[data-testid='store-link']")
        store_link = wait.until(EC.presence_of_element_located(store_link_locator))
        if store_link:
            store_link.click()
        else:
            self.fail("Store link not found")

        # 4. Click on a product image (Thumbnail) - first product.
        product_wrapper_locator = (By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']")
        product_wrapper = wait.until(EC.presence_of_element_located(product_wrapper_locator))
        if product_wrapper:
            product_wrapper.click()
        else:
            self.fail("Product wrapper not found")

        # 5. Select size by clicking the size button "L".
        size_button_locator = (By.XPATH, "//button[@data-testid='option-button'][text()='L']")
        size_button = wait.until(EC.presence_of_element_located(size_button_locator))
        if size_button:
            size_button.click()
        else:
            self.fail("Size button not found")

        # 6. Add the product to the cart.
        add_to_cart_button_locator = (By.CSS_SELECTOR, "button[data-testid='add-product-button']")
        add_to_cart_button = wait.until(EC.presence_of_element_located(add_to_cart_button_locator))
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found")

        # 7. Explicitly click the cart button to open the cart.
        nav_cart_link_locator = (By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")
        nav_cart_link = wait.until(EC.presence_of_element_located(nav_cart_link_locator))
        if nav_cart_link:
            nav_cart_link.click()
        else:
            self.fail("Cart link not found")

        # 8. Verify that the "GO TO CHECKOUT" button is present.
        go_to_checkout_button_locator = (By.CSS_SELECTOR, "a[data-testid='checkout-button']")
        go_to_checkout_button = wait.until(EC.presence_of_element_located(go_to_checkout_button_locator))
        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button is not present")

if __name__ == "__main__":
    unittest.main()