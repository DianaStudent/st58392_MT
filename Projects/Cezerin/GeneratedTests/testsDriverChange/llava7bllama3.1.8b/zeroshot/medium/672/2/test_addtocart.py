import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # Click on product category
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category']"))).click()
        
        # Select the first product
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/1']"))).click()

        # Click the "Add to cart" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='add-to-cart']"))).click()
        
        # Click the cart icon/button to open the shopping bag.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@class='cart-button']"))).click()

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        cart_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='#']")))
        self.assertIn("GO TO CHECKOUT", cart_button.text)

if __name__ == '__main__':
    unittest.main()