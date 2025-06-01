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
        wait = WebDriverWait(driver, 20)

        # 1. Open home page. Already done in setUp

        # 2. Click the menu button ("Menu").
        menu_button_locator = (By.DATA_TESTID, "nav-menu-button")
        menu_button = wait.until(EC.element_to_be_clickable(menu_button_locator))
        if menu_button:
            menu_button.click()
        else:
            self.fail("Menu button not found")

        # 3. Click the "Store" link.
        store_link_locator = (By.DATA_TESTID, "store-link")
        store_link = wait.until(EC.element_to_be_clickable(store_link_locator))
        if store_link:
            store_link.click()
        else:
            self.fail("Store link not found")

        # 4. Click on a product image (Thumbnail) - first product.
        product_wrapper_locator = (By.DATA_TESTID, "product-wrapper")
        product_wrappers = wait.until(EC.presence_of_all_elements_located(product_wrapper_locator))
        if product_wrappers:
            first_product = product_wrappers[0]
            first_product.click()
        else:
            self.fail("Product wrappers not found")

        # 5. Select size by clicking the size button "L".
        size_button_locator = (By.DATA_TESTID, "option-button")
        size_buttons = wait.until(EC.presence_of_all_elements_located(size_button_locator))
        if size_buttons:
            size_l_button = None
            for button in size_buttons:
                if button.text == "L":
                    size_l_button = button
                    break
            if size_l_button:
                size_l_button.click()
            else:
                self.fail("Size L button not found")
        else:
            self.fail("Size buttons not found")

        # 6. Add the product to the cart.
        add_to_cart_button_locator = (By.DATA_TESTID, "add-product-button")
        add_to_cart_button = wait.until(EC.element_to_be_clickable(add_to_cart_button_locator))
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found")

        # 7. Explicitly click the cart button to open the cart.
        nav_cart_link_locator = (By.DATA_TESTID, "nav-cart-link")
        nav_cart_link = wait.until(EC.element_to_be_clickable(nav_cart_link_locator))
        if nav_cart_link:
            nav_cart_link.click()
        else:
            self.fail("Cart button not found")

        # 8. Verify that the "GO TO CHECKOUT" button is present.
        go_to_checkout_button_locator = (By.DATA_TESTID, "checkout-button")
        go_to_checkout_button = wait.until(EC.element_to_be_clickable(go_to_checkout_button_locator))
        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button not found")

if __name__ == "__main__":
    unittest.main()