from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        
        # Find and hover over the first product
        product = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.product-wrap-2'))
        )

        actions = ActionChains(driver)
        actions.move_to_element(product).perform()
        
        # Find and click the "Add to cart" button
        add_to_cart_button = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.product-action-2 button[title="Add to cart"]'))
        )
        add_to_cart_button.click()
        
        # Click the cart icon to open the popup cart
        cart_icon = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.icon-cart'))
        )
        cart_icon.click()

        # Wait for the cart popup to become visible
        cart_popup = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.shopping-cart-content'))
        )
        
        # Check the popup contains at least one item
        if not cart_popup:
            self.fail("Cart popup did not become visible or is empty.")

        # Click "View Cart" in the popup
        view_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'View Cart'))
        )
        view_cart_button.click()

        # On the cart page, verify the product appears in the cart list
        product_in_cart = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.cart-table-content .product-name a'))
        )
        if not product_in_cart:
            self.fail("Product not found in the cart list.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()