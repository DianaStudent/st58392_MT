import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_cart_functionality(self):
        self.driver.get("http://localhost:8000")

        # Find the first product item
        product_item = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-item']"))
        )

        # Hover over the first product to reveal the "Add to cart" button
        self.driver.execute_script("arguments[0].mouseover();", product_item)

        # Find the "Add to cart" button
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary']"))
        )

        # Click the "Add to cart" button
        add_to_cart_button.click()

        # Find the cart icon and click it to open the popup cart
        cart_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='cart-icon']"))
        )
        cart_icon.click()

        # Wait for the popup to become visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='popup-cart']")))

        # Find the "View cart" button inside the popup and click it
        view_cart_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='btn btn-primary']"))
        )
        view_cart_button.click()

        # Navigate to the cart page
        self.driver.get("http://localhost:8000/cart")

        # Find the product in the cart list
        product_in_cart = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='cart-item']"))
        )

        # Verify that the product appears in the cart list
        self.assertIsNotNone(product_in_cart)
        self.assertNotEmpty(product_in_cart.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()