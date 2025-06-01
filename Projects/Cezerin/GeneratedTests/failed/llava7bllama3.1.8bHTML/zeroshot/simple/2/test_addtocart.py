from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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

    def test_add_to_cart(self):
        self.driver.get("data:,<!DOCTYPE html><html><body>{}</body></html>".format(html_data))
        
        # Wait for the product name to be present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.product-name")))
        
        # Click on add to cart button
        self.driver.find_element(By.BUTTON_TYPE, "button").click()
        
        # Wait for the cart button to be present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='cart']")))
        
        # Click on the cart button
        self.driver.find_element(By.XPATH, "//a[@class='cart']").click()
        
        # Wait for the "GO TO CHECKOUT" button to be present
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart")))
        
        # Check if "GO TO CHECKOUT" button is present
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".button-addtocart").text == "GO TO CHECKOUT")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()