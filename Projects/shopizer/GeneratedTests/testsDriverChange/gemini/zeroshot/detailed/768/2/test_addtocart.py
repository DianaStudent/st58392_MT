import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            cookie_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # Hover over the first product
        product_element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".col-xl-3.col-md-6.col-lg-4.col-sm-6:nth-child(1) .product-wrap-2"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(product_element).perform()

        # Click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".col-xl-3.col-md-6.col-lg-4.col-sm-6:nth-child(1) .product-wrap-2 .product-action-2 button[title='Add to cart']"))
        )
        add_to_cart_button.click()

        # Click the cart icon to open the popup cart
        cart_icon = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".header-right-wrap .cart-wrap .icon-cart"))
        )
        cart_icon.click()

        # Wait for the popup to become visible
        cart_popup = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".header-right-wrap .cart-wrap .shopping-cart-content.active"))
        )

        # Click "View cart" button inside the popup
        view_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".header-right-wrap .cart-wrap .shopping-cart-content .shopping-cart-btn a[href='/cart']"))
        )
        view_cart_button.click()

        # On the cart page, verify that the product appears in the cart list
        cart_item = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-main-area .cart-table-content tbody tr"))
        )
        self.assertIsNotNone(cart_item, "Cart item not found on the cart page.")

if __name__ == "__main__":
    unittest.main()