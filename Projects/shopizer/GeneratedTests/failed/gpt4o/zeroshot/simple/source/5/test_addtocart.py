from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_add_to_cart(self):
        driver = self.driver
        
        # Accept cookies
        try:
            accept_cookies_btn = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_btn.click()
        except Exception:
            self.fail("Accept cookies button not found")
        
        # Hover over first product to reveal 'Add to cart' button
        try:
            product = self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='product-wrap-2 mb-25'][1]"))
            )
            ActionChains(driver).move_to_element(product).perform()

            add_to_cart_btn = product.find_element(By.XPATH, ".//button[@title='Add to cart']")
            add_to_cart_btn.click()
        except Exception:
            self.fail("Add to cart button for first product not found")
        
        # Open cart popup by clicking the cart icon
        try:
            cart_button = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_button.click()
        except Exception:
            self.fail("Cart button not found")
        
        # Confirm success by checking that the cart popup contains at least one item
        try:
            cart_popup = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart-content"))
            )
            items_in_cart = cart_popup.find_elements(By.CLASS_NAME, "single-shopping-cart")
            self.assertGreater(len(items_in_cart), 0, "Cart popup is empty")
        except Exception:
            self.fail("Cart popup not found or empty")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()