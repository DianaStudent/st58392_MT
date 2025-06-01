from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_product_to_cart(self):
        try:
            # Click on the "Medusa Store" link to go to the store page
            store_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-store-link']")))
            store_link.click()

            # Click on the product link "Medusa Sweatshirt"
            product_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/dk/products/sweatshirt']")))
            product_link.click()

            # Select the size 'L' for the product
            size_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
            size_button.click()

            # Click on the "Add to cart" button
            add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='add-product-button']")))
            add_to_cart_button.click()

            # Click on the cart button in the navigation
            cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-cart-link']")))
            cart_button.click()

            # Verify the presence of the "GO TO CHECKOUT" button
            checkout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='go-to-cart-button']")))
        
        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

    def tearDown(self):
        # Quit the browser session
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()