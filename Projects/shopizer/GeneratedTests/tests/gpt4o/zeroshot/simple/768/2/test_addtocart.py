import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        
        # Accept cookies if the button exists
        try:
            accept_button = self.wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            accept_button.click()
        except:
            pass  # If it's not there, no action is needed

        # Locate the first product's "Add to cart" button
        product = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        
        # Hover over the product to reveal the "Add to cart" button
        ActionChains(driver).move_to_element(product).perform()
        
        # Click the "Add to cart" button
        add_to_cart_btn = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']"))
        )
        add_to_cart_btn.click()

        # Open the cart popup by clicking the cart icon
        cart_icon = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".icon-cart"))
        )
        cart_icon.click()

        # Check that the cart popup contains at least one item
        try:
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active .single-shopping-cart"))
            )
        except:
            self.fail("Cart popup did not contain any items.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()