import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")  # Run headless if necessary
        options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost/")

    def test_add_to_cart(self):
        # Accept cookies if the button exists
        try:
            cookie_accept_button = self.wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_accept_button.click()
        except:
            self.fail("Cookie accept button not found.")

        # Hover over the product image to reveal the 'Add to cart' button
        product = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/product/olive-table']"))
        )
        add_to_cart_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@title='Add to cart']"))
        )

        ActionChains(self.driver).move_to_element(product).perform()

        # Click the 'Add to cart' button
        add_to_cart_button.click()

        # Open the cart popup by clicking the cart icon
        cart_icon = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "icon-cart"))
        )
        cart_icon.click()

        # Verify that at least one product is listed in the popup cart
        shopping_cart_content = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping-cart-content"))
        )
        cart_items = shopping_cart_content.find_elements(By.CLASS_NAME, "single-shopping-cart")

        self.assertTrue(cart_items, "Cart is empty after adding a product.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()