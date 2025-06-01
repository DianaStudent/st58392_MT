import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        actions = ActionChains(driver)

        try:
            # Accept cookies
            accept_cookies = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies.click()
        except TimeoutException:
            self.fail("Cookie consent button not found")

        # Hover over the first product to reveal the "Add to cart" button
        product_locator = (By.CSS_SELECTOR, "div.product-wrap-2")
        products = wait.until(
            EC.presence_of_all_elements_located(product_locator)
        )

        if not products:
            self.fail("No products found on the page")

        first_product = products[0]
        actions.move_to_element(first_product).perform()

        # Click the revealed "Add to cart" button
        add_to_cart_btn_locator = (By.CSS_SELECTOR, "div.product-action-2 button[title='Add to cart']")
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable(add_to_cart_btn_locator)
            )
            add_to_cart_button.click()
        except (TimeoutException, ElementClickInterceptedException):
            self.fail("Add to cart button is not clickable")

        # Click the cart icon to open the popup cart
        cart_icon_locator = (By.CSS_SELECTOR, "button.icon-cart")
        try:
            cart_icon = wait.until(
                EC.element_to_be_clickable(cart_icon_locator)
            )
            cart_icon.click()
        except (TimeoutException, ElementClickInterceptedException):
            self.fail("Cart icon is not clickable")

        # Wait for the popup to become visible
        cart_popup_locator = (By.CSS_SELECTOR, "div.shopping-cart-content.active")
        try:
            cart_popup = wait.until(
                EC.visibility_of_element_located(cart_popup_locator)
            )
        except TimeoutException:
            self.fail("Cart popup is not visible")

        if not cart_popup.text:
            self.fail("Cart popup is empty")

        # Click "View cart" or similar button inside the popup
        view_cart_btn_locator = (By.CSS_SELECTOR, "a[href='/cart']")
        try:
            view_cart_button = wait.until(
                EC.element_to_be_clickable(view_cart_btn_locator)
            )
            view_cart_button.click()
        except TimeoutException:
            self.fail("View Cart button is not clickable")

        # On the cart page, verify that the product appears in the cart list
        cart_page_locator = (By.CSS_SELECTOR, "table.cart-table-content")
        try:
            cart_table = wait.until(
                EC.presence_of_element_located(cart_page_locator)
            )
        except TimeoutException:
            self.fail("Cart table is not visible")

        if not cart_table.text:
            self.fail("Cart table is empty")

        self.assertTrue("Chair" in cart_table.text or "Olive Table" in cart_table.text, 
                        "Product is not added to cart or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()