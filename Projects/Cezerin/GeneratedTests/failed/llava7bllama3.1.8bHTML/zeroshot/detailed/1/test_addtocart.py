from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/") # replace with your homepage URL

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # Open home page
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Click on product category
        self.driver.find_element(By.XPATH, "//a[@href='/category-a']").click() # replace with actual href

        # Select the first product
        self.driver.find_element(By.XPATH, "//a[@href='/product-a']").click() # replace with actual href

        # Click the "Add to cart" button
        self.driver.find_element(By.CSS_SELECTOR, ".button-addtocart > button").click()

        # Explicitly click the cart icon (shopping bag) to open the mini-cart
        self.driver.find_element(By.CSS_SELECTOR, ".cart-button").click()

        # Wait for the mini-cart to become visible
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".mini-cart")))

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = self.driver.find_element(By.XPATH, "//button[@class='button is-success'][contains(text(), 'GO TO CHECKOUT')]")
        self.assertTrue(go_to_checkout_button.is_displayed())

if __name__ == '__main__':
    unittest.main()