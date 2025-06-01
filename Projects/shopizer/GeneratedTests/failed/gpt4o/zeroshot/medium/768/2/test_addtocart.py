from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

        # Accept cookies
        try:
            accept_cookies_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_btn.click()
        except Exception as e:
            self.fail(f"Cookie acceptance button not found: {str(e)}")

    def test_add_to_cart(self):
        driver = self.driver

        # Hover over the first product to reveal the Add to Cart button
        try:
            product_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
            ActionChains(driver).move_to_element(product_element).perform()

            add_to_cart_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")))
            add_to_cart_btn.click()
        except Exception as e:
            self.fail(f"Add to cart button not found or not clickable: {str(e)}")

        # Open the cart popup by clicking the cart icon
        try:
            cart_icon = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
            cart_icon.click()
        except Exception as e:
            self.fail(f"Cart icon not found or not clickable: {str(e)}")
        
        # Verify that at least one product is listed in the popup cart
        try:
            cart_content = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active ul")))
            cart_items = cart_content.find_elements(By.CSS_SELECTOR, ".single-shopping-cart")
            self.assertTrue(len(cart_items) > 0, "No items were found in the popup cart")
        except Exception as e:
            self.fail(f"Popup cart not found or empty: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()