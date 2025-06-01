from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")  # Load the local file

    def test_add_to_cart(self):
        driver = self.driver

        try:
            # Navigate to Category A
            category_a_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']"))
            )
            category_a_link.click()

            # Load the Category A page from local file
            driver.get("http://localhost:3000/")

            # Navigate to Product A
            product_a_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']"))
            )
            product_a_link.click()

            # Load the Product page from local file
            driver.get("http://localhost:3000/")

            # Add product to cart
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]"))
            )
            add_to_cart_button.click()

            # Load the Popup from local file, simulating that the product is added
            driver.get("http://localhost:3000/")

            # Click on the cart button
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@class='cart-button']"))
            )
            cart_button.click()

            # Verify if "GO TO CHECKOUT" is present which indicates success
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Go to checkout')]"))
            )

            if not go_to_checkout_button:
                self.fail("Failed to find 'GO TO CHECKOUT' button")

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()