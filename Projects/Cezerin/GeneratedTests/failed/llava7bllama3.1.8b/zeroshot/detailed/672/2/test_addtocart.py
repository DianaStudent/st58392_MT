from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # Click on product category (e.g. Category A)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/category/a']"))
        ).click()
        
        # Select the first product (e.g. Product A)
        product_link = self.driver.find_element(By.XPATH, "(//a[@class='product-name'])[1]")
        product_link.click()

        # Click the "Add to cart" button
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart']"))
        ).click()
        
        # Explicitly click the shopping bag icon (cart-button) to open the mini-cart
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button"))
        ).click()

        # Wait for the mini-cart to become visible and assert presence of "GO TO CHECKOUT" button
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@class='checkout']"))
        )
        
        checkout_button = self.driver.find_element(By.XPATH, "//button[@class='checkout']")
        self.assertTrue(checkout_button.is_displayed())

if __name__ == "__main__":
    unittest.main()