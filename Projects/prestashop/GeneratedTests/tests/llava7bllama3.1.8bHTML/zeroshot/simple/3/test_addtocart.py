import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('your_url')

    def test_add_to_cart_and_confirm_success(self):
        # Click on an add to cart button
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.add-to-cart'))
        )
        add_to_cart_button.click()

        # Wait for the modal confirmation to appear after adding to cart
        modal_title = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.modal-title'))
        )

        # Confirm success by verifying the presence of the modal title that contains "successfully added"
        self.assertIn('successfully', modal_title.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()