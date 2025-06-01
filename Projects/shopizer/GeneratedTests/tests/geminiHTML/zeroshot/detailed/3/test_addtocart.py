import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies if present
        try:
            cookie_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # Hover over the first product
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
        actions = ActionChains(driver)
        actions.move_to_element(first_product).perform()

        # Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")))
        add_to_cart_button.click()

        # Click the cart icon to open the popup cart
        cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header-right-wrap .icon-cart")))
        cart_icon.click()

        # Wait for the popup to become visible
        cart_popup = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active")))

        # Check that the popup contains at least one item
        cart_items = cart_popup.find_elements(By.CSS_SELECTOR, ".single-shopping-cart")
        if not cart_items:
            self.fail("Cart is empty after adding a product.")

        # Click "View Cart" button
        view_cart_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # Verify that the product appears in the cart list on the cart page
        cart_page_product_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-main-area .product-name a")))
        if not cart_page_product_name.text:
            self.fail("Product name not found on cart page.")

if __name__ == "__main__":
    unittest.main()