import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies if present
        try:
            cookie_button = wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
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
            EC.presence_of_element_located((By.CSS_SELECTOR, ".header-right-wrap .cart-wrap.d-none.d-lg-block .icon-cart"))
        )
        cart_icon.click()

        # Wait for the popup to become visible
        cart_popup = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".header-right-wrap .cart-wrap.d-none.d-lg-block .shopping-cart-content.active"))
        )

        # Verify that the popup contains at least one item
        cart_items = cart_popup.find_elements(By.CSS_SELECTOR, "ul li.single-shopping-cart")
        if not cart_items:
            self.fail("Cart is empty after adding product.")

        # Click "View Cart" button inside the popup
        view_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".header-right-wrap .cart-wrap.d-none.d-lg-block .shopping-cart-content .shopping-cart-btn.btn-hover.text-center a[href='/cart']"))
        )
        view_cart_button.click()

        # On the cart page, verify that the product appears in the cart list
        cart_page_product_name = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-main-area .cart-table-content table tbody tr:nth-child(1) .product-name a"))
        )

        if not cart_page_product_name.text:
            self.fail("Product name is empty in cart page.")

        self.assertNotEqual(cart_page_product_name.text, "", "Product not found in cart list.")


if __name__ == "__main__":
    unittest.main()