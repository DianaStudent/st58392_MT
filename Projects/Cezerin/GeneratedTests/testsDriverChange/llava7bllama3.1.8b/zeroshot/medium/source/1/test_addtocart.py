import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")

    def test_add_to_cart(self):
        # Open product category page
        product_category_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/product-category']")))
        product_category_link.click()

        # Select the first product
        product_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/product-1']")))
        product_link.click()

        # Click "Add to cart" button
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='add-to-cart']")))
        add_to_cart_button.click()

        # Open shopping bag
        cart_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button")))
        cart_button.click()

        # Wait for presence of "GO TO CHECKOUT" button
        go_to_checkout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class='go-to-checkout']"))))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()