import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.url = "http://localhost/"

    def test_add_to_cart(self):
        driver = self.driver
        driver.get(self.url)

        wait = WebDriverWait(driver, 20)
        
        # Accept cookies
        try:
            accept_cookies_btn = wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_btn.click()
        except Exception as e:
            self.fail(f"Failed to locate and click accept cookies button: {str(e)}")

        # Hover over the first product to reveal the "Add to cart" button
        try:
            first_product = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2 .product-img"))
            )
            ActionChains(driver).move_to_element(first_product).perform()
            
            add_to_cart_btn = wait.until(
                EC.visibility_of_element_located((By.XPATH, ".//*[contains(@class, 'fa-shopping-cart')]/.."))
            )
            add_to_cart_btn.click()
        except Exception as e:
            self.fail(f"Failed to hover and click add to cart: {str(e)}")
        
        # Click the cart icon to open the popup cart
        try:
            cart_icon = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".icon-cart"))
            )
            cart_icon.click()
        except Exception as e:
            self.fail(f"Failed to locate and click cart icon: {str(e)}")
        
        # Wait for the popup to become visible
        try:
            cart_popup = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active"))
            )
        except Exception as e:
            self.fail(f"Cart popup not visible: {str(e)}")
        
        # Click "View cart" button inside the popup
        try:
            view_cart_btn = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "VIEW CART"))
            )
            view_cart_btn.click()
        except Exception as e:
            self.fail(f"Failed to locate and click view cart button: {str(e)}")
        
        # On the cart page, verify that the product appears in the cart list
        try:
            product_in_cart = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-table-content .product-name"))
            )
            
            if not product_in_cart.text:
                self.fail("Product name is empty, product not added to cart successfully")
                
        except Exception as e:
            self.fail(f"Product not present in cart page: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()