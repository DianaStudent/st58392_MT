from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_add_to_cart_process(self):
        driver = self.driver
        
        # Accept cookies if button is available
        try:
            accept_cookies_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except:
            self.fail("Cookie accept button not found")

        # Hover over "Olive Table" product to reveal "Add to cart" button
        try:
            product_element = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/product/olive-table']"))
            )
            hover = ActionChains(driver).move_to_element(product_element)
            hover.perform()
            
            add_to_cart_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/product/olive-table'] ~ div.product-action-2 button[title='Add to cart']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button for Olive Table not found or clickable")

        # Open cart popup by clicking cart icon
        try:
            cart_icon = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart"))
            )
            cart_icon.click()
        except:
            self.fail("Cart icon not found or clickable")

        # Confirm success by checking that the popup contains at least one item
        try:
            cart_item = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".single-shopping-cart"))
            )
            assert cart_item is not None, "No items in cart popup."
        except:
            self.fail("Cart popup does not contain any items")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()