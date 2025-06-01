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
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except Exception:
            self.fail("Cookies accept button not found")

        # Hover over "Olive Table" to reveal "Add to cart" button
        try:
            product_hover = wait.until(EC.visibility_of_element_located((By.XPATH, "//h3/a[text()='Olive Table']/../..")))
            ActionChains(driver).move_to_element(product_hover).perform()
        except Exception:
            self.fail("Product 'Olive Table' not found or hover failed")
        
        # Click "Add to cart" button
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//h3/a[text()='Olive Table']/../..//button[@title='Add to cart']")))
            add_to_cart_button.click()
        except Exception:
            self.fail("'Add to cart' button not found or not clickable")

        # Open cart popup by clicking cart icon
        try:
            cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
            cart_icon.click()
        except Exception:
            self.fail("Cart icon not found or not clickable")
        
        # Check if cart popup contains at least one item
        try:
            cart_item = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".single-shopping-cart")))
            self.assertIsNotNone(cart_item, "Cart is empty after adding a product")
        except Exception:
            self.fail("Cart popup did not show any item")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()