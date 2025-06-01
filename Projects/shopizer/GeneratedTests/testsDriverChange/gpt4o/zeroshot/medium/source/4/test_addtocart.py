from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ShopizerAddToCartTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window() 
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

        # Accept cookies if present
        try:
            accept_cookies_btn = self.wait.until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button')))
            accept_cookies_btn.click()
        except Exception:
            pass

    def test_add_to_cart(self):
        driver = self.driver
        
        # Hover to reveal "Add to cart" button
        product_img = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".product-img a[href='/product/olive-table']")
        ))
        actions = ActionChains(driver)
        actions.move_to_element(product_img).perform()

        # Click "Add to cart"
        add_to_cart_btn = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[title='Add to cart']")
        ))
        add_to_cart_btn.click()

        # Click the cart icon
        cart_icon = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
        cart_icon.click()

        # Verify the cart popup contains at least one item
        cart_items = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".single-shopping-cart")
        ))
        
        if not cart_items:
            self.fail("Cart popup does not contain any items.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()