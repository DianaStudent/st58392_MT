from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/')  # Replace with your URL

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_and_confirm(self):
        # Click on the product to add it to cart
        product = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.add-to-cart'))
        )
        product.click()

        # Wait for the modal confirmation to appear
        modal_title = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#myModalLabel'))
        )

        # Verify that the modal title contains "successfully added"
        self.assertIn('successfully', modal_title.text.lower())

if __name__ == '__main__':
    unittest.main()