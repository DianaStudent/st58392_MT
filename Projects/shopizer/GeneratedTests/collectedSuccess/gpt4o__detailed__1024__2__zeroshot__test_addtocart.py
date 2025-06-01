import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Accept cookies if present
        try:
            accept_cookies_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            pass  # Cookie banner might not exist

        # Step 2: Hover over the first product to reveal "Add to cart" button
        product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product-wrap-2')))
        ActionChains(driver).move_to_element(product).perform()
        
        # Step 3: Click "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.product-action-2 button[title="Add to cart"]')))
        add_to_cart_button.click()

        # Step 4: Click the cart icon to open the popup cart
        cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.icon-cart')))
        cart_icon.click()

        # Step 5: Wait for the popup to become visible
        cart_popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.shopping-cart-content.active')))
        self.assertIsNotNone(cart_popup, "Cart popup did not open.")

        # Step 6: Click "View cart" button
        view_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.shopping-cart-btn a[href="/cart"]')))
        view_cart_button.click()

        # Step 7: Verify product appears in the cart list
        cart_page_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cart-table-content .product-name a')))
        self.assertIsNotNone(cart_page_product, "Product is not present in the cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()