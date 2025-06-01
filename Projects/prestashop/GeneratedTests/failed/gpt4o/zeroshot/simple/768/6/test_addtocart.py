from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/')

    def test_add_to_cart(self):
        try:
            driver = self.driver
            
            # Navigate to "Art" category
            art_category_menu = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Art'))
            )
            art_category_menu.click()
            
            # Select "The best is yet to come' Framed poster" product
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "The best is yet to come'..."))
            )
            product_link.click()
            
            # Click "Add to Cart" button
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart"))
            )
            add_to_cart_button.click()
            
            # Wait for the modal to appear and confirm success
            modal_header = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "h4.modal-title.h6.text-sm-center"))
            )
            self.assertIn("successfully added", modal_header.text.lower())
        
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()